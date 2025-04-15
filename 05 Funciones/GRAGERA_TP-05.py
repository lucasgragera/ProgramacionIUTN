#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    return ("Hola Mundo!")
    
print(imprimir_hola_mundo())

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

nombre = input("Ingrese su nombre: ")

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

print(saludar_usuario(nombre))

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

def saludar_usuario(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print(saludar_usuario(nombre, apellido, edad, residencia))

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados.

radio = int(input("Ingrese el radio: "))

def calcular_area_circulo(radio):
    area = 3.14 * (radio)**2
    return (f"El area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * (3.14) * (radio)
    return (f"El perimetro del circulo es {perimetro}")

print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

segundos = int(input("Ingrese la cantidad de segundos: "))

def segundos_a_horas(segundos):
    hora = segundos / 3600
    return (f"{segundos} segundos equivalen a {hora} horas")

print(segundos_a_horas(segundos))

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

numero = int(input("Ingrese un numero: "))

def tabla_multiplicar(numero):
    resultado_de_la_tabla = ""
    for i in range(1,11):
        resultado = numero * i
        resultado_de_la_tabla += (f"{numero} X {i} = {resultado}\n")
    return resultado_de_la_tabla

print(tabla_multiplicar(numero))

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resulta-
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

def operaciones_basicas(a, b):
    suma = (a + b)
    resta = (a - b)
    if b != 0:
        division = a / b
    else:
        division = None
    multiplicacion = (a * b)
    return(f"Si a {a} y {b} los sumas da como resultado: {suma}, \n si los restas: {resta}, \n si los multiplicas: {multiplicacion} \n y si los dividis: {division}")

print(operaciones_basicas(a, b))

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

peso = float(input("Ingrese su peso(Kg): "))
altura = float(input("Ingrese su altura(m): "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return(f"Su Indice de Masa Corporal es {imc:.2f}")

print(calcular_imc(peso, altura))

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

celsius = float(input("Ingrese la temperatura en Celsius: "))

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

print(celsius_a_fahrenheit(celsius))

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return(f"El promedio de los tres numeros ingresados es: {promedio}")

print(calcular_promedio(a, b, c))