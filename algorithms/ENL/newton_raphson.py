def newton_raphson(x: float, f, fderiv, errormin: float) -> float | None:
    xold: float = x
    xnew: float = xold - (f(xold) / fderiv(xold))
    while abs(xold - xnew) > errormin:
        xold: float = xnew
        xnew: float = xold - (f(xold) / fderiv(xold))
    return xnew
