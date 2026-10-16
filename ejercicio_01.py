def calcular_promedio_mediciones():
    total = 0.0
    cantidad = 0

    while True:
        texto = input("Medición o fin: ")
        
        if texto == "fin":
            break
            
        try:
            valor = float(texto)
        except ValueError:
            print("Error: Entrada no numérica. Intente de nuevo.")
            continue
            
        if valor >= 0:
            total += valor
            cantidad += 1
        else:
            print("Error: Los valores negativos son rechazados.")

    if cantidad > 0:
        print(f"Promedio: {total / cantidad}")
    else:
        print("No se aceptó ninguna medición válida para calcular el promedio.")

if __name__ == "__main__":
    calcular_promedio_mediciones()
