'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:CALCULAR PROMEDIO DE NOTAS PARA UNA BECA DE DOS ALUMNOS:.\n")
print(" Asignaturas a evaluar: Matematicas, ingles, quimica, fisica.")

print("\n\t.:NOTAS DEL ALUMNO 1:.")
mate = float(input("Nota final de matematicas: "))
ingles = float(input("Nota final de ingles: "))
quim = float(input("Nota final de quimica: "))
fisi = float(input("Nota final de fisica: "))

lista = [mate, ingles, quim, fisi]
prom = (mate + ingles + quim + fisi) / 4
print(f"\nEl promedio de notas del alumno 1 es: {prom}")

if prom > 4.5:
    print(" El estudiante puede aspirar a una beca")
else:
    print(" El estudiante no puede aspirar a una beca")

print("\n\t.:NOTAS DEL ALUMNO 2:.")
mate2 = float(input("Nota final de matematicas: "))
ingles2 = float(input("Nota final de ingles: "))
quim2 = float(input("Nota final de quimica: "))
fisi2 = float(input("Nota final de fisica: "))

lista = [mate2, ingles2, quim2, fisi2]
prom2 = (mate2 + ingles2 + quim2 + fisi2) / 4
print(f"\nEl promedio de notas del alumno 2 es: {prom2}")

if prom2 > 4.5:
    print(" El estudiante puede aspirar a una beca")
else:
    print(" El estudiante no puede aspirar a una beca")

print("\t.:FIN DEL PROGRAMA:.")