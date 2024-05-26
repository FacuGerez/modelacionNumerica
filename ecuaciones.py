import math


def ec1(Qent,Qsal):
    return Qent-Qsal

def ec2(C,I,Aterr):
    return C*I*Aterr

def ec3(Qmax,Hmax,Hmin,Hs,H):
    """precondicion: Hs>H siempre"""
    difH = Hs-H
    if Hs-H>Hmax or Hs-H<Hmin:
        return 0
    return Qmax * math.sqrt((Hmax - difH)/(Hmax-Hmin))

def ec5(V,Asot):
    return V/Asot

def ec6(V,Vsot,tk,Csat,C):
    return (V/(Vsot*tk)) * (Csat-C)
