'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:DETERMINAR MONTO DE DESCUENTO Y TOTAL A PAGAR A UN PROFESOR:.\n")

while(True):
    horas = float(input("Ingrese la cantidad de horas trabajadas por el profesor: "))
    if horas >= 0.1:
        monto = horas * 30000
        monto_descuento = 0.05 * monto
        total = monto - monto_descuento
        print(f"\nEl monto del descuento es: ${monto_descuento}")
        print(f"El monto total a pagar es: ${total}")
        break
    else:
        print("\n\t.:DATO INVALIDO:.\n")

print("\n\t.:FIN DEL PROGRAMA:.")