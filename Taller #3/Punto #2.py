'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
print("\n\t.:CALCULAR LOS DIVISORES DE UN NUMERO ENTERO:.\n")

n = int(input("Dijite un numero entero: "))
for divisor in range (1,n+1):
    if n % divisor == 0:
        print(divisor)
print("\t.:FIN DEL PROGRAMA:.")