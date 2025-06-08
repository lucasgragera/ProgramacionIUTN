#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas)
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

frutas = precios_frutas.keys()
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}
contactos['Juan'] = 3525758293
contactos['Pablo'] = 74383928492
contactos['Sabri'] = 8583948238
contactos['Lucas'] = 7482948304
contactos['Martin'] = 65473920483
print(contactos["Juan"])
print(contactos["Lucas"])

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras_únicas:", palabras_unicas)
print("Recuento:", recuento)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

alumnos = {
    'Ana': (8, 9, 10),
    'Luis': (6, 7, 7),
    'Marta': (10, 9, 9)
}

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Promedio = {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {'Ana', 'Luis', 'Marta', 'Juan'}
parcial2 = {'Luis', 'Marta', 'Pedro', 'Sofía'}

ambos = parcial1.intersection(parcial2)

solo_uno = parcial1.difference(parcial2).union(parcial2.difference(parcial1))

al_menos_uno = parcial1.union(parcial2)

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

stock_productos = {'Pan': 10, 'Leche': 5, 'Huevos': 12}
print(stock_productos['Pan'])
stock_productos['Leche'] = 4
stock_productos['Mate'] = 4
print(stock_productos)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ('lunes', '09:00'): 'Reunión con equipo',
    ('martes', '11:00'): 'Clase de inglés',
    ('miércoles', '14:00'): 'Almuerzo con cliente'
}
print(agenda)

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividades programadas.")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

agenda = {
    ('Argentina'): 'Buenos Aires',
    ('Brasil'): 'Sao Paulo',
    ('España'): 'Madrid'
}

nueva_agenda = {valor: clave for clave, valor in agenda.items()}

print(nueva_agenda)