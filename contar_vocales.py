"""
Contar la cantidad de vocales en una frase 
"""

# Declaraciones
vocales = "aeiouAEIOU"

# Entradas
frase = input("Introduce una frase: ")

# Proceso
contador = 0
for letra in frase: 
    if letra in vocales:
        contador += 1

# Salidas
print("La frase tiene", contador, "vocales.")
