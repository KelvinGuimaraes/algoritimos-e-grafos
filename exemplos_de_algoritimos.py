"""
Algoritimo de dijkstra
"""

import heapq

def dijkstra(V, adj_list, inicio, end):
    dist = [float('inf')] * V
    dist[inicio] = 0
    pq = [(0, inicio)]  # (distância, vértice)

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in adj_list[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist[end]

# entrada
V = 5
E = 6
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]
inicio = 0
end = 4

# Construção da lista de adjacências
adj_list = [[] for _ in range(V)]
for u, v, w in edges:
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

# Chamada da função Dijkstra
result = dijkstra(V, adj_list, inicio, end)
print(result)  # Saída esperada: 6


"""
Algoritmo de detecção de ciclos em grafos direcionados.
"""

def has_cycle(V, adj_list):
    visited = [False] * V
    rec_stack = [False] * V

    def dfs(v):
        if not visited[v]:
            visited[v] = True
            rec_stack[v] = True

            for neighbor in adj_list[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True

        rec_stack[v] = False
        return False

    for i in range(V):
        if dfs(i):
            return True

    return False

# Exemplo de entrada
V = 4
E = 4
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 1)
]

# Construção da lista de adjacências
adj_list = [[] for _ in range(V)]
for u, v in edges:
    adj_list[u].append(v)

# Chamada da função pra o ciclo
result = has_cycle(V, adj_list)
print(result)  # Saída: True


"""
Componentes conexos em um grafo não direcionado
"""

def find_connected_components(V, adj_list):
    visited = [False] * V
    components = []

    def dfs(v, compo):
        stack = [v]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                compo.append(node)
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    for i in range(V):
        if not visited[i]:
            compo = []
            dfs(i, compo)
            components.append(compo)

    return components

# Exemplo de entrada
V = 6
E = 4
edges = [
    (0, 1),
    (1, 2),
    (3, 4),
    (4, 5)
]

#lista de adjacências de grafo não direcionado
adj_list = [[] for _ in range(V)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

#encontrar componentes conexos
result = find_connected_components(V, adj_list)
print(result)  # Saída: [[0, 1, 2], [3, 4, 5]]