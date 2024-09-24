'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
print("\n\t.:SERIES FIBONACCI:.\n")

print("\n\t.:SERIE A:.")
n = int(input("Dijite el rango de la serie: "))
c = 1
a = 2
cont = 1
aux1 = 0
for i in range (1,n+1):
    if cont == 1:
        aux1 = c * -1 * -1
    elif cont == 2:
        aux1 = c * -1
    print(f"{aux1}/{a}",end=", ")
    c = c+2
    a = a+2
    cont = cont +1
    if cont >= 3:
        cont = 1

print("\n\t.:SERIE B:.")
n = int(input("Dijite el rango de la serie: "))
c = 1
a = 2
cont = 1
aux1 = 0
for i in range (1,n+2):
    if cont == 1:
        aux1 = c * -1 * -1
    elif cont == 2:
        aux1 = c * -1
    print(f"{aux1}/{a}!",end=", ")
    c = c+2
    a = a+2
    cont = cont +1
    if cont >= 3:
        cont = 1

print("\n\t.:SERIE C:.")
n = int(input("Dijite el rango de la serie: "))
c = 1
a = 2
cont = 1
aux1 = 0
aux2 = 2
ex = 1
for i in range (1,n+2):
    if cont == 1:
        aux1 = c * -1 * -1
    elif cont == 2:
        aux1 = c * -1
    print(f"{aux1}^{ex}/{a}",end=", ")
    ex = aux2+2
    aux2 = ex
    c = c+2
    a = a+2
    cont = cont +1
    if cont >= 3:
        cont = 1

print("\n\t.:SERIE D:.")
n = int(input("Dijite el rango de la serie: "))
c = 1
a = 5
cont = 1
aux1 = 0
for i in range (1,n+2):
    if cont == 1:
        aux1 = c * -1
    elif cont == 2:
        aux1 = c * -1 * -1
    print(f"{aux1}/{a}",end=", ")
    c = c+2
    a = a+5
    cont = cont +1
    if cont >= 3:
        cont = 1