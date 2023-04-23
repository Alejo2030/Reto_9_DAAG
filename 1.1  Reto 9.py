#1. Reto 9
G = 6.67384e-11 #Establecer la constante G

fuerza_gravedad_entre_dos_objetos = lambda masa1, masa2, distancia: G * (masa1 * masa2) / distancia**2 #Establecer la función Lambda

if __name__ == "__main__":
    m1 = float(input("Ingrese la masa en Kilogramos del primer objeto: ")) #Ingresar los valores 
    m2 = float(input("Ingrese la masa en Kilogramos del segundo objeto: ")) #Ingresar los valores 
    d = float(input("Ingrese la distancia en metros que los separa: ")) #Ingresar los valores 

    fuerza_gravedad = fuerza_gravedad_entre_dos_objetos(m1, m2, d) # Calcular la fuerza de gravedad entre dos objetos 

    print("La fuerza de gravedad entre los dos objetos es:", fuerza_gravedad, "Newtons") #Imprimir el resultado