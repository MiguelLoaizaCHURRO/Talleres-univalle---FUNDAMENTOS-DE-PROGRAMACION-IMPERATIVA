'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:DETERMINAR DIA DE LA SEMANA CON NUMEROS:.\n")

while(True):
    dia = int(input(" Dijite un numero entre 1 y 7: "))
    if dia == 1:
        print("\nEs lunes")
        break
    elif dia ==2:
        print("\nEs martes")
        break
    elif dia ==3:
        print("\nEs miercoles")
        break
    elif dia ==4:
        print("\nEs jueves")
        break
    elif dia ==5:
        print("\nEs viernes")
        break
    elif dia ==6:
        print("\nEs sabado")
        break
    elif dia ==7:
        print("\nEs domingo")
        break
    else:
        print("\n\t.:EL NUMERO NO ESTA EN EL RANGO:.")

print("\n\t.:FIN DEL PROGRAMA:.")