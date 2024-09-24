'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:INCREMENTO SALARIAL DE UN EMPLEADO:.\n")

tipo = int(input("Dijite el tipo de empleado (1, 2, 3 o 4): "))
salario = int(input("Dijite el salario del empleado: $"))

if tipo == 1 or tipo == 2:
    aumento = salario + (salario*5/100)
    print(f"\nEl salario total con el aumento es: ${aumento}")
elif tipo == 3 or tipo == 4:
    aumento = salario + (salario*12/100)
    print(f"\nEl salario total con el aumento es: ${aumento}")

print("\n\t.:FIN DEL PROGRAMA:.")