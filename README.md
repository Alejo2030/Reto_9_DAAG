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

```



### :trumpet: 2. De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args)


### :memo: CODIGO:


```ruby

```


### :trumpet: 3. Escriba una función recursiva para calcular la operación de la potencia.




### :memo: CODIGO:


```ruby

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




### :trumpet: 6.Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalon. Dejar enlace en el repo.


### Evidencias:



## 📁 Este es el desarrollo del reto 9 en su totalidad, espero les sirva en su camino al aprendizaje!!!
## ¡¡ Vamos Manchester City!! 1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣ Este será tu año de oro!!! :large_blue_circle: :white_circle:  :large_blue_circle: :white_circle:  :large_blue_circle:   :large_blue_circle: :white_circle: :large_blue_circle: :white_circle:
