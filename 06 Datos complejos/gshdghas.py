agenda = {
    ('Argentina'): 'Buenos Aires',
    ('Brasil'): 'Sao Paulo',
    ('España'): 'Madrid'
}

nueva_agenda = {valor: clave for clave, valor in agenda.items()}

print(nueva_agenda)