'''
Universidad del valle sede Buga
Fundamentos de programación imperativa
Nombre: Miguel Angel Loaiza Villaneda
Codigo: 2357855
Fecha: 28/03/2023
'''

print("\n\t.:DESCOMPONER UN NUMERO DE 3 CIFRAS Y DARLOS EN TEXTO:.\n")

numeros = int(input("Dijite el numero: "))
num1 = numeros // 100
num2 = (numeros % 100) // 10
num3 = (numeros % 100) % 10

if num1 == 0:             #NUMERO 1
    num1 = "cero"
elif num1 == 1:
    num1 = "uno"
elif num1 == 2:
    num1 = "dos"
elif num1 == 3:
    num1 = "tres"
elif num1 == 4:
    num1 = "cuatro"
elif num1 == 5:
    num1 = "cinco"
elif num1 == 6:
    num1 = "seis"
elif num1 == 7:
    num1 = "siete"
elif num1 == 8:
    num1 = "ocho"
elif num1 == 9:
    num1 = "nueve"         #FIN NUMERO 1

if num2 == 0:              #NUMERO 2
    num2 = "cero"
elif num2 == 1:
    num2 = "uno"
elif num2 == 2:
    num2 = "dos"
elif num2 == 3:
    num2 = "tres"
elif num2 == 4:
    num2 = "cuatro"
elif num2 == 5:
    num2 = "cinco"
elif num2 == 6:
    num2 = "seis"
elif num2 == 7:
    num2 = "siete"
elif num2 == 8:
    num2 = "ocho"
elif num2 == 9:
    num2 = "nueve"        #FIN NUMERO 2

if num3 == 0:             #NUMERO 3
    num3 = "cero"
elif num3 == 1:
    num3 = "uno"
elif num3 == 2:
    num3 = "dos"
elif num3 == 3:
    num3 = "tres"
elif num3 == 4:
    num3 = "cuatro"
elif num3 == 5:
    num3 = "cinco"
elif num3 == 6:
    num3 = "seis"
elif num3 == 7:
    num3 = "siete"
elif num3 == 8:
    num3 = "ocho"
elif num3 == 9:
    num3 = "nueve"       #FIN NUMERO 3

print(f"\n{numeros} = {num1}, {num2}, {num3}.")

print("\n\t.:FIN DEL PROGRAMA:.")