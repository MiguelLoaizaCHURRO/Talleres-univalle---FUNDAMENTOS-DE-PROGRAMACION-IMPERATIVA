'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
suma = 0

for i in range(10):
    numero = float(input("Ingresa un número: "))
    suma = suma + numero

promedio = suma / 10
print(f"El promedio de los números ingresados es: {promedio}")