def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        coincidencia = 1 if ultimo == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))