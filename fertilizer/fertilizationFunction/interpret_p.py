def interpret_p(clay, P):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 41 Table 1
        
        Interpretation of soil P content extracted by the Mehlich-1
        method, according to the clay content for soybean, wheat, corn,
        and sunflower
        
        P in mg/dm^3
        
        i -> interpretation
            0 -> Very low
            1 -> Low
            2 -> Medium
            3 -> High
            4 -> Very high
    '''
    #Class I (clay 410 - 600 g/kg)
    if clay > 409 and clay < 601:
        #Very low
        if P < 4.0:
            i = 0
        #Low
        elif P < 8.0:
            i = 1
        #Medium
        elif P < 12.0:
            i = 2
        #High
        elif P < 24.0:
            i = 3
        #Very high
        else:
            i = 4
    #Class II (clay 210 - 400 g/kg)
    elif clay > 209 and clay < 401:
        #Very low
        if P < 5.0:
            i = 0
        #Low
        elif P < 10.0:
            i = 1
        #Medium
        elif P < 15.0:
            i = 2
        #High
        elif P < 30.0:
            i = 3
        #Very high
        else:
            i = 4
    
    return i