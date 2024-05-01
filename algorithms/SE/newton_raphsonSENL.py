import numpy as np
from solutionaxb import solutionaxb

def newton_raphsonSENL(x: np.array, f: np.ndarray[function[np.array[float]]], Jacob_invert: np.ndarray[function[np.array[float]]], iteration: int) -> float | None:
    xold: np.array = x
    xnew: np.array = xold - (np.dot(f(xold), Jacob_invert(xold)))
    for _ in range(iteration):
        xold: np.array = xnew
        xnew: np.array = xold - (np.dot(f(xold), Jacob_invert(xold)))
    return xnew


def newton_raphsonSENL2(x: np.array, f: np.ndarray[function[np.array[float]]], Jacob: np.ndarray[function[np.array[float]]], iteration: int) -> float | None:
    A = Jacob(x)
    b = f(x)*-1
    xold: np.array = x
    _,xnew,_ = solutionaxb(A,b)
    xnew = xnew + xold
    for _ in range(iteration):
        A = Jacob(xnew)
        b = f(xnew)*-1
        xold: np.array = xnew
        _,xnew,_ = solutionaxb(A,b)
        xnew = xnew + xold
    return xnew
