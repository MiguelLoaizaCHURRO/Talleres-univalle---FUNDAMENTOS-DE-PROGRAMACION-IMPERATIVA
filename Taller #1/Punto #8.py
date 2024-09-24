'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:CONVERSIONES DE LONGITUD:.\n")
print(" 1. Convertir kilometros a metros")
print(" 2. Convertir kilometros a centímetros")
print(" 3. Convertir kilometros a milímetros")
print(" 4. Convertir kilometros a pulgadas")
print(" 5. Convertir kilometros a yardas")
print(" 6. Convertir kilometros a millas")
print(" 7. Convertir kilometros a pies")

while(True):
    opcion = int(input("\nDijite la opción a realizar: "))
    if opcion == 1:
        while(True):
            km = float(input("\n Dijite los kilometros a convertir: "))
            if km >=0.1:
                m = km * 1 * 10 ** 4
                print(f"\nLos {km}km equivalen a {m}m")
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    elif opcion == 2:
        while (True):
            km = float(input("\n Dijite los kilometros a convertir: "))
            if km >= 0.1:
                cm = km * 1 * 10 ** 5
                print(f"\nLos {km}km equivalen a {cm}cm")
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    elif opcion == 3:
        while (True):
            km = float(input("\n Dijite los kilometros a convertir: "))
            if km >= 0.1:
                mm = km * 1 * 10 ** 6
                print(f"\nLos {km}km equivalen a {mm}mm")
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    elif opcion == 4:
        while (True):
            km = float(input("\n Dijite los kilometros a convertir: "))
            if km >= 0.1:
                pul = km * 39370.1
                print(f'\nLos {km}km equivalen a {pul}"')
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    elif opcion == 5:
        while (True):
            km = float(input(" Dijite los kilometros a convertir: "))
            if km >= 0.1:
                yar = km * 1093.61
                print(f"\nLos {km}km equivalen a {yar}yd")
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    elif opcion == 6:
        while (True):
            km = float(input(" Dijite los kilometros a convertir: "))
            if km >= 0.1:
                mi = km * 0.62136931818182
                print(f"\nLos {km}km equivalen a {mi}mi")
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    elif opcion == 7:
        while (True):
            km = float(input(" Dijite los kilometros a convertir: "))
            if km >= 0.1:
                pie = km * 3280.84
                print(f"\nLos {km}km equivalen a {pie}ft")
                break
            else:
                print("\n\t.:LOS KILOMETROS NO PUEDEN SER 0 O NEGATIVOS:.")
        break
    else:
        print("\n\t.:OPCION INVALIDA:.")

print("\n\t.:FIN DEL PROGRAMA:.")