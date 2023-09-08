import matplotlib.pyplot as plt
import numpy as np

# Rango de valores de entrada (n)
n = np.linspace(1, 10, 100)

# Distintas funciones de complejidad Big O
o_1 = np.ones_like(n)
o_log_n = np.log(n)
o_n = n
o_n_log_n = n * np.log(n)
o_n_squared = n**2

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(n, o_1, label='O(1)')
plt.plot(n, o_log_n, label='O(log n)')
plt.plot(n, o_n, label='O(n)')
plt.plot(n, o_n_log_n, label='O(n log n)')
plt.plot(n, o_n_squared, label='O(n^2)')

# Configuración del gráfico
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Número de operaciones')
plt.title('Distintos Tipos de Complejidad Big O')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()


