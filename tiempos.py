import time
import matplotlib.pyplot as plt

# Fibonacci Iterativo
def fibonacci_iterativo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        n1, n2 = 0, 1
        for i in range(2, n + 1):
            pos = n1 + n2
            n1, n2 = n2, pos
        return pos

# Fibonacci Recursivo
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fibonacci Dinámico
def fibonacci_dinamico(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    if n > 0:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Cambio de Monedas Voraz
def cambio_moneda(monedas, cantidad):
    monedas.sort(reverse=True)
    cambio = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            cambio.append(moneda)
    return cambio

# Cambio de Monedas Dinámico
def cambio_moneda_dinamica(monedas, cantidad):
    mon = [float('inf')] * (cantidad + 1)
    mon[0] = 0
    for i in range(1, cantidad + 1):
        for moneda in monedas:
            if i - moneda >= 0:
                mon[i] = min(mon[i], mon[i - moneda] + 1)
    cambio = []
    i = cantidad
    while i > 0 and mon[i] != float('inf'):
        for moneda in monedas:
            if i - moneda >= 0 and mon[i] == mon[i - moneda] + 1:
                cambio.append(moneda)
                i -= moneda
                break
    return cambio

# Mochila Binaria Dinámica
def mochila_binaria(valores, pesos, capacidad):
    n = len(valores)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidad]

# Ejemplo de uso y medición de tiempos
n_fibonacci = 30
n_cambio_moneda = 500
n_mochila_binaria = 100

# Fibonacci Iterativo
start_time = time.time()
fibonacci_iterativo_result = fibonacci_iterativo(n_fibonacci)
elapsed_time = time.time() - start_time
print(f"Fibonacci Iterativo: Resultado = {fibonacci_iterativo_result}, Tiempo = {elapsed_time:.6f} segundos")

# Fibonacci Recursivo
start_time = time.time()
fibonacci_recursivo_result = fibonacci_recursivo(n_fibonacci)
elapsed_time = time.time() - start_time
print(f"Fibonacci Recursivo: Resultado = {fibonacci_recursivo_result}, Tiempo = {elapsed_time:.6f} segundos")

# Fibonacci Dinámico
start_time = time.time()
fibonacci_dinamico_result = fibonacci_dinamico(n_fibonacci)
elapsed_time = time.time() - start_time
print(f"Fibonacci Dinámico: Resultado = {fibonacci_dinamico_result}, Tiempo = {elapsed_time:.6f} segundos")

# Cambio de Monedas Voraz
monedas_disponibles = [500, 200, 100, 50, 20, 10, 5, 2, 1]
cantidad_a_cambiar = n_cambio_moneda
start_time = time.time()
cambio_moneda_voraz_result = cambio_moneda(monedas_disponibles, cantidad_a_cambiar)
elapsed_time = time.time() - start_time
print(f"Cambio de Monedas Voraz: Resultado = {cambio_moneda_voraz_result}, Tiempo = {elapsed_time:.6f} segundos")

# Cambio de Monedas Dinámico
start_time = time.time()
cambio_moneda_dinamica_result = cambio_moneda_dinamica(monedas_disponibles, cantidad_a_cambiar)
elapsed_time = time.time() - start_time
print(f"Cambio de Monedas Dinámico: Resultado = {cambio_moneda_dinamica_result}, Tiempo = {elapsed_time:.6f} segundos")

# Mochila Binaria Dinámica
valores_mochila = [20, 50, 80]
pesos_mochila = [10, 20, 30]
capacidad_mochila = n_mochila_binaria
start_time = time.time()
mochila_binaria_result = mochila_binaria(valores_mochila, pesos_mochila, capacidad_mochila)
elapsed_time = time.time() - start_time
print(f"Mochila Binaria Dinámica: Resultado = {mochila_binaria_result}, Tiempo = {elapsed_time:.6f} segundos")

# Creación de gráficos
n_values = list(range(1, 31))
fibonacci_iterativo_times = []
fibonacci_recursivo_times = []
fibonacci_dinamico_times = []

for n in n_values:
    start_time = time.time()
    fibonacci_iterativo(n)
    elapsed_time = time.time() - start_time
    fibonacci_iterativo_times.append(elapsed_time)

    start_time = time.time()
    fibonacci_recursivo(n)
    elapsed_time = time.time() - start_time
    fibonacci_recursivo_times.append(elapsed_time)

    start_time = time.time()
    fibonacci_dinamico(n)
    elapsed_time = time.time() - start_time
    fibonacci_dinamico_times.append(elapsed_time)

plt.figure(figsize=(10, 6))
plt.plot(n_values, fibonacci_iterativo_times, label='Fibonacci Iterativo')
plt.plot(n_values, fibonacci_recursivo_times, label='Fibonacci Recursivo')
plt.plot(n_values, fibonacci_dinamico_times, label='Fibonacci Dinámico')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución para Fibonacci')
plt.legend()
plt.show()
