def es_primo(n):
    """
    Recibe un entero n. Devuelve False para todos los menores que 2 
    y decide la primalidad para los demás utilizando la estructura for...else.
    """
    # Filtrar de inmediato todos los números menores que 2
    if n < 2:
        return False
        
    # Evaluar los divisores para números mayores o iguales a 2
    for divisor in range(2, n):
        if n % divisor == 0:
            resultado = False
            break
    else:
        # Se ejecuta solo si el ciclo terminó sin encontrar divisores (sin break)
        resultado = True
        
    return resultado
