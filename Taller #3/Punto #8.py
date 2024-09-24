'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
print("\n\t.:CALCULAR UNA SECUENCIA FIBONACCI:.\n")

n =int(input("hasta que numero desea imprimir: "))
a = 0
b = 1
for i in range (1, n+1):
    c = a + b
    print(c)
    a = b
    b = c