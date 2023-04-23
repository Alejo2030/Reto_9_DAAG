# :+1: Reto_9_DAAG :+1:
##  :cloud: Desarrollo del reto 9, vamos allá!!! :sunny:
### Ejercicios 
## :dart: 1. Cree una función que permita calcular el Máximo Comun Divisor de dos números dados (a y b).

### CODIGO :

```ruby
#Ejercicio 1
def calcular_mcd(num1, num2):
    # Calcular el MCD utilizando el algoritmo de Euclides
    a, b = max(num1, num2), min(num1, num2)
    while b > 0:
        a, b = b, a % b
    
    # Mostrar el resultado del cálculo del MCD
    print(f"El Maximo comun divisor  de {num1} y {num2} es {a}")

# Solicitar al usuario que ingrese los números para los cuales se desea calcular el MCD
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular el MCD y mostrar el resultado
calcular_mcd(num1, num2)
```

## :dart: 2. Cree una función anónima que calcule:
###                         $$f(x) = \frac{x}{x^{1/3}-1}$$


### CODIGO:

```ruby
# Ejercicio 2
if __name__ == "__main__":
  a = int(input("Ingrese valor de X: "))
  suma = (lambda x : x / (x**(1/3)-1))(a)
  print("La funcion para cuando X vale " + str(a) + ", Y vale " + str(suma))
```


## :dart: 4.Cree una función que reciba dos números y un parametro con el cual se decida si regresa el mayor o el menor, por defecto debe regresar el mayor.

### CODIGO:


```ruby
# Ejercicio 4
def comparar_numeros():
     #Ingresar los números y el modo deseado
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    modo = input("Ingrese el modo ('mayor' o 'menor'): ").lower()
    
    # Verificar el modo ingresado y devolver el número mayor o menor según corresponda
    if modo == "mayor":
        resultado = max(num1, num2)
    elif modo == "menor":
        resultado = min(num1, num2)
    else:
        # Si se ingresa un modo no válido, lanzar una excepción
        raise ValueError("Modo no válido. Use 'mayor' o 'menor'.")
    
    # Mostrar el resultado de la función
    print(f"El {modo} número es: {resultado}")
```

## Desarrollo Reto 9

### :trumpet: 1.De los retos anteriores seleciones 3 funciones y escribalas en forma de lambdas.


### :memo: CODIGO:


```ruby
#1. Reto 9
G = 6.67384e-11 #Establecer la constante G

fuerza_gravedad_entre_dos_objetos = lambda masa1, masa2, distancia: G * (masa1 * masa2) / distancia**2 #Establecer la función Lambda

if __name__ == "__main__":
    m1 = float(input("Ingrese la masa en Kilogramos del primer objeto: ")) #Ingresar los valores 
    m2 = float(input("Ingrese la masa en Kilogramos del segundo objeto: ")) #Ingresar los valores 
    d = float(input("Ingrese la distancia en metros que los separa: ")) #Ingresar los valores 

    fuerza_gravedad = fuerza_gravedad_entre_dos_objetos(m1, m2, d) # Calcular la fuerza de gravedad entre dos objetos 

    print("La fuerza de gravedad entre los dos objetos es:", fuerza_gravedad, "Newtons") #Imprimir el resultado
```

```ruby
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

```

```ruby
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
```



### :trumpet: 2. De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args)


### :memo: CODIGO:


```ruby
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

```

```ruby
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
```

```ruby
#2. Reto 9 

# Definir la función con argumentos no definidos 
def calcular_valor_prestamo(*args) -> float:
    prestamo = args[0]
    tasa_interes = args[1]
    meses = args[2]
    interes = tasa_interes * prestamo / 100
    return prestamo + meses * interes

if __name__ == '__main__':
    prestamo = float(input("Ingrese el valor del préstamo en pesos: "))
    tasa_interes = float(input("Ingrese la tasa de interés en porcentaje: "))
    meses = int(input("Ingrese el número de meses para el préstamo: "))
    valor_prestamo = calcular_valor_prestamo(prestamo, tasa_interes, meses)
    
    # Imprimir el resultados 
    print("El valor a pagar es de: " + str(valor_prestamo))
```
### :trumpet: 3. Escriba una función recursiva para calcular la operación de la potencia.




### :memo: CODIGO:


```ruby
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
```



### :trumpet: 4.Utilice la siguiente plantilla de code para contar el tiempo: 

```ruby
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```


#### Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.


### :memo: CODIGO:


```ruby

```


### :trumpet: 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo


### Evidencias:


[![Captura-de-pantalla-2023-04-23-174153.png](https://i.postimg.cc/QdNtYwyL/Captura-de-pantalla-2023-04-23-174153.png)](https://postimg.cc/jL9tLgTv)




### :trumpet: 6.Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.


### Evidencias:



## 📁 Este es el desarrollo del reto 9 en su totalidad, espero les sirva en su camino al aprendizaje!!!
## ¡¡ Vamos Manchester City!! 1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣ Este será tu año de oro!!! :large_blue_circle: :white_circle:  :large_blue_circle: :white_circle:  :large_blue_circle:   :large_blue_circle: :white_circle: :large_blue_circle: :white_circle:
