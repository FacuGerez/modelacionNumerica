import numpy as np
from gaussjordansolution.gauss import gauss
from typing import Tuple

def descompose(A: np.ndarray, b: np.array, mantize: int = 8) -> Tuple[np.ndarray, np.ndarray,np.array]:
    if len(A) == 0 or len(A) != len(A[0]) or len(A) != len(b):
        raise Exception("The matrix and vector do not have the same size")
    if A.dtype != float:
        A = A.astype(float)
    if b.dtype != float:
        b = b.astype(float)

    new_a = np.column_stack((A, b))
    (gauss_result,changes) = gauss(new_a, len(new_a[0]), len(new_a), mantize,LU=True)
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    for fil in range(len(A)):
        L[fil][fil] = 1
        for col in range(fil):
            L[fil][col] = gauss_result[fil][col]
        for col in range(fil, len(A)):
            U[fil][col] = gauss_result[fil][col]

    """ P is not necessary for the descomposition of LU

    Perm = np.zeros_like(A)
    for i in range(len(changes)):
        Perm[i][changes[i]] = 1
    
    """

    return L,U,changes




descompose(np.array([[7,2,3],[7,5,4],[7,8,9]]),np.array([1,2,8]))
