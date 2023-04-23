#4. Reto 9

import time  # Importamos el módulo time para medir el tiempo de ejecución

# Definimos la función para calcular Fibonacci con recursión
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# Definimos la función para calcular Fibonacci con iteración
def fibonacci_iteration(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a + b
        return b

# Pedimos al usuario que ingrese el valor de n
n = int(input("Ingrese el valor de n: "))

# Fibonacci con recursión
start_time_recursion = time.time()  # Tomamos el tiempo actual
fib_recursion = fibonacci_recursion(n)  # Calculamos Fibonacci con recursión
end_time_recursion = time.time()  # Tomamos el tiempo actual nuevamente
timer_recursion = end_time_recursion - start_time_recursion  # Calculamos la diferencia de tiempo
print("El tiempo de ejecución de Fibonacci con recursión fue de: " + str(timer_recursion) + " segundos.")

# Fibonacci con iteración
start_time_iteration = time.time()  # Tomamos el tiempo actual
fib_iteration = fibonacci_iteration(n)  # Calculamos Fibonacci con iteración
end_time_iteration = time.time()  # Tomamos el tiempo actual nuevamente
timer_iteration = end_time_iteration - start_time_iteration  # Calculamos la diferencia de tiempo
print("El tiempo de ejecución de Fibonacci con iteración fue de: " + str(timer_iteration) + " segundos.")

# Comparamos tiempos
if timer_recursion > timer_iteration:
    print("Fibonacci con iteración es más rápido que con recursión.")
else:
    print("Fibonacci con recursión es más rápido que con iteración.")