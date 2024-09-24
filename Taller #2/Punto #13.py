'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:DETERMINAR SEMESTRE DE UN ESTUDIANTE CON SU CODIGO:.\n")

while(True):
    codigo = int(input("Ingrese el código de estudiante: "))
    '''
    año = int(codigo_estudiante[:4])
    semestre = int(codigo_estudiante[4])
    ES UNA FORMA DE EXTRAER DATOS
    '''
    año = codigo // 10000
    semestre = (codigo % 10000) // 1000

    if semestre == 1:
        print(f" El estudiante ingresó en el primer semestre del año {año}.")
        break
    elif semestre == 2:
        print(f" El estudiante ingresó en el segundo semestre del año {año}.")
        break
    else:
        print("\n\t.:CODIGO NO VALIDO:.\n")

print("\n\t.:FIN DEL PROGRAMA:.")