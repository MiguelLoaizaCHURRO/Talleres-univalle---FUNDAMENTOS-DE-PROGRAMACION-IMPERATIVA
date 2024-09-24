'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:PROGRAMA PARA DETERMINAR EL AREA DE LA FIGURA:.\n")
while(True):
    A = float(input(" Dijite el valor de A: "))
    B = float(input(" Dijite el valor de B: "))
    C = float(input(" Dijite el valor de C: "))
    D = float(input(" Dijite el valor de D: "))
    E = float(input(" Dijite el valor de E: "))
    if (A >= 0.1) and (B >= 0.1) and (C >= 0.1) and (D >= 0.1) and (E >= 0.1):
        area = (E * D) + (((C + A) * B) / 2) + ((E * B) / 2)
        print(f"\nEl area total de la figura es: {area:.2f}\n")
        break
    else:
        print("\n\t.:LOS LADOS NO PUEDEN SER 0 NI NEGATIVOS:.\n")

print("\t.:FIN DEL PROGRAMA:.")