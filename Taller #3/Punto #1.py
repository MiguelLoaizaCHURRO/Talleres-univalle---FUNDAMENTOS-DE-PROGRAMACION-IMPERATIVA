'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
print("\n\t.:CALCULAR EN UN RANGO DE NUMEROS LOS MULTIPLOS DE UN NUMERO:.\n")

x = int(input("Dijite el numero: "))
n = int(input("Dijite el rango de numeros a evaluar: "))
print(f"\n\tLos multiplos de {x} son:")

for i in range(1,n+1):
    multi = x * i
    print(f"{x} x {i} = {multi}")
print("\t.:FIN DEL PROGRAMA:.")