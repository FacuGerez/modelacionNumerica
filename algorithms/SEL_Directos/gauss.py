from modelacionNumerica.algorithms.SEL_Directos.functionlist import multiplicatorlist, restlists


def gauss(a: list[list[float]], savemultiplicator: bool = False, pivot: bool = False) -> (list[list[float]], list[int]):
    if len(a) == 0:
        return a
    seguritymatrix(a)

    result: list[list[float]] = a.copy()
    changes: list[int] = list(range(len(a)))
    fil: int = len(result)
    colum: int = len(result[0])

    for f1 in range(colum):

        if f1 == fil:
            break
        if pivot:
            withpivot(result, f1, f1, changes)
        else:
            withoutpivot(result, f1, f1, changes)
        if result[f1][f1] == 0:
            continue

        for f2 in range(f1 + 1, fil):

            multiplicator: float = (result[f2][f1] / result[f1][f1])
            result[f2] = restlists(result[f2], multiplicatorlist(result[f1], multiplicator))

            if savemultiplicator:
                result[f2][f1] = multiplicator
            else:
                result[f2][f1] = 0

    return result, changes


def withpivot(lis: list[list[float]], fil: int, colum: int, changes: list[int]):
    mx: float = abs(lis[fil][colum])
    position: int = fil
    for f in range(fil, len(lis)):
        if mx < abs(lis[f][colum]):
            mx = abs(lis[f][colum])
            position = f
    lis[colum], lis[position] = lis[position], lis[colum]
    changes[colum], changes[position] = changes[position], changes[colum]


def withoutpivot(lis: list[list[float]], fil: int, colum: int, changes: list[int]):
    if lis[fil][colum] == 0:
        for f in range(fil, len(lis)):
            if lis[f][colum] != 0:
                lis[f], lis[fil] = lis[fil], lis[f]
                changes[f], changes[fil] = changes[fil], changes[f]
                break


def seguritymatrix(lis: list[list[float]]) -> None:
    c: int = len(lis[0])
    for fil in lis:
        if len(fil) != c:
            raise Exception("this not is a matrix")
