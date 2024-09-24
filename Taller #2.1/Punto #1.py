'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 15/04/2023
'''

print("\n\t.:PROGRAMA PARA DETERMINAR EL SALARIO DE UN EMPLEADO CON UN CODIGO:.\n")
print("\tCODIGO = CTGVVVHEHS\n")
print(" C = Categoria (1: 10%, 2: 20%, 3: 30%")
print(" T = Turno (1: Diurno, 2: Nocturno")
print(" G = Genero (1: masculino, 2:femenino)")
print(" VVV = Valor de la hora (3 dijitos)")
print(" he = hora de entrada (Menor a la de salida) (.:FORMATO 00 HASTA LAS 23:.)")
print(" hs = hora de salida (.:FORMATO 00 HASTA LAS 23:.)")

codigo = int(input("\n\tDijite el codigo: "))

c = codigo //1000000000
aux1 = codigo % 1000000000
t = aux1 // 100000000
aux2 = codigo % 100000000
g = aux2 // 10000000
aux3 = codigo % 10000000
vvv = aux3 // 10000
aux4 = codigo % 10000
he = aux4 // 100
hs = codigo % 100

horas = hs - he
subtotal = vvv * horas
total = subtotal

if c == 1:
    categoria_pago = subtotal * 10/100
    total += categoria_pago
else:
    if c == 2:
        categoria_pago = subtotal * 20 / 100
        total += categoria_pago
    else:
        if c == 3:
            categoria_pago = subtotal * 30 / 100
            total += categoria_pago
        else:
            print("\t.:DATO NO VALIDO:.")

if g == 1:
    genero_pago = subtotal * 5/100
    total += genero_pago
else:
    if g == 2:
        genero_pago = subtotal * 10 / 100
        total += genero_pago
    else:
        print("\t.:DATO NO VALIDO:.")

if t == 1:
    turno_pago = subtotal * 10/100
    total += turno_pago
else:
    if t == 2:
        turno_pago = subtotal * 20 / 100
        total += turno_pago
    else:
        print("\t.:DATO NO VALIDO:.")
        
print(f"El total a pagar es: ${total} por {horas} horas trabajadas")