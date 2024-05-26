import sys
from algorithms.PVI.eulerexp import euler
from peticionar import peticionar_const


def main():
    """argu = sys.argv[1:]"""
    """constantes_necesarias:dict[str,float] = peticionar_const()"""
    y0 = 1
    t0 = 0
    times = list(range(1, 13))
    h = 0.1
    f = lambda t,y: -y
    result = euler(times, y0, f, h, t0)
    print(result)

main()
