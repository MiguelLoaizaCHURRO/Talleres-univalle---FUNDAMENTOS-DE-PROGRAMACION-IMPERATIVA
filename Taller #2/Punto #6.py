'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:OBTENCION DE DATOS DE UNA PERSONA:.\n")

name = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (hombre o mujer): ").lower()
estado = input("Ingrese su estado civil: ").lower()

if (sexo == "hombre" and estado == "casado" and edad > 40) or (sexo == "mujer" and estado == "soltera" and edad == 50):
    print(f"Su nombre es: {name}")

print("\n\t.:FIN DEL PROGRAMA:.")