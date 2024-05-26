def euler(times:list[float], y0:float, f:callable[float,float,float], h:float = None, t0:float = 0)->dict:
    """precondición: times.keys() != [] and t0<=min(times.keys()) and y0 es el valor de la función en t0"""
    result:dict = {}
    y = y0
    if h is None:
        sorted_times = [t0] + sorted(times)
        for t in range(0, len(sorted_times)):
            y += f(sorted_times[t], y, sorted_times[t+1]-sorted_times[t] if t < len(sorted_times)-1 else 1)
            result[t] = y
    else:
        maxt = max(times)
        for t in range(t0, maxt, h):
            y += f(t, y, h)
            if t in times:
                result[t] = y
    return result
