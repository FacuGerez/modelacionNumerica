import math
from tabulate import tabulate
from algorithms.PVI.euler import euler, _euler_Exp
from peticionarconpadron import peticionar_const


def main():
    #-----------------------Constantes--------------------------------
    cons:dict[str,float] = peticionar_const()
    tiempo = list(cons["I"].keys()) # [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]

    #-----------------------Ecuaciones--------------------------------
    Qent = lambda C,t: C*cons["I"][t]*cons["Aterr"]
    H = lambda V: cons["Hs"] - (V/cons["Asot"]) if (cons["Hs"] - (V/cons["Asot"])) > cons["Hmin"] and (cons["Hs"] - (V/cons["Asot"])) < cons["Hmax"] else cons["Hmax"] if (cons["Hs"] - (V/cons["Asot"])) > cons["Hmax"] else cons["Hmin"]
    Qsal = lambda Qmax,V: Qmax * math.sqrt((cons["Hmax"] - H(V))/(cons["Hmax"]-cons["Hmin"]))
    V = lambda C,t,V: Qent(C,t) - Qsal(V)
    C = lambda V,C: (V/(cons["Vsot"]*cons["tk"])) * (cons["Csat"]-C)

    #-----------------------A1--------------------------------

    print()
    print("A1")
    A1 = euler(0,0,lambda t,y: Qent(1,1),h=1/60,tk=1)
    print(tabulate(A1,headers=["Tiempo", "Volumen"],tablefmt='grid',stralign='center', numalign= 'center'))

    #-----------------------A2--------------------------------

    def modelar(fV,fC,h) -> list: # Aca se modela el sistema de ecuaciones diferenciales paso a paso
        resultado = []
        i = 0
        NewV = 0
        NewC = cons["C0"]
        resultado.append([0, NewV, NewC]) # Aca se guarda el primer resultado en la lista
        while NewV >= 0 and i >= 0: #corta la iteracion cuando NewV es menor a 0 osea q se vacio
            t = h*i # Aca se calcula el tiempo desde t=0 hasta t= 0+h*i donde h avanza de a 1 minuto
            NewV = _euler_Exp(NewV, t, lambda _,y: fV(NewC,t,y), h) # Aca se hace el euler paso a paso de la ecuacion 1
            NewC = _euler_Exp(NewC, t, lambda _,y: fC(NewV,y), h) # Aca se hace el euler paso a paso de la ecuacion 6
            i+=1
            resultado.append([t+h, NewV, NewC]) # Aca se guarda el resultado de cada iteracion en la lista
        return resultado

    for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
        h = 1/60
        resultA2 = modelar(lambda C,t,newV: (Qent(C,tk)- Qsal(cons["Qmax"],newV)) if t<tk else (0 - Qsal(cons["Qmax"],newV)),
                        lambda V,newC: C(V,newC),
                        h)
        print()
        print("A2 with tk = ",tk,"h")
        print(tabulate(resultA2,headers=["Tiempo", "Volumen", "C"],tablefmt='grid',stralign='center', numalign= 'center'))

    #-----------------------B1--------------------------------
    for tk in tiempo:# [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
        h = 1/60
        NewQmax = 15.0463125 #aproximadamente
        BQsal = lambda V: Qsal(NewQmax, V)
        resultB = modelar(lambda C,t,newV: (Qent(C,tk)- BQsal(newV)) if t<tk else (0 - BQsal(newV)),
                        lambda V,newC: C(V,newC),
                        h)
        print()
        print("B1 with tk = ",tk,"h")
        print(tabulate(resultB,headers=["Tiempo", "Volumen", "C"],tablefmt='grid',stralign='center', numalign= 'center'))

    #-----------------------C1--------------------------------
    tk = tiempo[4] # 1h


main()
