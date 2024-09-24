'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:CONVERTIR MEDICION DE TIEMPOS EN SEGUNDOS:.\n")
while(True):
    segundos = int(input("Ingrese la cantidad de segundos: "))
    if segundos >= 0.1:
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
        print(f"\n Horas = {horas} \n Minutos = {minutos} \n Segundos = {segundos}")
        break
    else:
        print("\n\t.:DATO INVALIDO:.\n")

print("\n\t.:FIN DEL PROGRAMA:.")