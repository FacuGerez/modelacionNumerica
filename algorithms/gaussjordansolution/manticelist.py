import numpy as np

def manticereformat(L: np.array,colums:int, mantiza:int):
    for i in range(colums):
        L[i] = round(L[i], mantiza)
