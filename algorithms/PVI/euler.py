def euler(y0:float, t0:float, f:callable, h:float, tk:float, exp:bool = True)->list:
    """precondición:  t0<=tk and y0 es el valor de la función en t0"""
    result:list = [(t0, y0)]
    y = y0
    iterations = int((tk-t0)/h)
    for i in range(0, iterations):
        t = t0 + h*i
        y = _euler_Exp(y, t, f, h) if exp else _euler_Imp(y, t, f, h)
        result.append((t+h,y))
    return result

def _euler_Exp(Un:float, tn:float, f:callable, h:float)->dict:
    nextUn = Un + f(tn, Un)*h
    return nextUn

def _euler_Imp(Un:float, tn:float, f:callable, h:float)->dict:
    nextUn = f(tn, Un, h)
    return nextUn
