#Actividades
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input('Ingrese su edad: '))

if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”
#.

nota = int(input('Ingrese su nota: '))
if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par"
#. Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input('Ingrese un numero par: '))

if numero % 2 == 0:
    print('Ha ingresado un numero par')
else:
    print('Por favor, ingrese un número par')    

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#Niño/a: menor de 12 años.
#Adolescente: mayor o igual que 12 años y menor que 18 años.
#Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#Adulto/a: mayor o igual que 30 años.

edad = int(input('Ingrese su edad: '))

if edad < 16:
    print('Categoria niño/a')
elif edad >= 16 and edad < 18:
    print('Categoria adolescente')
elif edad >= 18 and edad < 30:
    print('Categoria adulto/a joven')
else: 
    print('Categoria adulto/a')

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
#Nota: investigue el usode la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input('Ingrese la contraseña: ')

if 8 <= len(contraseña) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres') 

#6)Escribir un programa que tome la listanumeros_aleatorios, calcule su moda, su mediana y su media y 
#las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

moda = mode(numeros_aleatorios)
print(f'Moda: {moda}')

mediana = median(numeros_aleatorios)
print(f'Mediana: {mediana}')

media = mean(numeros_aleatorios)
print(f'Media: {media}')

if media > mediana:
    print('Sesgo positivo')
elif media < mediana:
    print('Sesgo negativo')
else:
    print('Sin sesgo')

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

texto = input('Ingrese una palabra u oracion: ')

ultima = texto[-1].lower()

if ultima == 'a' or ultima == 'e' or ultima == 'i' or ultima == 'o' or ultima == 'u':
    texto += "!"

print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. 2. 3. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input('Ingresa tu nombre: ')
opcion = int(input('Ingrese un numero: \n 1)- Nombre el mayusculas \n 2)- Nombre en minusculas \n 3)- Nombre con solo primera letra en mayuscula \n Tu opcion: '))

if opcion == 1:
    nombre = nombre.upper()
elif opcion ==2:
    nombre = nombre.lower()
else:
    nombre = nombre.title()

print(nombre)

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#Menor que 3: "Muy leve" (imperceptible).
#Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = float(input('Ingrese la magnitud del terremoto: '))

if magnitud_terremoto < 3:
    print('Muy leve')
elif magnitud_terremoto >= 3 and magnitud_terremoto <4:
    print('Leve')
elif magnitud_terremoto >= 4 and magnitud_terremoto <5:
    print('Moderado')
elif magnitud_terremoto >= 5 and magnitud_terremoto <6:
    print('Fuerte')    
elif magnitud_terremoto >= 6 and magnitud_terremoto <7:
    print('Muy Fuerte') 
elif magnitud_terremoto >= 7:
    print('Sálvese quien pueda') 

#10)-Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

from datetime import date

hemisferio = input("Ingrese el hemisferio donde se encuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

fecha = date(2025, mes, dia)

primavera = (date(2025, 3, 21), date(2025, 6, 20))
verano = (date(2025, 6, 21), date(2025, 9, 20))
otoño = (date(2025, 9, 21), date(2025, 12, 20))
invierno = (date(2025, 12, 21), date(2026, 3, 20))  # Se usa 2026 para que incluya enero y febrero

def obtener_estacion(hemisferio, fecha):
    if primavera[0] <= fecha <= primavera[1]:
        return "Primavera" if hemisferio == "N" else "Otoño"
    elif verano[0] <= fecha <= verano[1]:
        return "Verano" if hemisferio == "N" else "Invierno"
    elif otoño[0] <= fecha <= otoño[1]:
        return "Otoño" if hemisferio == "N" else "Primavera"
    else:
        return "Invierno" if hemisferio == "N" else "Verano"

if hemisferio in ["N", "S"]:
    estacion = obtener_estacion(hemisferio, fecha)
    print(f"La estación en la que te encuentras es: {estacion}")
else:
    print("Hemisferio no válido. Por favor, ingrese 'N' o 'S'.")