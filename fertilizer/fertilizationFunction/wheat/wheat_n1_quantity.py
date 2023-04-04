def wheat_n1_quantity(prev, OM, productivity):
    '''
        Reference: Recomendaciones de fertilización para soja, trigo,
        maíz y girasol bajo el sistema de siembra directa en el 
        Paraguay. Martín M. Cubilla A., Ademir Wendling, Fñávio L.F. 
        Eltz, Telmo J. C. Amado, João Mielniczuk. Page 58 Table 13
        
        Nitrogen fertilization recommendation for wheat in SSD
        for wheat in SSD for Paraguay.
        
        prev -> Previous crop
            - 'M' -> Maize
            - 's' -> Soy
        productivity -> Expected productivity in kg/ha
        OM -> Organic matter (%) (Sample depth 0 - 10 cm)
        
        N1 -> N in kg/ha
    '''
    
    #Previous crop: Maize
    if prev == 'M':
        if OM < 2:
            if productivity < 2000:
                N1 = 60
            elif productivity < 3001:
                N1 = 80
            else:
                N1 = 100
        elif OM < 3.1:
            if productivity < 2000:
                N1 = 40
            elif productivity < 3001:
                N1 = 60
            else:
                N1 = 80
        else:
            if productivity < 2000:
                N1 = 20
            elif productivity < 3001:
                N1 = 40
            else:
                N1 = 60
    #Previous crop: Soy
    elif prev == 'S':
        if OM < 2:
            if productivity < 2000:
                N1 = 40
            elif productivity < 3001:
                N1 = 60
            else:
                N1 = 80
        elif OM < 3.1:
            if productivity < 2000:
                N1 = 20
            elif productivity < 3001:
                N1 = 40
            else:
                N1 = 60
        else:
            if productivity < 2000:
                N1 = 0
            elif productivity < 3001:
                N1 = 20
            else:
                N1 = 40
    return N1