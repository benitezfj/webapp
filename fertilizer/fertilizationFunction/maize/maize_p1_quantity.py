def maize_p1_quantity(clay, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 63 Table 17
        
        Suggested phosphate fertilization recommendation for 
        corn based on target yields according to target yield, 
        for an average P content and clay content class, 
        Paraguay 2012. Recommendation for established SSD (over 5 years).
        for established SSD (more than 5 years).
    
        clay -> Clay tennor in g/kg
        
        productivity -> Productivity expectation (kg/ha)
        
        P1 -> P2O5 in kg/ha
    '''
    
    #Class I (410 - 600 g/kg) - 
    if clay > 409 and clay < 601: 
        if productivity < 4000:
            P1 = 60
        elif productivity > 3999 and productivity < 6001:
            P1 = 70
        else:
            P1 = 80
    #Class II (210 - 400 g/kg)
    elif clay > 209 and clay < 401:
            if productivity < 4000:
                P1 = 50
            elif productivity > 3999 and productivity < 6001:
                P1 = 60
            else:
                P1 = 70
    return P1