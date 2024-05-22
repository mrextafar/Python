import heapq

count = 0
def Dijkstra(graph, start):#0(N^2)
    global count
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        count += 1

        current_distance, current_vertex = heapq.heappop(queue)

        # Обрабатываем только вершину с наименьшим расстоянием
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
graph = {
	"A": {'B': 1, 'C': 3, 'D': 7, 'E': 2},
	"B": {'A': 1, 'C': 7, 'D': 8, 'E': 9},
	"C": {'A': 3, 'B': 7, 'D': 4, 'E': 1},
    "D": {'A': 7, 'B': 8, 'C': 4, 'E': 3},
    'E': {"A": 2, 'B': 9, 'C': 1, 'D': 3}
}

print(Dijkstra(graph,"A"))
print(count)