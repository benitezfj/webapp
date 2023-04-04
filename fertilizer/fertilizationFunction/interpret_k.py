def interpret_k(K):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 44 Table 4
        
        Interpretation of K content in the soil extracted by the 
        Mehlich-1 method according to the K content in the soil.

        Interpretation of presence of K (mg/dm^3)
            i = 0 -> Very low
            i = 1 -> Low
            i = 2 -> Medium
            i = 3 -> High
            i = 4 -> Very high
    '''
    #Very low
    if K < 25.0:
        i = 0
    #Low
    elif K < 50.0:
        i = 1
    #Medium
    elif K < 75.0:
        i = 2
    #High
    elif K < 150:
        i = 3
    #Very high
    else:
        i = 4
    
    return i