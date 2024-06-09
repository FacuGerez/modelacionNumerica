import math
from tabulate import tabulate
from algorithms.PVI.euler import euler, _euler_Exp
from algorithms.PVI.rungekuta import _runge2
from peticionarconpadron import peticionar_const


def main():
    #-----------------------Constantes--------------------------------

    cons:dict[str,float] = peticionar_const()
    tiempo = list(cons["I"].keys()) # [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]

    #-----------------------Ecuaciones--------------------------------

    Qent = lambda C,t: C*cons["I"][t]*cons["Aterr"]* (1/1000)
    H = lambda V: cons["Hs"] - (V/cons["Asot"]) if (cons["Hs"] - (V/cons["Asot"])) > cons["Hmin"] and (cons["Hs"] - (V/cons["Asot"])) < cons["Hmax"] else cons["Hmax"] if (cons["Hs"] - (V/cons["Asot"])) > cons["Hmax"] else cons["Hmin"]
    Qsal = lambda Qmax,V: Qmax * math.sqrt((cons["Hmax"] - H(V))/(cons["Hmax"]-cons["Hmin"]))
    V = lambda C,t,V: Qent(C,t) - Qsal(V)
    C = lambda V,C: (V/(cons["Vsot"]*cons["tk"])) * (cons["Csat"]-C)

    #-----------------------Pre-functions--------------------------------

    def modelar(fV,fC,h,model) -> list: # Aca se modela el sistema de ecuaciones diferenciales paso a paso
        resultado = []
        i = 0
        NewV = 0
        NewC = cons["C0"]
        resultado.append([0, NewV, NewC, NewV/cons["Asot"]]) # Aca se guarda el primer resultado en la lista
        while NewV >= 0 and i >= 0: #corta la iteracion cuando NewV es menor a 0 osea q se vacio
            t = h*i # Aca se calcula el tiempo desde t=0 hasta t= 0+h*i donde h avanza de a 1 minuto
            NewV = model(NewV, t, lambda _,y: fV(NewC,t,y), h) # Aca se hace el euler paso a paso de la ecuacion 1
            NewC = model(NewC, t, lambda _,y: fC(NewV,y), h) # Aca se hace el euler paso a paso de la ecuacion 6
            i+=1
            resultado.append([t+h, NewV, NewC,NewV/cons["Asot"]]) # Aca se guarda el resultado de cada iteracion en la lista
        return resultado

    with open("tablas.txt", "w") as archivo: # Abre el archivo en modo escritura
        #-----------------------A1--------------------------------

        archivo.write("A1)\n")  # Escribe el contenido en el archivo
        A1 = euler(0,0,lambda t,y: Qent(1,1),h=1/60,tk=1)
        tabulado = tabulate(A1,headers=["Tiempo", "Volumen"],tablefmt='grid',stralign='center', numalign= 'center')
        archivo.write(tabulado) # Escribe el contenido en el archivo
        """print()
        print("A1")
        print(tabulado)"""

        #-----------------------A2--------------------------------

        for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
            h = (1/60) * (tk if tk > 1 else 1)
            resultA2 = modelar(lambda C,t,newV: (Qent(C,tk)- Qsal(cons["Qmax"],newV)) if t<tk else (0 - Qsal(cons["Qmax"],newV)),
                            lambda V,newC: C(V,newC),
                            h,
                            _euler_Exp)
            archivo.write(f"\n\nA2) with tk = {tk}h and h= {h} \n")
            tabulado = tabulate(resultA2,headers=["Tiempo", "Volumen", "C", "H"],tablefmt='grid',stralign='center', numalign= 'center')
            archivo.write(tabulado)
            """print()
            print("A2 with tk = ",tk,"h and h= ",h)
            print(tabulado)
            _ = input("Press Enter to continue...")"""

        #-----------------------B y C--------------------------------

        NewQmax = 1
        for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
            NewQmax = max(NewQmax, ((0.9*cons["I"][tk]*cons["Aterr"]*(1/1000)) - (0.25*cons["Asot"]/tk))) #aproximadamente
        NewQmax = int(NewQmax)+2

        #-----------------------B1--------------------------------

        for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
            h = 1/60 * (tk if tk > 1 else 1)
            BQsal = lambda V: Qsal(NewQmax, V)
            resultB = modelar(lambda C,t,newV: (Qent(C,tk)- BQsal(newV)) if t<tk else (0 - BQsal(newV)),
                            lambda V,newC: C(V,newC),
                            h,
                            _euler_Exp)

            archivo.write(f"\n\nB1) with tk = {tk}h and h= {h}\n")
            tabulado = tabulate(resultB,headers=["Tiempo", "Volumen", "C", "H"],tablefmt='grid',stralign='center', numalign= 'center')
            archivo.write(tabulado)
            """print()
            print("B1 with tk = ",tk,"h and h= ",h)
            print(tabulado)
            next = input("Press Enter to continue...")"""

        #-----------------------C1--------------------------------

        tk = tiempo[4] # 1h
        hrunge = 1/60
        heuler1 = 5/60
        heuler2 = 10/60
        CQsal = lambda V: Qsal(NewQmax, V)
        resultC1Euler1 = modelar(lambda C,t,newV: (Qent(C,tk)- CQsal(newV)) if t<tk else (0 - CQsal(newV)),
                            lambda V,newC: C(V,newC),
                            heuler1,
                            _euler_Exp)
        resultC1Euler2 = modelar(lambda C,t,newV: (Qent(C,tk)- CQsal(newV)) if t<tk else (0 - CQsal(newV)),
                            lambda V,newC: C(V,newC),
                            heuler2,
                            _euler_Exp)
        resultC1Runge = modelar(lambda C,t,newV: (Qent(C,tk)- CQsal(newV)) if t<tk else (0 - CQsal(newV)),
                            lambda V,newC: C(V,newC),
                            hrunge,
                            _runge2)


        for i in range(len(resultC1Euler1)):
            resultC1Euler1[i].pop(3)
        for i in range(len(resultC1Euler2)):
            resultC1Euler2[i].pop(3)
        for i in range(len(resultC1Runge)):
            resultC1Runge[i].pop(0)
            resultC1Runge[i].pop(2)

        for i in range(len(resultC1Euler1)):
            if i*5 >= len(resultC1Runge):
                resultC1Euler1[i] += [0,0,0,0]
                break
            resultC1Euler1[i] += resultC1Runge[i*5] + [abs(resultC1Euler1[i][1]-resultC1Runge[i*5][0]),abs(resultC1Euler1[i][2]-resultC1Runge[i*5][1])]
        for i in range(len(resultC1Euler2)):
            if i*10 >= len(resultC1Runge):
                resultC1Euler2[i] += [0,0,0,0]
                break
            resultC1Euler2[i] += resultC1Runge[i*10] + [abs(resultC1Euler2[i][1]-resultC1Runge[i*10][0]),abs(resultC1Euler2[i][2]-resultC1Runge[i*10][1])]

        archivo.write(f"\n\nC1) with tk = {tk}h\n")
        archivo.write(f"First Euler and h={heuler1}\n")
        tabulado = tabulate(resultC1Euler1,headers=["Tiempo", "Vol_Eu", "C_Eu", "Vol_Run", "C_Run", "Dif_Vol", "Dif_C"],tablefmt='grid',stralign='center', numalign= 'center')
        archivo.write(tabulado)
        archivo.write(f"\nSecond Euler and h={heuler2}\n")
        tabulado = tabulate(resultC1Euler2,headers=["Tiempo", "Vol_Eu", "C_Eu", "Vol_Run", "C_Run", "Dif_Vol", "Dif_C"],tablefmt='grid',stralign='center', numalign= 'center')
        archivo.write(tabulado)


        """
        archivo.write(f"\n\nC1) with tk = {tk}h\n")
        archivo.write(f"Euler and h= {heuler}\n")
        tabulado = tabulate(resultC1Euler,headers=["Tiempo", "Volumen", "C", "H"],tablefmt='grid',stralign='center', numalign= 'center')
        archivo.write(tabulado)
        print()
        print("C1 with tk = ",tk,"h")
        print("Euler and h= ",heuler)
        print(tabulado)
        archivo.write(f"\nRunge and h= {hrunge}\n")
        tabulado = tabulate(resultC1Runge,headers=["Tiempo", "Volumen", "C", "H"],tablefmt='grid',stralign='center', numalign= 'center')
        archivo.write(tabulado)
        print("Runge and h= ",hrunge)
        print(tabulado)"""




main()
