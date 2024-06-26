def rungekuta(y0:float, t0:float, f:callable, h:float, tk:float, runge2:bool = True)->list:
    """precondición:  t0<=tk and y0 es el valor de la función en t0"""
    result:list = [(t0, y0)]
    y = y0
    iterations = int((tk-t0)/h)
    for i in range(0, iterations):
        t = t0 + h*i
        y = _runge2(y, t, f, h) if runge2 else _runge4(y, t, f, h)
        result.append((t+h,y))
    return result

def _runge4(Un:float, tn:float, f:callable, h:float)->dict:
    q1 = h*f(tn, Un)
    q2 = h*f(tn + h/2, Un + q1/2)
    q3 = h*f(tn + h/2, Un + q2/2)
    q4 = h*f(tn + h, Un + q3)
    nextUn = Un + (1/6)*(q1 + 2*q2 + 2*q3 + q4)
    return nextUn


def _runge2(Un:float, tn:float, f:callable, h:float)->dict:
    q1 = h*f(tn, Un)
    q2 = h*f(tn + h, Un + q1)
    nextUn = Un + (1/2)*(q1 + q2)
    return nextUn
