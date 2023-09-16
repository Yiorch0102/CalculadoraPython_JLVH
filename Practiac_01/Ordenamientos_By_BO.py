
# Función para realizar el ordenamiento burbuja
def burbuja(bubbles):
    nbu = len(bubbles) #Función que sirve para obtener el numero de elementos de un arreglo
    flag = True
    while flag:
        flag = False
        for i in range(1, nbu): #Iteración de los elementos del arreglo desde 1 hasta el total de elementos
            if bubbles[i - 1] > bubbles[i]:
                bubbles[i - 1], bubbles[i] = bubbles[i], bubbles[i - 1]
                flag = True
        nbu -= 1
#El algoritmo de la función funciona de modo que la variable nbu (number_bubbles) se iguala al numero de variables que hay en el arreglo 
#Luego el algoritmo declara una variable booleana llamada flag como verdadera. A continuación se hace un bucle mediante un while el cual no parara mientras la variable flag siga estando declarada como verdadera
#Dentro del while esta el ciclo for que se repetira los n elementos del arreglo (Desde 1 hasta el total de elemntos). Por cada iteración se pondra un if que pregunte si el elemento de la posición actual menos 
# uno en el arreglo es mayor al elemento de la posición actual, en caso de que esta condición se cumpla, cambiara de posiciones los elementos, finalmente declarará flag como true. El ciclo continuará hasta que
#la condición if se deje de cumplir, en ese momento flag dejará de declararse como verdadera y el ciclo terminara, indicando que el ordenamiento a finalizado.

# Función para realizar el ordenamiento burbuja optimizada
def burbuja_op(bubbles):
    nbu = len(bubbles)
    for i in range(nbu):
        flag = False
        for j in range(0, nbu - i - 1):
            if bubbles[j] > bubbles[j + 1]:
                bubbles[j], bubbles[j + 1] = bubbles[j + 1], bubbles[j]
                flag = True
        if not flag:
            break
#Esta función tiene casi la misma lógica que el burbuja normal, tan solo es que este enfoque se evita hacer iteraciones innecesarias pues hace verificaciones para evitar hacer comparaciones en los arreglos que 
#ya esten casi ordenados.

# Función para ingresar el tamaño del arreglo y los datos
def arreglo_dat_tam():
    tamaño = int(input("Ingrese el tamaño del arreglo: "))
    bubbles = []
    for i in range(tamaño):
        datos = int(input(f"Ingrese el elemento {i + 1}: "))
        bubbles.append(datos)
    return bubbles
#Esta función trata de asignar un input a una variable (tamaño del arreglo), esta variable definirá la cantidad de veces que se repetira la instrucción input("Ingrese un elemento"), 
#cada elemento que se ingrese se concatenara en el arreblo bubbles con ayuda del comando .append

# Función principal
def main():
    print("Elige el tipo de ordenamiento:")
    print("1: Ordenamiento Burbuja Optimizada")
    print("2: Ordenamiento Burbuja")

    elec = int(input("Ingrese su elección (1 o 2): "))

    if elec == 1:
        bubbles = arreglo_dat_tam()
        burbuja_op(bubbles)
        print("Arreglo ordenado con ordenamiento burbuja:", bubbles)
    elif elec == 2:
        bubbles = arreglo_dat_tam()
        burbuja(bubbles)
        print("Arreglo ordenado con burbuja optimizada:", bubbles)
    else:
        print("Esa opción no existe")

#Menú de siempre, hacemos un if para un menu de opciones, en cada opción la variable bubbles toma el tamaño definido en la función del tamaño, y luego mandamos a traer a la función op o clásica dependiendo
# de la opción tomada en el menú y listo, la imprimimos.
if __name__ == "__main__":
    main()
