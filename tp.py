import math
from algorithms.PVI.euler import euler, _euler_Exp
from peticionarconpadron import peticionar_const


def main():
    #-----------------------Constantes--------------------------------
    cons:dict[str,float] = peticionar_const()
    tiempo = list(cons["I"].keys())

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
    tk = tiempo[3]
    h = 1/60
    i = 0
    NewV = 0
    NewC = cons["C0"]
    print("i={0}/// t={1} /// V={2} /// C={3}".format(i,0,NewV,NewC))
    while NewV >= 0 and i >= 0: #corta la iteracion cuando NewV es menor a 0 osea q se vacio
        t = h*i # Aca se calcula el tiempo desde t=0 hasta t= 0+h*i donde h avanza de a 1 minuto
        NewV = _euler_Exp(NewV, t, lambda _,y: (Qent(NewC,tk)- Qsal(y)) if t<tk else (0 - Qsal(y)), h) # Aca se hace el euler paso a paso de la ecuacion 1
        NewC = _euler_Exp(NewC, t, lambda _,y: C(NewV,y), h) # Aca se hace el euler paso a paso de la ecuacion 6
        i+=1
        print("i={0} /// t={1} /// V={2} /// C={3}".format(i,t+h,NewV,NewC))

    #-----------------------B1--------------------------------
main()
