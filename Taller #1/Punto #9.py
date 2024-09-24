'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:CONVERSIONES DE MASA:.\n")
print(" 1. Convertir toneladas a kilogramos")
print(" 2. Convertir toneladas a quintales")
print(" 3. Convertir toneladas a gramos")
print(" 4. Convertir toneladas a libras")

while(True):
    opcion = int(input("\nDijite la opción a realizar: "))
    if opcion == 1:
        while(True):
            ton = float(input("\n Dijite los toneladas a convertir: "))
            if ton >= 0.1:
                kg = ton * 1 * 10 ** 4
                print(f"\nLas {ton}ton equivalen a {kg}kg")
                break
            else:
                print("\n\t.:LAS TONELADAS NO PUEDEN SER 0 O NEGATIVAS:.")
        break
    elif opcion == 2:
        while (True):
            ton = float(input("\n Dijite los toneladas a convertir: "))
            if ton >= 0.1:
                q = ton * 10
                print(f"\nLas {ton}ton equivalen a {q}q")
                break
            else:
                print("\n\t.:LAS TONELADAS NO PUEDEN SER 0 O NEGATIVAS:.")
        break
    elif opcion == 3:
        while (True):
            ton = float(input("\n Dijite los toneladas a convertir: "))
            if ton >= 0.1:
                g = ton * 1 * 10 ** 6
                print(f"\nLas {ton}ton equivalen a {g}g")
                break
            else:
                print("\n\t.:LAS TONELADAS NO PUEDEN SER 0 O NEGATIVAS:.")
        break
    elif opcion == 4:
        while (True):
            ton = float(input("\n Dijite los toneladas a convertir: "))
            if ton >= 0.1:
                lb = ton * 2204.62
                print(f"\nLas {ton}ton equivalen a {lb}lb")
                break
            else:
                print("\n\t.:LAS TONELADAS NO PUEDEN SER 0 O NEGATIVAS:.")
        break
    else:
        print("\n\t.:OPCION INVALIDA:.")

print("\n\t.:FIN DEL PROGRAMA:.")