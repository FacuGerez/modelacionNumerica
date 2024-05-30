import math
from algorithms.PVI.euler import euler, _euler_Exp
from peticionarconpadron import peticionar_const


def main():
    #-----------------------Constantes--------------------------------
    cons:dict[str,float] = peticionar_const()
    tiempo = list(cons["I"].keys()) # [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]

    #-----------------------Ecuaciones--------------------------------
    Qent = lambda C,t: C*cons["I"][t]*cons["Aterr"]
    Qsal = lambda V: cons["Qmax"] * math.sqrt((cons["Hmax"] - (cons["Hs"]-(V/cons["Asot"])))/(cons["Hmax"]-cons["Hmin"]))
    V = lambda C,t,V: Qent(C,t) - Qsal(V)
    C = lambda V,C: (V/(cons["Vsot"]*cons["tk"])) * (cons["Csat"]-C)

    #-----------------------A1--------------------------------
    """A1 = euler(0,0,lambda t,y: Qent(1,1),1/60,1)
    print(A1[-1])
    """

    #-----------------------A2--------------------------------
    def modelar(fV,fC,tk,h):
        i = 0
        NewV = 0
        NewC = cons["C0"]
        print("i={0}/// t={1} /// V={2} /// C={3}".format(i,0,NewV,NewC))
        while NewV >= 0 and i >= 0: #corta la iteracion cuando NewV es menor a 0 osea q se vacio
            t = h*i # Aca se calcula el tiempo desde t=0 hasta t= 0+h*i donde h avanza de a 1 minuto
            NewV = _euler_Exp(NewV, t, lambda _,y: fV(NewC,tk,t,y), h) # Aca se hace el euler paso a paso de la ecuacion 1
            NewC = _euler_Exp(NewC, t, lambda _,y: fC(NewV,y), h) # Aca se hace el euler paso a paso de la ecuacion 6
            i+=1
            print("i={0} /// t={1} /// V={2} /// C={3}".format(i,t+h,NewV,NewC))

    tk = tiempo[3] # [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
    h = 1/60
    modelar(lambda C,tk,t,newV: (Qent(C,tk)- Qsal(newV)) if t<tk else (0 - Qsal(newV)),lambda V,newC: C(V,newC),tk,h)
    #modelar(fV                                                                       ,fC                      ,tk,h)

    #-----------------------B1--------------------------------
    """tk = tiempo[0] # [5min,10min,15min,30min,1h,3h,6h,12h,24h,72h]
    h = 1/60
    NewQmax = 15.0463125 #aproximadamente
    BQsal = lambda V: NewQmax * math.sqrt((cons["Hmax"] - (cons["Hs"]-(V/cons["Asot"])))/(cons["Hmax"]-cons["Hmin"]))
    modelar(lambda C,tk,t,newV: (Qent(C,tk)- BQsal(newV)) if t<tk else (0 - BQsal(newV)),lambda V,newC: C(V,newC),tk,h)
    #modelar(fV                                                                         ,fC                      ,tk,h)"""


main()
