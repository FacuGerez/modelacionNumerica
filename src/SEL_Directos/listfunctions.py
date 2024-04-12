def multiplicatorandrestlist(a: list[float], b: list[float], ka: float = 1, kb: float = 1) -> list[float]:
    if len(a) != len(b):
        Exception("its not posible to rest this if they are the same lenght")
    c: list[float] = list(range(len(a)))
    for i in range(len(a)):
        c[i] = (ka * a[i] - kb * b[i])
    return c
def seguritymatrix(lis: list[list[float]]) -> None:
    c: int = len(lis[0])
    for fil in lis:
        if len(fil) != c:
            Exception("this not is a matrix")