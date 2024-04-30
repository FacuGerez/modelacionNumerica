import numpy as np
from math import log10
from gaussjordansolution.solutionaxb import solutionaxb
from typing import Tuple


def gauss_seidel(A: np.ndarray, b: np.array, seed:np.array,corte:int) -> np.array:
    """
    Gauss-Seidel method for solving a system of linear equations (sistem A.x = b)
    :param A: matrix of NxN
    :param b: vector of N
    :param seed: vector of N
    :return: vector of N
    """
    if len(A) != len(A[0]) or len(A) != len(b) or len(A) != len(seed):
        raise Exception("The matrix and vector do not have the same size")
    if A.dtype != float:A:np.ndarray = A.astype(float)
    if b.dtype != float:b:np.array = b.astype(float)
    if seed.dtype != float:seed:np.array = seed.astype(float)

    N = len(A)
    domainmatrix,new_b = dominantdiag(A,b)
    xp = seed.copy()
    for i in range(N):
        factor = domainmatrix[i][i]
        domainmatrix[i] = (domainmatrix[i] / factor) *-1
        new_b[i] = new_b[i] / factor
        domainmatrix[i][i] = 0

    for _ in range(corte):
        for i in range(N):
            xp[i] = new_b[i] + np.dot(domainmatrix[i], xp)

    return xp



def dominantdiag(A: np.ndarray, b: np.array) -> Tuple[np.ndarray, np.array]:
    if len(A) != len(A[0]):
        raise Exception("The matrix is not square")

    maxs = list([float('-inf') for i in range(len(A))])
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

    result = np.zeros((len(A), len(A[0])))
    new_b = np.zeros(len(b))
    for i in range(len(A)):
        result[i] = A[maxs[i]]
        new_b[i] = b[maxs[i]]
    return result,new_b


# Example of use
"""
xp = gauss_seidel(np.array([[1, 10, 4], [10, 2, 6], [2, -7, -10]]), np.array([28, 7, -17]), np.array([1, 1, 0]), 8)
print(xp)
print()
print(np.dot(np.array([[1, 10, 4], [10, 2, 6], [2, -7, -10]]), xp))
"""

