'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
print("\n\t.:SERIES FIBONACCI:.\n")

print("\t.:SERIE 1:.")
n = int(input("Dijite el rango de la serie: "))
b = 4
c = 1
for i in range (1,n+1):
    print(c,end=", ")
    c = b
    b = b+4

print("\n\t.:SERIE 2:.")
n = int(input("Dijite el rango de la serie: "))
a = 1
aux = 3
for x in range (1,n+1):
    print(a,end=", ")
    a = a+aux
    aux = aux + 2

print("\n\t.:SERIE 3:.")
n = int(input("Dijite el rango de la serie: "))
c = 2
for i in range (1,n+1):
    print(c,end=", ")
    c = c+2

print("\n\t.:SERIE 4:.")
n = int(input("Dijite el rango de la serie: "))
cont = 1
x = 0
y = 2
z = 0
aux = 0
for i in range (1,n+1):
    z = x+y
    if cont == 1:
        aux = z * -1
    elif cont == 2:
        aux = z *-1 *-1
    print(aux,end=", ")
    x = y
    y = z
    cont = cont + 1
    if cont >= 3:
        cont = 1

print("\n\t.:FIN DEL PROGRAMA:.")