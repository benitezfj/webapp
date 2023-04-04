def soy_k1_quantity(K, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 57 Table 11
        
        Potassium fertilization recommendation (kg ha-1) for soybean
        suggested according to target yield, for an average 
        potassium content, Paraguay, 2012.
        
        K -> K in mg/dm^3
        productivity -> Productivity in kg/ha
        K1 -> K2O in kg/ha
    '''
    
    #For medium category of K in soil (51 - 75 mg/ dm^3)
    #Create validation for K =< 50 
    if K > 50 and K < 76:
        if productivity < 2000:
            K1 = 70
        # Productivity?
        elif K > 1999 and K < 3001:
            K1 = 90
        else:
            K1 = 100
        
    return K1
    