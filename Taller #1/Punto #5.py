'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:PROGRAMA PARA CALCULAR AREAS:.\n")
print(" 1. Area de un triangulo")
print(" 2. Area de un rombo")
print(" 3. Area de un trapecio\n")

while(True):
    opcion = int(input(" Dijite la opción a realizar: "))
    if opcion == 1:
        print("\n Formula: \n (base x altura)/2\n")
        while(True):
            base = float(input(" Dijite el largo de la base: "))
            altura = float(input(" Dijite la altura: "))
            if (base >= 0.1) and (altura >= 0.1):
                area = (base * altura) / 2
                print(f"  El area del triangulo es: {area}\n")
                break
            else:
                print("\n\t.:LA BASE Y ALTURA NO PUEDE SER 0 O NEGATIVA:.\n")
        break
    elif opcion == 2:
        print("\n Formula: \n (D x d)/2\n")
        while(True):
            lado_D = float(input(" Dijite el largo del lado D: "))
            lado_d = float(input(" Dijite el largo del lado d: "))
            if (lado_D >= 0.1) and (lado_d >= 0.1):
                area = (lado_D * lado_d) / 2
                print(f"  El area del rombo es: {area}\n")
                break
            else:
                print("\n\t.:LOS LADOS NO PUEDEN SER 0 O NEGATIVO:.\n")
        break
    elif opcion == 3:
        print("\n Formula: \n ((B + b) * h)/2\n")
        while(True):
            B = float(input(" Dijite el largo de la base mayor: "))
            b = float(input(" Dijite el largo de la base menor: "))
            h = float(input(" Dijite la altura: "))
            if (B >= 0.1) and (b >= 0.1) and (h >= 0.1):
                area = ((B + b) * h) / 2
                print(f"  El area del trapecio es: {area}\n")
                break
            else:
                print("\n\t.:LAS BASES NO PUEDEN SER 0 O NEGATIVO:.\n")
        break
    else:
        print("\n\t.:OPCION INVALIDA:.\n")

print("\t.:FIN DEL PROGRAMA:.")