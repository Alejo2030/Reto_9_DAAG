#3. Reto 9

def potencia(base: int, exponente: int) -> int:
    # Caso base, si el exponente es 0 entonces la potencia es 1
    if exponente == 0:
        return 1
    # Caso base, si el exponente es 1 entonces la potencia es la base
    elif exponente == 1:
        return base
    # Caso general, se llama recursivamente a la función con un exponente menor y se multiplica por la base
    else:
        return base * potencia(base, exponente - 1)

# Solicitar  la base y el exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calculamr la potencia
resultado = potencia(base, exponente)

# Imprimir el resultado
print(f"{base} elevado a la {exponente} es igual a {resultado}")
