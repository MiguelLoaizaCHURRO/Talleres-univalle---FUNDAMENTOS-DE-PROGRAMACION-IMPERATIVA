'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:PROGRAMA PARA CALCULAR IVA 16%:.\n")
tarifa = 16/100

while(True):
    dinero = float(input(" Dijite el valor: "))
    if dinero>=0.1:
        iva = dinero * tarifa
        total = dinero + iva
        print(f" El iva es de: COP${iva:.2f} y el valor más iva es de: COP${total:.2f}\n")
    else:
        print("\n\t.:VALOR INVALIDO:.\n")

print("\t.:FIN DEL PROGRAMA:.")