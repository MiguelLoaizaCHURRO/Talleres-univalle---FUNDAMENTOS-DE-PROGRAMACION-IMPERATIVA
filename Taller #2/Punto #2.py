'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:CALCULAR SI UN AÑO ES BISIESTO :.\n")
fecha = input("Ingrese una fecha en formato AAAAMMDD: ")
año = int(fecha[0:4])

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(f"\n {año} es un año bisiesto.")
else:
    print(f"\n {año} no es un año bisiesto.")

print("\n\t.:FIN DEL PROGRAMA:.")