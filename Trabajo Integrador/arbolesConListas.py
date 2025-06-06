# Cada nodo se representa como: [valor, hijo_izquierdo, hijo_derecho]

def crear_arbol(valor):
    return [valor, [], []]

def insertar_izquierda(nodo, nuevo_valor):
    subarbol_izq = nodo[1]
    if subarbol_izq:
        nodo[1] = [nuevo_valor, subarbol_izq, []]
    else:
        nodo[1] = [nuevo_valor, [], []]

def insertar_derecha(nodo, nuevo_valor):
    subarbol_der = nodo[2]
    if subarbol_der:
        nodo[2] = [nuevo_valor, [], subarbol_der]
    else:
        nodo[2] = [nuevo_valor, [], []]

# Recorridos con impresión de nodos vacíos explícitos (None)
def preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        preorden(arbol[1])
        preorden(arbol[2])

def inorden(arbol):
    if arbol:
        inorden(arbol[1])
        print(arbol[0], end=' ')
        inorden(arbol[2])

def postorden(arbol):
    if arbol:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end=' ')

# Visualización del árbol, rotado 90° hacia la izquierda
def imprimir_arbol(arbol, nivel=0):
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)
        print(' ' * 4 * nivel + str(arbol[0]))
        imprimir_arbol(arbol[1], nivel + 1)

# -----------------------
# Ejemplo de uso
# -----------------------

# Crear árbol binario con números
arbol = crear_arbol(40)
insertar_izquierda(arbol, 10)
insertar_derecha(arbol, 9)
insertar_izquierda(arbol[1], 1)
insertar_izquierda(arbol[1][1], 20)
insertar_derecha(arbol[1], 5)
insertar_izquierda(arbol[2], 40)
insertar_derecha(arbol[2], 55)
insertar_derecha(arbol[2][2], 60)
insertar_derecha(arbol[2][2][2], 65)

# Mostrar el árbol
print("Árbol visualizado (rotado 90°):")
imprimir_arbol(arbol)

# Recorridos
print("\nRecorrido Preorden:")
preorden(arbol)

print("\nRecorrido Inorden:")
inorden(arbol)

print("\nRecorrido Postorden:")
postorden(arbol)
