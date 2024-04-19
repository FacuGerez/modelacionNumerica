from modelacionNumerica.algorithms.SEL_Directos.functionlist import multiplicatorlist, restlists


def jordan(a_gauss: list[list[float]], mantiza: int = 8) -> list[list[float]]:
    if len(a_gauss) == 0 or len(a_gauss[0]) == 0:
        return a_gauss
    result: list[list[float]] = a_gauss.copy()
    c: int = len(a_gauss[0])
    f: int = len(a_gauss)

    for diag in range(min(f, c) - 1, -1, -1):
        columpivot: int = diag
        for col in range(diag, c):
            if result[diag][col] != 0:
                columpivot = col
                break
        if result[diag][columpivot] == 0:
            continue
        result[diag] = multiplicatorlist(result[diag], round(1 / result[diag][columpivot], mantiza), mantiza=mantiza)
        result[diag][columpivot] = 1
        for fil in range(0, diag):
            result[fil] = restlists(result[fil], multiplicatorlist(result[diag], result[fil][columpivot]))
    return result
