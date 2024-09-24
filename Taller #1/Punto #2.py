'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:PROGRAMA PARA CALCULAR EL AREA DE UN TRIANGULO:.\n")
print("  Formula: \narea = √p(p-a)(p-b)(p-c)\n")

while(True):
    a = float(input(" Dijite la longitud del lado a: "))
    b = float(input(" Dijite la longitud del lado b: "))
    c = float(input(" Dijite la longitud del lado c: "))
    if (a >= 0.1) and (b >= 0.1) and (c >= 0.1):
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"El area del triangulo es: {area:.2f}\n")  # aqui use aproximacion de 2 decimales
        break
    else:
        print("\n\t.:LAS LONGITUDES NO PUEDEN SER NEGATIVAS:.\n")

print("\t.:FIN DEL PROGRAMA:.")