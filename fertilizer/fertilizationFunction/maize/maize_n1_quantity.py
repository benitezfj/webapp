def maize_n1_quantity(prev, productivity, OM):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 62 Table 16
        
        Nitrogen fertilization recommendation for Maize in SSD for 
        Paraguay.
    
        prev -> Previous crop:
            'G' - Grass (gramínea)
            'C' - Cockle (consorcio o berberecho)
            'L' - Legume (leguminosa)
        
        productivity -> Productivity expectation (kg/ha)
        OM -> Organic matter (%)
        
        N1 -> N in kg/ha
        
    '''
    if prev == 'G':
        if OM < 2:
            if productivity < 3000:
                N1 = 30
            elif productivity < 4000:
                N1 = 50
            elif productivity < 6000:
                N1 = 70
            elif productivity <= 8000:
                N1 = 90
            else:
                N1 = 110
        elif OM <= 3:
            if productivity < 3000:
                N1 = 20
            elif productivity < 4000:
                N1 = 40
            elif productivity < 6000:
                N1 = 60
            elif productivity <= 8000:
                N1 = 80
            else:
                N1 = 100
        else:
            if productivity < 3000:
                N1 = 20
            elif productivity < 4000:
                N1 = 30
            elif productivity < 6000:
                N1 = 50
            elif productivity <= 8000:
                N1 = 70
            else:
                N1 = 90
    elif prev == 'C':
        if OM < 2:
            if productivity < 3000:
                N1 = 20
            elif productivity < 4000:
                N1 = 30
            elif productivity < 6000:
                N1 = 50
            elif productivity <= 8000:
                N1 = 70
            else:
                N1 = 90
        elif OM <= 3:
            if productivity < 4000:
                N1 = 20
            elif productivity < 6000:
                N1 = 40
            elif productivity <= 8000:
                N1 = 60
            else:
                N1 = 80
        else:
            if productivity < 4000:
                N1 = 20
            elif productivity < 6000:
                N1 = 30
            elif productivity <= 8000:
                N1 = 50
            else:
                N1 = 70
    elif prev == 'L':
        if OM < 2:
            if productivity < 4000:
                N1 = 20
            elif productivity < 6000:
                N1 = 40
            elif productivity <= 8000:
                N1 = 50
            else:
                N1 = 70
        elif OM <= 3:
            if productivity < 4000:
                N1 = 20
            elif productivity < 6000:
                N1 = 40
            elif productivity <= 8000:
                N1 = 50
            else:
                N1 = 70
        else:
            if productivity < 6000:
                N1 = 20
            elif productivity <= 8000:
                N1 = 30
            else:
                N1 = 50     
    return N1