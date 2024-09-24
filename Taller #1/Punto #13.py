'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:DETERMINAR EL MONTO DEL TRABAJADOR Y SU DESCUENTO:.\n")

while(True):
    salario = float(input("Dijite el salario del trabajador: "))
    if salario >= 0.1:
        seguro = salario * 4/100
        pension = salario * 5/100
        ahorro = salario * 7/100
        total = salario - (seguro + pension + ahorro)
        print(f"\nEl monto por seguro social es: ${seguro}")
        print(f"\nEl monto por pension es: ${pension}")
        print(f"\nEl monto por ahorro es: ${ahorro}")
        print(f"\nEl total a pagar es: ${total}")
        break
    else:
        print("\n\t.:EL SALARIO NO PUEDE SER NEGATIVO O IGUAL A 0:.\n")

print("\n\t.:FIN DEL PROGRAMA:.")