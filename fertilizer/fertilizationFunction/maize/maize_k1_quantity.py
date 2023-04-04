def maize_k1_quantity(K, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 63 Table 18
        
        Potassium fertilization recommendation (kg ha-1) for corn 
        suggested according to the target yield, for an average K 
        content, Paraguay 2012.
    
        K -> K in mg/dm^3
        productivity -> Productivity expectation (kg/ha)
        
        K1 -> K2O in kg/ha
        
    '''
    
    #For medium category of K in soil (51 - 75 mg/ dm^3)
    if K > 50 and K < 76:
        if productivity < 4000:
            K1 = 80
        elif K > 3999 and K < 6001:
            K1 = 90
        else:
            K1 = 100
        
    return K1