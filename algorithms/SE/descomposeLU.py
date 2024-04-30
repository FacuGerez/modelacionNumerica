import numpy as np
from gaussjordansolution.gauss import gauss
from typing import Tuple

def descompose(A: np.ndarray, b: np.array, mantize: int = 8) -> Tuple[np.ndarray, np.ndarray]:
    if len(A) == 0 or len(A) != len(A[0]) or len(A) != len(b):
        raise Exception("The matrix and vector do not have the same size")
    if A.dtype != float:
        A = A.astype(float)
    if b.dtype != float:
        b = b.astype(float)

    new_a = np.column_stack((A, b))
    (gauss_result,changes) = gauss(new_a, len(new_a[0]), len(new_a), mantize,LU=True)
    print(gauss_result)


descompose(np.array([[7,2,3],[7,5,4],[7,8,9]]),np.array([1,2,8]))
