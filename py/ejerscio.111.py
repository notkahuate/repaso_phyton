def leernotasrecursivas(totalnotas: int, titulos: str, nota: float, totalnotas_Ac: int) :
    sumanota = nota
    if totalnotas_Ac < totalnotas:
        nota_actual = float(input(f'Ingrese la nota nro {totalnotas_Ac + 1} de {titulos}: '))
        sumanota += nota_actual
        return leernotasrecursivas(totalnotas, titulos, sumanota, totalnotas_Ac + 1)
    else:
        return sumanota

if __name__ == '__main__':
    sumaparciales = leernotasrecursivas(3, "Parciales", 0.0, 0)
    sumaquices = leernotasrecursivas(4, "Quices", 0.0, 0)
    sumatrabajos = leernotasrecursivas(2, "Trabajos", 0.0, 0)

    print(f'Nota total: {total}')

    promedio_Quices = sumaquices/4
    promedio_parciales = sumaparciales/3
    promedio_trabajos = sumatrabajos/2
    promediototal = (promedio_parciales * 0.6) +  (promedio_Quices * 0.3) + (promedio_trabajos * 0.1)

    if total >= 30:
        print("El estudiante aprobó.")
        print ( f'promedio_Quices {promedio_Quices} , promedio_parciales {promedio_parciales} ,promedio_trabajos {promedio_trabajos }')
        print(f' promedio total {promediototal}')


        
    else:
        print("El estudiante reprobó.")
        print ( f'promedio_Quices {promedio_Quices} , promedio_parciales {promedio_parciales} ,promedio_trabajos {promedio_trabajos }')
        print(f' promedio total {promediototal}')





