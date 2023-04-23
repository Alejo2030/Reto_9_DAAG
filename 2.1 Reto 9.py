# 2. Reto 9

def d(*args: float) -> float:

    p, m, h, b = args
    total = (p * 300) + (m * 3300) + (h * 350)
    cambio = b - total
    return cambio


if __name__ == '__main__':
    # Pedir las cantidades de pan, leche y huevos, y el dinero entregado.
    p = int(input("Ingrese la cantidad de panes: "))
    m = int(input("Ingrese la cantidad de bolsas de leche: "))
    h = int(input("Ingrese la cantidad de huevos: "))
    b = float(input("Ingrese la cantidad de dinero entregada: "))

    # Calcular el cambio a entregar.
    cambio = d(p, m, h, b)

    # Imprimir el resultado.
    if cambio < 0:
        print("El dinero entregado no es suficiente para pagar la compra.")
    else:
        print("El cambio a entregar es de: $" + str(cambio))