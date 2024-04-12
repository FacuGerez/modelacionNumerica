from listfunctions import multiplicatorandrestlist,seguritymatrix


def gauss(a: list[list[float]], savemultiplicator: bool = False, pivot: bool = False) -> (list[list[float]], list[int]):
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
