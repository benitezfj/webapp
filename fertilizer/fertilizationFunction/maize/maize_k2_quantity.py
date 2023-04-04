from fertilizer.fertilizationFunction.interpret_k import interpret_k

def maize_k2_quantity(K, n):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 54 Table 9
        
        Recommendation for corrective potassium fertilization, 
        gradual and total in kg ha-1 K2O in in kg ha-1 of K2O 
        in the SSD for Paraguay.
        
        n -> Number of crops per year (1, 2, or 3)
        K -> quantity of K (mg/dm^3)
        K2 -> K2O (kg/ha)
    '''
    
    i = interpret_k(K)
    
    #Very low presence of K
    if i == 0:
        if n ==1:
            K2 = 150
        elif n == 2:
            K2 = 250
        elif n == 3:
            K2 = 310
    #Low presence of K
    elif i == 1:
        if n == 1:
            K2 = 90
        elif n == 2:
            K2 = 150
        elif n == 3:
            K2 = 190
    #Medium presnece of K
    elif i == 2:
        M = 37.5 #Manutention 37.5
        if n == 1:
            K2 = 60
        elif n == 2:
            K2 = 60 + M
        elif n == 3:
            K2 = 60 + (2 * M)
    #High presence of K
    elif i == 3:
        M = 37.5 #Manutention 37.5
        if n == 1:
            K2 = M
        elif n == 2:
            K2 = 2 * M
        elif n == 3:
            K2 = 3 * M
    #Very high presence of K
    elif i == 4:
        R = 6 #Reposition 6
        if n ==1:
            K2 = R
        elif n == 2:
            K2 = 2 * R
        elif n == 3:
            K2 = 3 * R
    
    return K2
                
            