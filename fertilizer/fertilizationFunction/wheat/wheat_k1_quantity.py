def wheat_k1_quantity(K, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 60 Table 15
        
        Potassium fertilization recommendation (kg ha-1) for 
        wheat suggested according to suggested for wheat 
        according to the target yield, for an average potassium 
        content, Paraguay, 2012. average potassium content, 
        Paraguay, 2012.
        
        K -> K in mg/dm^3
        productivity -> Expected productivity in kg/ha
        
        K1 -> K2O in kg/ha
    '''
    if K > 50 and K < 76:
        if productivity < 2000:
            K1 = 70
        elif productivity < 3001:
            K1 = 90
        else:
            K1 = 100
    return K1