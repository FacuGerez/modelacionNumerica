def seguritymatrix(lis: list[list[float]]) -> None:
    c: int = len(lis[0])
    for fil in lis:
        if len(fil) != c:
            raise Exception("this not is a matrix")


def _multilists(a: list[float], b: list[float]) -> float:
    c: float = 0
    for i in range(len(a)):
        c += (a[i] * b[i])
    return c


def multi(a: list[list[float]], b: list[float]) -> list[float]:
    if len(a) == 0 or len(b) == 0:
        return []
    seguritymatrix(a)
    if len(a[0]) != len(b):
        raise Exception("this is not posible")
    c = list(range(len(b)))
    for i in range(len(a)):
        c[i] = _multilists(a[i], b)


def truncA(a: list[list[float]], mantiza=8) -> list[list[float]]:
    b: list[list[float]] = a.copy()
    for fil in range(len(b)):
        for col in range(len(b[fil])):
            b[fil][col] = round(b[fil][col], mantiza)
    return b


def truncvector(a: list[float], mantiza=8) -> list[float]:
    b: list[float] = a.copy()
    for i in range(len(b)):
        b[i] = round(b[i], mantiza)
    return b
