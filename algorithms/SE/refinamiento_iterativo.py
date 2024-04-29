import numpy as np
from gaussjordansolution.solutionaxb import solutionaxb
from gaussjordansolution.manticelist import manticereformat


def ref_iterative(A: np.ndarray, b: np.array):
    if A.dtype != float:
        A = A.astype(float)
    if b.dtype != float:
        b = b.astype(float)
    (jordan_result,xp,changes) = solutionaxb(A, b) # <------error in this fuction
    print(jordan_result)
    print()
    print(xp)
    print()
    print(changes)
    print()
    R = A * xp - b
    print(R)

# Example of use
A = np.array([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 2, 3])
ref_iterative(A, b)
