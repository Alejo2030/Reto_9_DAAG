#1. Reto 9
# Crear la función lambda que recibe la cantidad de gallinas, gallos y pollitos y devuelve la cantidad de carne de aves en kilos
calcular_cantidad_carne_aves = lambda n_gallinas, m_gallos, k_pollitos: (n_gallinas * 6) + (m_gallos * 7) + (k_pollitos * 1)

if __name__ == '__main__':
    # Pedir la cantidad de aves
    n_gallinas = int(input("Ingrese la cantidad de gallinas: "))
    m_gallos = int(input("Ingrese la cantidad de gallos: "))
    k_pollitos = int(input("Ingrese la cantidad de pollitos: "))

    # Calcular la cantidad de carne de aves utilizando la función lambda
    cantidad_carne = calcular_cantidad_carne_aves(n_gallinas, m_gallos, k_pollitos)

    # Imprimir el resultado
    print("La cantidad de carne de aves es:", cantidad_carne, "kilos.")