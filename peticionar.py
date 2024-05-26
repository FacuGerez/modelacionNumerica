def peticionar_const():
    """Pide al usuario las constantes necesarias para el programa"""
    constantes_necesarias:dict[str,float] = {}
    constantes_necesarias["A"] = float(input("Ingrese el área del terreno: "))
    constantes_necesarias["H"] = float(input("Ingrese la altura del sótano: "))
    constantes_necesarias["As"] = float(input("Ingrese el superficie del sótano, en planta: "))
    constantes_necesarias["V"] = float(input("Ingrese el volumen del sótano: "))
    constantes_necesarias["C"] = float(input("Ingrese el coeficiente de infiltración con el suelo saturado de agua: "))
    constantes_necesarias["Qmax"] = float(input("Ingrese el caudal máximo que puede extraer la bomba: "))
    constantes_necesarias["Hmax"] = float(input("Ingrese el máximo desnivel que puede extraer la bomba, entre la superficie del agua y el desagote: "))
    constantes_necesarias["Hmin"] = float(input("Ingrese el máximo desnivel que puede extraer la bomba, entre la superficie del agua y el desagote: "))
    constantes_necesarias["I"] = {1/12:241.4, #1/12 = 5min
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
    return constantes_necesarias
