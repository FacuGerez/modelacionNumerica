def regula_falsi(a: float, b: float, f, errormin: float) -> float | None:
    """ precondition:
        * F(A) * F(B) > 0
    """
    ra: float = f(a)
    rb: float = f(b)
    half: float = (a-(b-a)*ra)/(rb-ra)

    if ra * rb > 0:  # because if ra*rb>0 === precondition isn´t true
        return None
    if (b - a)/2 < errormin or f(half) == 0:  # condition of curt
        return half
    if ra * f(half) > 0:
        return regula_falsi(half, b, f, errormin)
    elif rb * f(half) > 0:
        return regula_falsi(a, half, f, errormin)
