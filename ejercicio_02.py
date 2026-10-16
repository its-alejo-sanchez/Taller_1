def registrar(valores, registro):
    """
    Recibe una colección (lista o tupla) de números y un diccionario de registro.
    Retorna una nueva lista con el primer elemento incrementado en 1 y almacena
    una copia de este estado en el diccionario sin compartir referencias.
    """
    copia = list(valores) 
    copia[0] = copia[0] + 1
    registro["ultima"] = copia.copy() 
    return copia