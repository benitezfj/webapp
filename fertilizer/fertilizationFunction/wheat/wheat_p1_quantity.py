def wheat_p1_quantity(clay, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 59 Table 14
        
        Phosphate fertilization recommendation (kg ha-1) for 
        wheat suggested according to target yield, for an 
        average P content and clay content class, Paraguay 2012.
        P and clay content class, Paraguay 2012. Recommendation
        for established SSD (more than 5 years).
        
        clay -> Caly tenor in g/kg
        productivity -> Expected productivity in kg/ha
        
        P1 -> P2O5 in kg/ha
    '''
    
    #Class I (410 - 600 g/kg)
    if clay > 409 and clay < 601:
        if productivity < 2000:
            P1 = 60
        elif productivity < 3001:
            P1 = 70
        else:
            P1 = 80
    #Class II (210 - 400 g/kg)
    elif clay > 209 and clay < 401:
        if productivity < 2000:
            P1 = 50
        elif productivity < 3001:
            P1 = 60
        else:
            P1 = 70
    return P1