from algorithms.PVI.eulerexp import euler
from peticionarconpadron import peticionar_const
import ecuaciones


def main():
    cons:dict[str,float] = peticionar_const()
    tiempo = list(cons["I"].keys())
    Qent = lambda C,t: ecuaciones.ec2(C,cons["I"][t],cons["Aterr"])
    Qsal = lambda H: ecuaciones.ec3(cons["Qmax"],cons["Hmax"],cons["Hmin"],cons["Hs"],H)
    H = lambda V: ecuaciones.ec5(V,cons["Asot"])

    A1 = euler(tiempo,0,0,lambda t,_: ecuaciones.ec1(Qent(1,t),0) if t!=0 else 0)
    print(A1)
main()
