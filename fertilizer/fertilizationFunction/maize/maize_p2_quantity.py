from fertilizer.fertilizationFunction.interpret_p import interpret_p


def maize_p2_quantity(clay, P):
    """
    Reference: Recomendaciones de fertilización para soja, trigo,
    maíz y girasol bajo el sistema de siembra directa en el
    Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F.
    Eltz, Telmo J. C. Amado, João Mielniczuk. Page 52 Table 6

    Potassium fertilization recommendation (kg ha-1) for
    corn suggested according to the target yield, for an
    average K content, Paraguay 2012.

    clay -> Clay tennor in g/kg
    P -> P in

    P2 -> P2O5 in kg/ha
    """
    i = interpret_p(clay, P)

    # Class I (410 - 600 g/kg)
    if clay > 409 and clay < 601:
        if i == 0:
            P2 = 200
        elif i == 1:
            P2 = 100
        elif i == 2:
            P2 = 25
        elif i == 3:
            P2 = 0
        elif i == 4:
            i == 0
    # Class II (210 - 400 g/kg)
    elif clay > 209 and clay < 401:
        if i == 0:
            P2 == 150
        elif i == 1:
            P2 = 75
        elif i == 2:
            P2 = 15
        elif i == 3:
            P2 = 0
        elif i == 4:
            P2 = 0

    return P2
