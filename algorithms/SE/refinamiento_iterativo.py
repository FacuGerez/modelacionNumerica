import numpy as np
from math import log10
from gaussjordansolution.solutionaxb import solutionaxb


def ref_iterative(A: np.ndarray, b: np.array, digitsignificative:int = 5, mantize: int = 4) -> np.array:
    if A.dtype != float:A:np.ndarray = A.astype(float)
    if b.dtype != float:b:np.array = b.astype(float)


    _,xp,_ = solutionaxb(A, b,mantize=mantize)
    R = b - np.dot(A, xp)
    _,lamdax,_ = solutionaxb(A, R,mantize=mantize)
    ka = (max(abs(lamdax))/max(abs(xp))) * (10**mantize)
    q = mantize - log10(ka)
    if q < 0:
        raise Exception("it is not possible to perform the iterative refinement with this matrix")
    counter = 1
    xp+=lamdax
    while (q*counter < digitsignificative):
        R = b - np.dot(A, xp)
        _,lamdax,_ = solutionaxb(A, R,mantize=mantize)
        xp += lamdax
        counter += 1
    return xp
    
    

# Example of use
"""
A = np.array([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 2, 3])
xp = ref_iterative(A, b,digitsignificative=8,mantize=9)
print(xp)
print(np.dot(A,xp))
print(np.dot(A,np.array([0,0,1/3])) )
"""

