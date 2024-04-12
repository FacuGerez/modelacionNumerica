def gauss(a: list[list[float]], savemultiplicator: bool = False, pivot: bool = False) -> (list[list[float]], list[int]):
    if len(a) == 0:
        return a
    seguritymatrix(a)

    result: list[list[float]] = a
    changes: list[int] = list(range(len(a)))
    fil: int = len(result)
    colum: int = len(result[0])

    for f1 in range(colum):

        if f1 == fil:
            break
        if pivot:
            withpivot(result, f1, f1)
        else:
            withoutpivot(result, f1, f1)
        if result[f1][f1] == 0:
            continue

        for f2 in range(f1 + 1, fil):

            multiplicator: float = (result[f2][f1] / result[f1][f1])
            result[f2] = multiplicatorandrestlist(result[f2], result[f1], kb=multiplicator)

            if savemultiplicator:
                result[f1][f2] = multiplicator
            else:
                result[f1][f2] = 0

    return result, changes


def withpivot(lis: list[list[float]], fil: int, colum: int):
    mx: float = abs(lis[fil][colum])
    position: int = fil
    for f in range(fil, len(lis)):
        if mx < abs(lis[f][colum]):
            mx = abs(lis[f][colum])
            position = f
    lis[colum], lis[position] = lis[position], lis[colum]


def withoutpivot(lis: list[list[float]], fil: int, colum: int):
    if lis[fil][colum] == 0:
        for f in range(fil, len(lis)):
            if lis[f][colum] != 0:
                lis[f], lis[fil] = lis[fil], lis[f]
                break


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
