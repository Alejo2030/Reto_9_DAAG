#1. Reto 9

import math

# Función lambda para calcular el volumen de la figura
hallar_volumen_figura = lambda r1, r2, h: (r2**2*h*math.pi)/3 + (r1*3*4*math.pi)/3

# Función lambda para calcular el área de la figura
hallar_area_de_la_figura = lambda r1, r2, h: (r1*2*4*math.pi) + (r2*math.pi)*(r2+(r2**2+h**2)**(1/2))

if __name__ == "__main__":
    # Ingresar valores 
    r1 = float(input("Ingrese el radio de la esfera que va a utilizar en centimetros: "))
    r2 = float(input("Ingrese el radio del cono que va a utilizar en centimetros: "))
    h = float(input("Ingrese la altura del cono que va a utilizar en centimetros: "))

    # Calcular el volumen y el área de la figura usando las funciones lambda
    volumen_figura =  hallar_volumen_figura(r1,r2,h)
    area_figura =   hallar_area_de_la_figura(r1,r2,h) 

    # Imprimir los resultados
    print("El volumen de la figura es " + str(volumen_figura) + " cm^3") 
    print("El area de la figura es " + str(area_figura) * " cm^2")
