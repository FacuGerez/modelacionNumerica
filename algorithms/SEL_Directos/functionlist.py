def multiplicatorlist(a: list[float], k: float) -> list[float]:
    result: list[float] = list(range(len(a)))
    for i in range(len(a)):
        result[i] = a[i] * k
    return result


def restlists(a: list[float], b: list[float]) -> list[float]:
    if len(a) != len(b):
        raise Exception("its not posible to rest this if they are the same lenght")
    result: list[float] = list(range(len(a)))
    for i in range(len(a)):
        result[i] = (a[i] - b[i])
    return result