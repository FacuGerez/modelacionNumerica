import numpy as np
from manticelist import manticereformat

def gauss(A: np.ndarray,colums:int,fils:int,mantize:int = 8) -> np.ndarray:
    result: np.ndarray = A.copy()
    row: int = 0
    # Iterate through each row in the matrix
    for i in range(colums):
        pivot_row: int = row
        # Find the row with the maximum absolute value in the current column
        if row + 1 == fils:
            break
        for j in range(row + 1, fils):
            if abs(result[j][i]) > abs(result[pivot_row][i]):
                pivot_row = j

        if pivot_row == row and result[row][i] == 0:
            continue
        if pivot_row != row:
            result[[row, pivot_row]] = result[[pivot_row, row]] # Swap the current row with the row having the maximum absolute value
        # Perform Gaussian elimination on the matrix
        for j in range(row + 1, fils):
            factor = result[j][i] / result[row][i]
            result[j] -= factor * result[row]
            result[j][i] = 0
            manticereformat(result[j], len(result[j]), mantize)
        row += 1
    return result
