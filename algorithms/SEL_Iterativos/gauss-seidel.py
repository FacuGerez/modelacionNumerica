from algorithms.SEL_Directos.gaussjordansolution.matrix_functions import seguritymatrix


def checkdiagdominant(a: list[list[float]]):
    columdominate: list[int] = []
    for fil in range(len(a)):
        maxim: float = 0
        c: int = 0
        suma: float = 0
        for col in range(len(a[fil])):
            suma += abs(a[fil][col])
            if abs(a[fil][col]) > maxim:
                maxim: float = abs(a[fil][col])
                c: int = col
        if suma - maxim > maxim or c in columdominate:
            return []
        columdominate.append(c)
    return columdominate


def gaussseidel(a: list[list[float]]):
    seguritymatrix(a)
    b: list[list[float]] = a.copy()
    columsdom: list[int] = checkdiagdominant(b)
    if len(columsdom) == 0:
        return
