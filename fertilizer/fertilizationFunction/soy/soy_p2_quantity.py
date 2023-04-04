from fertilizer.fertilizationFunction.interpret_p import interpret_p

def soy_p2_quantity(clay, P):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 52 Table 6
        
        Total corrective phosphate corrective fertilization 
        recommendations in kg ha-1 of P2O5, according to clay 
        content.
        
        clay -> Caly tenor (g/kg)
        P -> P in mg/dm^3
        P2 -> P2O5 in kg/ha
    '''
    i = interpret_p(clay, P)
    
    #Class I (410 - 600 g/kg)
    if clay >= 410 and clay <= 600:
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
    #Class II (210 - 400 g/kg)
    elif clay >= 210 and clay <= 400:
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
                
             
        