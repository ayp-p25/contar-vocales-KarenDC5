"""
Contar la cantidad de vocales en una frase 
"""

# Declaraciones
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Entradas
frase = input("Introduce una frase: ")

# Proceso
contador = 0
for letra in frase: 
    if letra.lower() in vocales:
        contador += 1

# Salidas
print(f"La frase tiene {contador} vocales.")
