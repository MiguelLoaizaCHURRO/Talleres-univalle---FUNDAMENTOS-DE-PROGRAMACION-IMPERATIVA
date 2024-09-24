'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:EXPRESIONES A REALIZAR:.\n")
print(" 1. (100-200) / (A-5)")
print(" 2. 15-(A^2/3)")
print(" 3. a^2 + b^2 -35c")
print(" 4. 5X^2-3X+5")
print(" 5. √a + √b^3")
print(" 6. a^10 - 5")

while(True):
    opcion = int(input("\nDijite la opción a realizar: "))
    if opcion == 1:
        A = float(input("Dijite el valor de A: "))
        resul = (100 - 200) / (A - 5)
        print(f"El resultado de la operación es: {resul:.2f}\n") #aqui use aproximación de 2 decimales
        break
    elif opcion == 2:
        A = float(input("Dijite el valor de A: "))
        resul = 15 - (A ** 2 / 3)
        print(f"El resultado de la operación es: {resul:.2f}\n") #aqui use aproximación de 2 decimales
        break
    elif opcion == 3:
        a = float(input("Dijite el valor de a: "))
        b = float(input("Dijite el valor de b: "))
        c = float(input("Dijite el valor de c: "))
        resul = a ** 2 + b ** 2 - 35 * c
        print(f"El resultado de la operación es: {resul:.2f}\n") #aqui use aproximación de 2 decimales
        break
    elif opcion == 4:
        x = float(input("Dijite el valor de x: "))
        resul = 5 * (x ** 2) - 3 * x + 5
        print(f"El resultado de la operación es: {resul:.2f}\n") #aqui use aproximación de 2 decimales
        break
    elif opcion == 5:
        a = float(input("Dijite el valor de a: "))
        b = float(input("Dijite el valor de b: "))
        resul = (a ** 0.5) + ((b ** 3) ** 0.5)
        print(f"El resultado de la operación es: {resul:.2f}\n") #aqui use aproximación de 2 decimales
        break
    elif opcion == 6:
        a = float(input("Dijite el valor de a: "))
        resul = a ** 10 - 5
        print(f"El resultado de la operación es: {resul:.2f}\n") #aqui use aproximación de 2 decimales
        break
    else:
        print("\n\t.:OPCION INVALIDA:.")

print("\t.:FIN DEL PROGRAMA:.")