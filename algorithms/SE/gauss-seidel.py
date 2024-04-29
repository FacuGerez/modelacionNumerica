import numpy as np
from math import log10
from gaussjordansolution.solutionaxb import solutionaxb


def gauss_seidel(A: np.ndarray, b: np.array) -> np.array:
    print(A)
    print()
    print(dominantdiag(A))

def dominantdiag(A: np.ndarray) -> np.ndarray:
    if len(A) != len(A[0]):
        raise Exception("The matrix is not square")
    maxs = [float('-inf') for i in range(len(A))]
    for i in range(len(A)):
        max = float('-inf')
        sum = 0
        for j in range(len(A[i])):
            sum += abs(A[i][j])
            if abs(A[i][j]) > max:
                max = abs(A[i][j])
                maxs[i] = j
        if sum - max > max or maxs.count(maxs[i]) != 1:
            raise Exception("The matrix does not have a dominant diagonal")

    for i in range(len(A)):
        if i != maxs[i]:
            A[[i,maxs[i]]] = A[[maxs[i],i]]
    return A


# Example of use
gauss_seidel(np.array([[1, 10, 4], [10, 2, 6], [2, -7, -10]]), np.array([28, 7, -17]))