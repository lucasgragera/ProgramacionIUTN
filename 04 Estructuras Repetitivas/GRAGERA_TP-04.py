#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0,101):
    print (i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingrese un numero: "))
contador = 1

while numero > 0:
    numero = numero // 10
    if numero > 0:
        contador += 1

print(f"El numero tiene {contador} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
contador=0

for i in range(numero1+1, numero2):
    contador=contador+i

print(f"La suma entre {numero1} y {numero2} es: {contador}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

contador=0
numero = int(input("Ingrese un numero (0 para detener)"))
while numero != 0:
    contador += numero
    numero = int(input("Ingrese un numero (0 para detener)"))

print(f"La suma de los numeros ingresados es: {contador}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero = random.randint(0,9)
contador = 1
intento = int(input("Ingrese un intento: "))
while numero != intento:
    intento = int(input("Ingrese un intento: "))
    contador += 1
    
print(f"Adivino el numero {numero}, en {contador} intentos")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range(100,0,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero: "))
contador = 0

for i in range(0,numero+1):
    contador += i

print(f"La suma de los numeros entre 0 y {numero} es: {contador}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100

positivos = 0
negativos = 0
impares = 0
pares = 0

numero = int(input("Ingrese un numero: "))

for i in range(cantidad):
    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1      
    numero = int(input("Ingrese otro numero: "))

print(f"De los {cantidad} de numeros ingresados hubieron: (positivos: {positivos}, negativos: {negativos}, pares: {pares} e impares: {impares})")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 10
contador= 0

for i in range(1, cantidad+1):
    numero = int(input(f"Ingrese el {i}° numero: "))
    contador += numero   

media =  contador / cantidad

print(f"La media de los {cantidad} numeros es: {media})")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número: "))
invertido = 0

while numero > 0:
    digito = numero % 10                 # Obtiene el último dígito
    invertido = invertido * 10 + digito  # Agrega el dígito al número invertido
    numero = numero // 10                # Elimina el último dígito

print(f"El número invertido es: {invertido}")