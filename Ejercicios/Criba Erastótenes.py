import math
import timeit
import numpy as np

def criba_eratostenes(limite):
    numeros_primos = [True] * (limite + 1)
    numeros_primos[0] = numeros_primos[1] = False
   
    for num in range(2, int(limite**0.5) + 1):
        if numeros_primos[num]:
            max_num = math.ceil((limite+1) / num)
            for multiplo in range(num,max_num):
                numeros_primos[multiplo*num] = False
   
    return [num for num in range(limite + 1) if numeros_primos[num]]

def criba_eratostenes_py(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False

    for i in range(2, int(limite ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, limite + 1, i):
                primos[j] = False

    return [i for i in range(2, limite + 1) if primos[i]]

def criba_eratostenes_np(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0:2] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = False

    return np.nonzero(sieve)[0]

# Verificamos que todas las funciones devuelvan el mismo resultado
print(all(criba_eratostenes(1000000) == criba_eratostenes_py(1000000) == criba_eratostenes_np(1000000)))

# Tiempos de ejecución
limite_superior = 1000000000
tiempo_ejecucion = timeit.timeit("criba_eratostenes(limite_superior)", globals=globals(), number=10)

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

tiempo_ejecucion = timeit.timeit("criba_eratostenes_py(limite_superior)", globals=globals(), number=10)

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

tiempo_ejecucion = timeit.timeit("criba_eratostenes_np(limite_superior)", globals=globals(), number=10)

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")