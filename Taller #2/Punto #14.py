'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:DETERMINAR EL MULTIPLO DE UN NUMERO DE 4 CIFRAS:.\n")

numero = int(input("Ingrese un numero de 4 cifras: "))

if numero % 3 ==0:
    print(f"\n El numero {numero} es multiplo de 3")
elif numero % 6 ==0:
    print(f"\n El numero {numero} es multiplo de 6")
elif (numero % 3 ==0) and (numero % 6 == 0):
    print(f"\n El numero {numero} es multiplo de 3 y 6")

print("\n\t.:FIN DEL PROGRAMA:.")