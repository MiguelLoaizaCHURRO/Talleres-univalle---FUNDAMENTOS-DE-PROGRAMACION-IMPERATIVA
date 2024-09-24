'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 1/05/2023
'''
print("\n\t.:PROGRAMA PARA LAS TABLAS DE MULTIPLICAR DEL 1 AL 9:.\n")

for i in range (1,10):
    print(f"\n\t .:TABLA DEL {i}:.\n")
    for n in range(1,11):
        result = i * n
        print(f"{i} x {n} = {result}")
print("\n\t.:FIN DEL PROGRAMA:.")