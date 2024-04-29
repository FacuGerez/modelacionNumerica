from gauss import gauss
from jordan import jordan
import numpy as np
from manticelist import manticereformat


def solutionaxb(A: np.ndarray, b: np.array, mantize: int = 8) -> np.array:
    if len(A) != len(b) or len(A) == 0 or len(A[0]) == 0 or len(b) == 0:
        raise Exception("this not have solution")
    if A.dtype != float:
        A = A.astype(float)
    if b.dtype != float:
        b = b.astype(float)
    new_a = np.column_stack((A, b))

    gauss_result = gauss(new_a, len(new_a[0]), len(new_a), mantize)
    jordan_result = jordan(gauss_result, len(gauss_result[0]), len(gauss_result), mantize)
    xp = np.zeros(len(b))
    for i in range(len(b)):
        sum_val = sum(jordan_result[i])
        if sum_val == jordan_result[i][-1]:
            raise Exception("this not have solution")
        xp[i] = jordan_result[i][-1]
    return xp
