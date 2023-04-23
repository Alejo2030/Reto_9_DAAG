# 2. Reto 9

# Definir la función 'calculo_contagiados_del_covid' que recibe dos argumentos: el número de contagiados actuales (C) y los días transcurridos (D).
def calculo_contagiados_del_covid(C:int, D:int) -> int:
    # Calcular el número de contagiados por COVID-19 a partir de la fórmula dada: C*(D)**2
    numero_de_contagiados_por_covid = C*(D)**2
    # Retornar el resultado del cálculo
    return numero_de_contagiados_por_covid

# Verificar que el programa se está ejecutando como el archivo principal
if __name__ == "__main__":
    # Ingresar el número de contagiados actuales y los días transcurridos
    C= int(input("Ingrese el número de contagiados actuales: "))
    D  = int(input("Ingrese los días transcurridos: "))

    # Calcular el número de contagiados por COVID-19 utilizando la función 'calculo_contagiados_del_covid'
    CA= calculo_contagiados_del_covid(C,D)

    # Imprimir el resultado
    print("El número de contagiados después de "+ str(D)+ " días serán "+ str(CA))