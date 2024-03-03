from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return  
    

def bfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    queue = deque([start]) 
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)


graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'D'},
    'D': {'E'},
    'E': {'D'},
}


print("DFS:")
dfs(graph, 'A')
print("\nBFS:")
bfs(graph, 'A')

