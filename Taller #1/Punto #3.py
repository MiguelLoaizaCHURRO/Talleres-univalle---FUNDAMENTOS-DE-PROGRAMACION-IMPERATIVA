'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:OPCIONES A REALIZAR:.\n")
print(" 1. Convertir de dólares a pesos")
print(" 2. Convertir de pesos a dólares")
print(" 3. Convertir de grados centígrados a Farenheit")
print(" 4. Calcular el promedio de 3 números\n")
vpeso = 4816.98

while(True):
    opcion = int(input("  Dijite la opción a realizar: "))
    if opcion == 1:
        while(True):
            dolar = float(input("¿Cuantos dolares a convertir son? "))
            if dolar >= 0.1:
                conver = dolar * vpeso
                print(f"Sus USD${dolar} equivalen a COP${conver:.2f}\n")
                break
            else:
                print("\n\t.:LOS DOLARES NO PUEDEN SER 0 O NEGATIVOS:.\n")
        break
    elif opcion == 2:
        while(True):
            pesos = float(input("¿Cuantos pesos a convertir son? "))
            if pesos >= 0.1:
                conver = pesos / vpeso
                print(f"Sus COP${pesos} equivalen a USD${conver:.2f}\n")
                break
            else:
                print("\n\t.:LOS PESOS NO PUEDEN SER 0 O NEGATIVOS:.\n")
        break
    elif opcion == 3:
        grados = float(input("¿Cuantos grados °C a convertir son? "))
        f = 1.8 * grados + 32
        print(f"Sus °C {grados} equivalen a °F {f:.2f}\n")
        break
    elif opcion == 4:
        num1 = float(input("Dijite un número: "))
        num2 = float(input("Dijite un número: "))
        num3 = float(input("Dijite un número: "))
        resul = (num1 + num2 + num3)/3
        print(f"El promedio de los numeros {num1,num2,num3} es: {resul}")
        break
    else:
        print("\t.:OPCION INVALIDA:.\n")

print("\t.:FIN DEL PROGRAMA:.")