
def fibonacci_recursivo(n):
    if n == 0:
        resultado = 0
    elif n == 1:       
        resultado = 1
    else:
        resultado = fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    return resultado
i= int(input("Hasta que posición te gustaría imprimir fibonacci"))
for n in range (i): 
    print(fibonacci_recursivo(n + 1))
print("")

def factorial_recursivo(n):
    if n == 1 or n == 0:
        resultado = 1
    else:
         resultado = n * factorial_recursivo(n-1)
    return resultado
i = int(input("Escribe el número factorial"))
for n in range (i):
    print(factorial_recursivo(n+1))
