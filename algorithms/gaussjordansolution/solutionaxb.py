from gauss import gauss
from jordan import jordan


def solutionaxb(a: list[list[float]], b: list[float], mantiza: int = 8) -> (list[list[float]], list[float]):
    if len(a) == 0 or len(a[0]) == 0 or len(b) == 0:
        return []  # not have solution
    if len(a) != len(b):
        raise Exception("this not have solution")

    new_a: list[list[float]] = a.copy()
    for i in range(len(new_a)):
        new_a[i].append(b[i])

    a_gaussian_jordan: list[list[float]] = jordan(gauss(new_a,mantiza=mantiza,pivot=True)[0])
    xp: list[float] = _solutionaxb(a_gaussian_jordan)
    if _checksolution(a_gaussian_jordan):
        return a_gaussian_jordan, xp
    else:
        return a_gaussian_jordan, [float("inf")]  # not have solution


def _checksolution(a_gaussian_jordan: list[list[float]]) -> bool:
    for fil in range(len(a_gaussian_jordan)):
        filwithonlyzeros: bool = True
        for col in range(len(a_gaussian_jordan[fil]) - 1):
            if a_gaussian_jordan[fil][col] != 0:
                filwithonlyzeros: bool = False
                break
        if filwithonlyzeros:
            return False
    return True


def _solutionaxb(a_gaussian_jordan: list[list[float]]) -> list[float]:
    xp: list[float] = []
    for fil in range(len(a_gaussian_jordan)):
        xp.append(a_gaussian_jordan[fil][len(a_gaussian_jordan[0]) - 1])
        a_gaussian_jordan[fil].pop(len(a_gaussian_jordan[0]) - 1)
    return xp
