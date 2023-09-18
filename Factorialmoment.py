def fibonacci():
    # Programa para hacer la secuencia de fibonacci
    nterms = int(input("¿Cuántos términos?"))

    # Primeros dos términos
    n1, n2 = 0, 1
    cuenta = 0

# Chequeo para saber si los números ingresados son correctos
    if nterms <= 0:
        print("Ingresa una cantidad positiva")
        print("Ingresa un numero positivo")
    # Si solo hay un término muestra esto
    elif nterms == 1:
     print("Aqui tienes la sencuenta hasta 1,")
     print(n1)
    # Secuencia
    else:
        print("Aqui tienes tu secuencia de fibonacci:")
        while cuenta < nterms:
            print(n1)
            nf = n1 + n2
            n1 = n2
            n2 = nf
            cuenta += 1
def factorial():