'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:MOSTRAR UN RESULTADO CON LA SUMA DE DOS NUMEROS:.\n")

num1 = float(input("Dijite un numero: "))
num2 = float(input("Dijite otro numero: "))
suma = num1 + num2

if suma <= -0.1:
    prom = (num1 + num2) / 2
    print(f"El promedio de los numeros es: {prom}")
else:
    if suma%2 == 0:
        print(f"El resultado de la suma de {num1} y {num2} es par ({suma})")
    else:
        print(f"El resultado de la suma de {num1} y {num2} es impar ({suma})")

print("\n\t.:FIN DEL PROGRAMA:.")