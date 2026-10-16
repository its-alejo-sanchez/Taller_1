def velocidades(intervalos, *pares, **opciones):
    escala = opciones.get("escala", 1)
    
    for clave in opciones:
        if clave != "escala":
            raise ValueError(f"Opción inválida: '{clave}'")
            
    if not pares:
        raise ValueError("Debe existir al menos un par.")
        
    if len(intervalos) != len(pares):
        raise ValueError("La cantidad de intervalos debe coincidir con la de pares.")
        
    resultado_velocidades = []
    
    for intervalo, par in zip(intervalos, pares):
        if intervalo <= 0:
            raise ValueError("Todos los intervalos deben ser positivos.")
            
        pos_inicial, pos_final = par
        velocidad = (pos_final - pos_inicial) / intervalo
        resultado_velocidades.append(velocidad * escala)
        
    return resultado_velocidades
