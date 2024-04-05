def biseccion(a: float, b: float, f, errormin: float, k: int = 1) -> float | None:
    """ precondition:
        * A < B ===> [A,B]
    and
        * (F(A)>F(B) or F(B)>F(A))
    """
    ra: float = f(a)
    rb: float = f(b)
    half: float = (a + b) / 2

    if ra * rb > 0:  # because if ra*rb>0 === precondition isn´t true
        return None
    if (b - a) / (2 ** (k + 1)) < errormin or f(half) == 0:  # condition of curt
        return half
    if ra * f(half) > 0:
        return biseccion(half, b, f, errormin, k + 1)
    elif rb * f(half) > 0:
        return biseccion(a, half, f, errormin, k + 1)
