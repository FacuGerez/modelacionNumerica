def peticionar_const():
    """Pide al usuario las constantes necesarias para el programa"""
    NP = float(input("Ingrese el nro de padron: "))
    constantes_necesarias:dict[str,float] = {}
    constantes_necesarias["Aterr"] = (17.32 * (NP/3000))
    constantes_necesarias["Asot"] = 8.66 * 8.66
    constantes_necesarias["Qmax"] = 8
    constantes_necesarias["Hmax"] = 4
    constantes_necesarias["Hmin"] = 1
    constantes_necesarias["Hs"] = 3.50
    constantes_necesarias["Csat"] = 0.90
    constantes_necesarias["C0"] = 0.60
    constantes_necesarias["tk"] = (1 - NP/140000)
    constantes_necesarias["I"] = {1/12:241.4, #1/12 = 5min     Constantes q nos dan
                                  1/6:190.7, #1/6 = 10min
                                  1/4:162.6, #1/4 = 15min
                                  1/2:119.6, #1/2 = 30min
                                  1:85.0, #1 = 1h
                                  3:41.7, #3 = 3h
                                  6:26.4, #6 = 6h
                                  12:16.7, #12 = 12h
                                  24:10.9, #24 = 24h
                                  72:5.2 #72 = 72h
                                  }
    constantes_necesarias["V0"] = 0
    constantes_necesarias["Vsot"] = constantes_necesarias["Hs"] * constantes_necesarias["Asot"]
    return constantes_necesarias
