def secante(x: float, f, errormin: float) -> float | None:
    if f(x) == 0:
        return x
    xold: float = x
    xmed: float = xold - min((f(xold) / ((f(xold) - f(xold - 1)) / (xold - (xold - 1)))),
                             (f(xold) / ((f(xold) - f(xold + 1)) / (xold - (xold + 1)))))
    xnew: float = xmed - (f(xmed) / ((f(xmed) - f(xold)) / (xmed - xold)))
    while abs(xold - xnew) > errormin:
        if f(xmed) == 0:
            return xmed
        if f(xnew) == 0:
            return xnew
        xold: float = xmed
        xmed: float = xnew
        xnew: float = xmed - (f(xmed) / ((f(xmed) - f(xold)) / (xmed - xold)))
    return xnew
