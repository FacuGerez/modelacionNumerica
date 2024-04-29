import numpy as np
from .manticelist import manticereformat


def jordan(A_gauss: np.ndarray,colums:int,fils:int, mantize: int = 8) -> np.ndarray:
    result: np.ndarray = A_gauss.copy()
    row: int = 0
    # Iterate through each row in the matrix
    for i in range(colums):
        # Find the row with the maximum absolute value in the current column
        if row + 1 == fils:
            break
        if result[row][i] == 0:
            continue

        factor = 1 / result[row][i]
        result[row] *= factor
        result[row][i] = 1
        manticereformat(result[row], len(result[row]), mantize)
        for j in range(row):
            factor = result[j][i]
            result[j] -= factor * result[row]
            manticereformat(result[j], len(result[j]), mantize)
        row += 1
    return result
