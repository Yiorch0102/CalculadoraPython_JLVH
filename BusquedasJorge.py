# Función de búsqueda lineal
def busqueda_lineal(arr, elemento):
    for i in range(len(arr)):
        if arr[i] == elemento:
            return i    #Vuelta al indice
    return -1 #Elemento no encontrado

# Función de búsqueda binaria
def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio  # Elemento encontrado, nos devolvemos el índice
        elif lista[medio] < elemento:
            izquierda = medio + 1  # Se sabe que el dato esta a la derecha
        else:
            derecha = medio - 1  # Se sabe que el dato esta a la izquierda
    
    return -1  # Eso pasa cuando el elemento no se encontro

# Función principal del programa
def main():
    try:
        tamano = int(input("Ingrese el tamaño del arreglo: ")) #Escaneo del tamaño del arreglo en la variable tamaño
        if tamano <= 0:                                          #Condional que verifica si el esta compuesto por numeros enteros positivos, de lo contrario reinicia el programa
            print("El tamaño del arreglo debe ser un número positivo XD.")
            return
        
        arreglo = []
        for i in range(tamano): #Definición el tamaño del arreglo en base al rango del entero guardado
            valor = int(input(f"Ingrese el elemento {i + 1}: "))#Inserción del elemento a buscar
            arreglo.append(valor)
        
        elemento_buscar = int(input("Ingrese el elemento que desea buscar mi estimado: "))
        elec = int(input("¿Qué metodo de busqueda prefieres, 1-busqueda lineal o 2-busqueda binaria? "))
        if elec == 1:
            indice = busqueda_lineal(arreglo, elemento_buscar)
        elif elec == 2:
            indice = busqueda_binaria(arreglo, elemento_buscar)
        else: 
            print("Esa opción es inexistente maistro")
            return
    
        if indice != -1:
            print(f"{elemento_buscar} se encuentra en el índice {indice} del arreglo.")
        else:
            print(f"{elemento_buscar} no se encuentra en el arreglo.")

    except ValueError:
        print("Ingrese un número válido.")

if __name__ == "__main__":  #Esta cosa por así decirlo controla la ejecución de este programa, existe porque esta programado como un script
    main()                  #Funciona, no lleguemos más detalles de los que conocemos.




