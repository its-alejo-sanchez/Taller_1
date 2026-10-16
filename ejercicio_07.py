def leer(ruta):
    filas = []
    
    with ruta.open(encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip()
        if encabezado != "tiempo_s,posicion_m":
            raise ValueError("Encabezado incorrecto o corrupto.")
        for numero, linea in enumerate(archivo, start=2):
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue  
            campos = linea_limpia.split(",")
            if len(campos) != 2:
                raise ValueError(f"Fila {numero} rechazada: cantidad incorrecta de campos (se esperaban 2, se encontraron {len(campos)}).")
            try:
                tiempo = float(campos[0])
                posicion = float(campos[1])
            except ValueError:
                raise ValueError(f"Fila {numero} rechazada: campos no numéricos detectados.")
            filas.append((tiempo, posicion))
    if not filas:
        raise ValueError("Archivo inválido: ausencia total de mediciones.")
    return filas
