'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 20/03/2023
'''

print("\n\t.:DETERMINAR EL COSTO DE UNA LLAMADA:.\n")

while(True):
    inicial = float(input(" Dijite el monto inicial: $"))
    final = float(input(" Dijite el monto final: $"))
    if (inicial and final >=0.1) and (inicial > final):
        costo = (inicial - final) + ((inicial - final)*20/100)
        print(f"\nEl costo total de la llamada es de: ${costo}")
        break
    else:
        print("\n\t.:DATOS INVALIDOS:.")
        print(".:Asegurese de que el monto final no sea mayor al inicial o sean numeros bajo 0:.\n")

print("\n\t.:FIN DEL PROGRAMA:.")