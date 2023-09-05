print("Bienvenidos a la calculadora de Python")
print("A continuación ingresa los dos numeros con los que vamos a operar")
N1 = float(input("Primer numero: "))
N2 = float(input("Segundo numero: "))

print("Bueno, ¿Qué vamos a hacer?")
sel = int(input("Ingresa el numero de la opción que elegiste\n 1: SUMA\n 2: RESTA\n 3: DIVISION\n 4: MULTIPLICACION\n"))

if sel == 1:
    res = N1 + N2
    print("El resultado es:")
    print(res)

elif sel == 2:
    res = N1 - N2
    print("El resultado es:")
    print(res)

elif sel == 3:
    res = N1 / N2
    print("El resultado es:")
    print(res)
    
elif sel == 4:
    res = N1 * N2
    print("El resultado es:")
    print(res)
    
    