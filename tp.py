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
        Vn = 0
        Cn = cons["C0"]
        resultado.append([0, Vn, Cn, Vn/cons["Asot"]]) # Aca se guarda el primer resultado en la lista
        while Vn >= 0 and i >= 0: #corta la iteracion cuando Vn es menor a 0 osea q se vacio
            t = h*i # Aca se calcula el tiempo desde t=0 hasta t= 0+h*i donde h avanza de a 1 minuto
            NewV = model(Vn, t, lambda _,y: fV(Cn,t,y), h) # Aca se hace el euler paso a paso de la ecuacion 1
            NewC = model(Cn, t, lambda _,y: fC(Vn,y), h) # Aca se hace el euler paso a paso de la ecuacion 6
            Vn = NewV
            Cn = NewC
            i+=1
            resultado.append([t+h, Vn, Cn,Vn/cons["Asot"]]) # Aca se guarda el resultado de cada iteracion en la lista
        return resultado

    with open("tablas.txt", "w") as archivo: # Abre el archivo en modo escritura
        #-----------------------A1--------------------------------

        archivo.write("A1)\n")  # Escribe el contenido en el archivo
        A1 = euler(0,0,lambda t,y: Qent(1,1),h=1/60,tk=1)
        tabulado = tabulate(A1,headers=["Tiempo", "Volumen"],tablefmt='grid',stralign='center', numalign= 'center')
        archivo.write(tabulado) # Escribe el contenido en el archivo

        #-----------------------A2--------------------------------

        for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
            h = (1/60) * (tk if tk > 1 else 1)
            resultA2 = modelar(lambda Cn,t,Vn: (Qent(Cn,tk)- Qsal(cons["Qmax"],Vn)) if t<tk else (0 - Qsal(cons["Qmax"],Vn)),
                            lambda V,Cn: C(V,Cn),
                            h,
                            _euler_Exp)
            archivo.write(f"\n\nA2) with tk = {tk}h and h= {h} \n")
            tabulado = tabulate(resultA2,headers=["Tiempo", "Volumen", "C", "H"],tablefmt='grid',stralign='center', numalign= 'center')
            archivo.write(tabulado)

        #-----------------------B y C--------------------------------

        NewQmax = cons["Qmax"]
        raiz = math.sqrt((cons["Hmax"] - H(0.25*cons["Asot"]))/(cons["Hmax"]-cons["Hmin"]))
        for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
            h = 1/60 * (tk if tk > 1 else 1)
            i = 0
            Vn = 0
            Cn = cons["C0"]
            while Vn >= 0 and i >= 0: #corta la iteracion cuando Vn es menor a 0 osea q se vacio
                t = h*i # Aca se calcula el tiempo desde t=0 hasta t= 0+h*i donde h avanza de a 1 minuto
                NewV = _euler_Exp(Vn, t, lambda _,y: (Qent(Cn,tk)- Qsal(cons["Qmax"],y)) if t<tk else (0 - Qsal(cons["Qmax"],y)), h) # Aca se hace el euler paso a paso de la ecuacion 1
                NewC = _euler_Exp(Cn, t, lambda _,y: C(Vn,y), h) # Aca se hace el euler paso a paso de la ecuacion 6
                if t > 0 and t < tk:
                    Qentx = Qent(Cn,tk)
                    minus = (0.25*cons["Asot"])/ t
                    NewQmax = max(NewQmax, (Qentx-minus)/raiz)
                Vn = NewV
                Cn = NewC
                i+=1

        #-----------------------B1--------------------------------

        for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
            h = 1/60 * (tk if tk > 1 else 1)
            BQsal = lambda V: Qsal(NewQmax, V)
            resultB = modelar(lambda Cn,t,Vn: (Qent(Cn,tk)- BQsal(Vn)) if t<tk else (0 - BQsal(Vn)),
                            lambda Vn,Cn: C(Vn,Cn),
                            h,
                            _euler_Exp)

            archivo.write(f"\n\nB1) with tk = {tk}h and h= {h}\n")
            tabulado = tabulate(resultB,headers=["Tiempo", "Volumen", "C", "H"],tablefmt='grid',stralign='center', numalign= 'center')
            archivo.write(tabulado)

        #-----------------------C1--------------------------------

        tk = tiempo[4] # 1h
        hrunge = 1/60
        heuler1 = 5/60
        heuler2 = 10/60
        CQsal = lambda V: Qsal(NewQmax, V)
        resultC1Euler1 = modelar(lambda Cn,t,Vn: (Qent(Cn,tk)- CQsal(Vn)) if t<tk else (0 - CQsal(Vn)),
                            lambda Vn,Cn: C(Vn,Cn),
                            heuler1,
                            _euler_Exp)
        resultC1Euler2 = modelar(lambda Cn,t,Vn: (Qent(Cn,tk)- CQsal(Vn)) if t<tk else (0 - CQsal(Vn)),
                            lambda Vn,Cn: C(Vn,Cn),
                            heuler2,
                            _euler_Exp)
        resultC1Runge = modelar(lambda Cn,t,Vn: (Qent(Cn,tk)- CQsal(Vn)) if t<tk else (0 - CQsal(Vn)),
                            lambda Vn,Cn: C(Vn,Cn),
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




main()
