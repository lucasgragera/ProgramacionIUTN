#Actividades
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print('Hola Mundo!')

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre2=input('Ingrese su nombre:')

saludo=(f'Hola {nombre2}!')
print(saludo)

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre3=input('Ingrese su nombre:')
apellido3=input('Ingrese su apellido:')
edad3=input('Ingrese su edad:')
pais3=input('Ingrese su pais:')

mensaje=(f'Soy {nombre3} {apellido3}, tengo {edad3} años y vivo en {pais3}')
print(mensaje)

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro
radio=input('Ingrese el radio:')
radio=float(radio)
pi=3.1415

area=pi*radio*radio
perimetro=pi*(radio*2)

print(f'El perimetro es: {perimetro} y el area es: {area}')

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos=input('Ingrese los segundos deseados:')
segundos=int(segundos)

horas=segundos/3600

print(f'{segundos} segundos, son {horas} horas')

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero=input('Ingrese un numero del que quiera ver la tabla')
numero=int(numero)

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1=int(input('Ingrese un numero distinto de cero: '))
numero2=int(input('Ingrese un numero distinto de cero: '))

suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2

print(f'Ambos numeros al sumarlos da como resultado: {suma}, al restarlos: {resta}, al multiplicarlos: {multiplicacion} y al dividirlos {division}')

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2
peso=float(input('Ingrese su peso en kg: '))
altura=float(input('Ingrese su altura en metros: '))

imc=peso/(altura)**2

print(f'Su IMC es: {imc}')

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius=float(input('Ingrese una tempreratura en grados Celsius C: '))

fahrenheit=(9/5)*celsius+32

print(f'{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit')

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
primerNumero=int(input('Ingrese un numero entero: '))
segundoNumero=int(input('Ingrese un numero entero: '))
tercerNumero=int(input('Ingrese un numero entero: '))

promedio=(primerNumero+segundoNumero+tercerNumero)/3

print(f'El promedio de {primerNumero}, {segundoNumero} y {tercerNumero} es: {promedio}')