def fibonacci_recursivo(n):
    if n == 0:
        resultado = 0
    elif n == 1:
        resultado = 1
    else:
        resultado = fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    return resultado
    
print(fibonacci_recursivo(8))



def factorial_recursivo(n):
    if n == 1 or n == 0:
        resultado = 1
    else:
         resultado = n * factorial_recursivo(n-1)

    return resultado

print(factorial_recursivo(4))
