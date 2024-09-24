'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:SUMA DE NUMEROS EXECEPTUANDO NEGATIVOS:.\n")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))
suma = 0

if num1 >= 0:
    suma += num1
if num2 >= 0:
    suma += num2
if num3 >= 0:
    suma += num3
if num4 >= 0:
    suma += num4
print(f"\nLa suma de los números es: {suma}")

print("\n\t.:FIN DEL PROGRAMA:.")