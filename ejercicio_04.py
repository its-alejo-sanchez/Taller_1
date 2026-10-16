def factorial(n):
    """
    Recibe un entero no negativo n y retorna su factorial.
    Lanza ValueError si el número ingresado es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
        
    return 1 if n <= 1 else n * factorial(n - 1)

def euclides(a, b):
    """
    Recibe dos enteros no negativos a y b.
    Retorna el Máximo Común Divisor (MCD) usando el algoritmo de Euclides.
    """
    if b == 0:
        return a
    return euclides(b, a % b)
