from gaussjordansolution.solutionaxb import solutionaxb
from algorithms.SEL_Directos.gaussjordansolution.matrix_functions import multi, truncvector
from algorithms.SEL_Directos.gaussjordansolution.functionlist import restlists
import math


def ref_iterative(a: list[list[float]], b: list[float], digitsignificative: float = 3, t: int = 8, precision: int = 2):
    matrizgaussian, xp = solutionaxb(a=a, b=b, mantiza=max(t * precision, 16))
    resid = restlists(b, multi(matrizgaussian, xp))
    resid = truncvector(resid, mantiza=t)
    _, lamdax = solutionaxb(a=matrizgaussian, b=resid, mantiza=max(t * precision, 16))
    ka = (max(lamdax) / max(xp)) * (10 ** t)  # ponele
    p = math.log10(ka)
    q = t - p
    if q > 0:
        i: int = 0
        while q * i <= digitsignificative:
            xp = xp + lamdax
            resid = restlists(b, multi(matrizgaussian, xp))
            resid = truncvector(resid, mantiza=t)
            _, lamdax = solutionaxb(a=matrizgaussian, b=resid, mantiza=max(t * precision, 16))
            i += 1

        return xp
    else:
        return []

    # truncar un float = round(65.66, 1)
