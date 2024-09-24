'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:DETERMINAR SI EL CENTENAR DE UN NUMERO ES PAR:.\n")

numero = int(input("Dijite un numero de 3 cifras: "))
num = numero //100

if num % 2==0:
    print(f"\n El centenar de numero {numero} ({num}) es par")
else:
    print(f"\n El centenar de numero {numero} ({num}) es impar")

print("\n\t.:FIN DEL PROGRAMA:.")