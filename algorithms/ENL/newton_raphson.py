def newton_raphson(x: float, f: function[float], fderiv: function[float], errormin: float) -> float | None:
    xold: float = x
    xnew: float = xold - (f(xold) / fderiv(xold))
    while xold - xnew > errormin:
        xold: float = xnew
        xnew: float = xold - (f(xold) / fderiv(xold))
    return xnew
