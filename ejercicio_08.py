def integrar_cuadrado(a, b, n):
    # 1. Validar las restricciones de entrada al inicio
    if n <= 0 or b <= a:
        raise ValueError("intervalo o partición inválidos")
        
    ancho = (b - a) / n
    acumulado = 0.0
    
    # 2. Iterar y acumular correctamente las contribuciones de los puntos medios
    for i in range(n):
        centro = a + (i + 0.5) * ancho
        acumulado += (centro ** 2) * ancho
        
    return acumulado
