def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")

def print_path(predecessors, start, end):
    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = predecessors.get(current_vertex, None)
        if current_vertex is None:  # If there's no predecessor, break the loop
            print("Шляху не існує")
            return
    path.insert(0, start)
    print("Найкоротший шлях від {} до {}: {}".format(start, end, " -> ".join(path)))

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        print_table(distances, visited)

    print_path(predecessors, start, end)
    return distances


graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

dijkstra(graph, 'A', 'E')
