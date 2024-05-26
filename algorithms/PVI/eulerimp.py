def euler(times:list[float], y0:float, t0:float, f:callable, h:float = None)->dict:
    """precondición: times.keys() != [] and t0<=min(times.keys()) and y0 es el valor de la función en t0"""
    result:dict = {} # (t,y)
    y = y0
    if h is None:
        sorted_times = [t0] + sorted(times)
        for t in range(0, len(sorted_times)):
            y = f(sorted_times[t], y, sorted_times[t+1]-sorted_times[t] if t < len(sorted_times)-1 else 1)
            result[t] = y
    else:
        maxt = max(times)
        iterations = int((maxt-t0)/h) + 1
        for i in range(0, iterations):
            t = t0+h*i
            y = f(t, y, h)
            if t in times:
                result[t] = y
    return result
