import heapq
import time

def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
class Graph:
    def __init__(self):
        self.graph = {}
#Método para agregar vertices. Pregunta si no existe el vertice ya, en caso de que no existe lo concatenara a self.graph
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)
        self.graph[start].append((end, weight))
#Para hacer a las aristas, el código tiene que estar preguntando si el vértice inicial y el vértice inicial no existen ya. Para el primero simplemente se agreg a self.graph, para el segundo
#se agrega el vertice de destino y se le asigna un peso, todo esto concatenado en self.graph
    def dijkstra(self, start):
        # Inicializar distancias y conjunto de vértices visitados
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        visited = set()

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # pregunta para saber si ya se visite un vértice adyacente 
            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            # Actualizar las distancias para los vértices adyacentes
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # preguntamos por una distancia más corta para en su caso actualizarls
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

#Usamos el método add_Vertex para introducir en una lista un string que representará nuestros vertices
grafo = Graph()
grafo.add_vertex("A")
grafo.add_vertex("B")
grafo.add_vertex("C")
grafo.add_vertex("D")

#Definimos con el método add_edge los vértices que son adyacentes entre sí y su distancia entre ellos con la variable weigh. Por ejemplo, entre A y B tenemos un peso en el camino de 3.
#Entre A y C un peso de 5 y así seguidamente, en el método se trabajará con estos datos como las variables start, end y weigh.
grafo.add_edge("A", "B", 2)
grafo.add_edge("B", "A", 2)
grafo.add_edge("A", "C", 5)
grafo.add_edge("C", "A", 5)
grafo.add_edge("B", "C", 3)
grafo.add_edge("C", "B", 3)
grafo.add_edge("B", "D", 2)
grafo.add_edge("D", "B", 2)
grafo.add_edge("D", "C", 1)
grafo.add_edge("C", "D", 1)
#Por la manera de trabajar del código definiendo el primer vertice como
#inicio y el segundo como final, fue necesario definir las aristas dos
#veces, la primera tomando un vertice de inicio y otro de final, y la 
#segunda tomando ambos vertices al reves, el del final como inicio y 
#el de inicio como final.

#Llamamos a la funcion dijkstra para que calcule la distancia más corta a los vértices que tiene adyacentes
start_vertex = "A"
caminos_minimos = grafo.dijkstra(start_vertex)
print(f"Caminos mínimos desde {start_vertex}: {caminos_minimos}")
resultado, tiempo_ejecucion = measure_execution_time(grafo.dijkstra, "A")
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")



