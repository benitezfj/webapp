def soy_p1_quantity(clay, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 57 Table 11
        
        Phosphate fertilization recommendation (kg ha-1) for 
        soybeans suggested according to the target yield, for an 
        average P content and clay content class, P and clay 
        content class, Paraguay, 2012 - Recommendation for established SSD (over 5 years).
        for established SSD (over 5 years).
        
        clay -> Caly tenor (g/kg)
        productivity -> Productivity in kg/ha
        P1 -> P2O5 in kg/ha
    '''
    
    #Class I (410 - 600 g/kg)
    if clay > 409 and clay < 601: 
        if productivity < 2000:
            P1 = 40 
        elif productivity > 1999 and productivity < 3001:
            P1 = 70
        else:
            P1 = 90
    #Class II (1210 -400 g/kg)
    elif clay > 209 and clay < 401:
            if productivity < 2000:
                P1 = 30
            elif productivity > 1999 and productivity < 3001:
                P1 = 60
            else:
                P1 = 80
    return P1