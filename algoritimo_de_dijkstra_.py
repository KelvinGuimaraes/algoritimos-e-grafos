
import heapq # usado para implementar a fila de prioridade

def dijkstra(grafo, origem):
  """
  Implementação do algoritmo de Dijkstra para encontrar o caminho mínimo entre um vértice de origem e todos os outros vértices em um grafo ponderado(que possui pesos).
  Argumentos:
    grafo: Um dicionário que representa o grafo. As chaves do dicionário são os vértices e os valores são dicionários que mapeiam os vértices vizinhos aos seus pesos.
    origem: O vértice de origem.
  Retorna:
    Um dicionário que mapeia os vértices aos seus custos mínimos de origem.
  """

  # Inicializa as distâncias mínimas.
  distancias_minimas = {vertice: float('inf') for vertice in grafo} #cria um dicionario onde cada vertice recebe o valor infinito de distacia exeto o de origem que recebe 0
  distancias_minimas[origem] = 0 #recebendo 0

  # Inicializa a fila de prioridade.
  fila_prioridade = [(0, origem)] # cria uma fila de prioridade ciontendo uma tupla indicando que o vertice de origem tem custo 0 e deve ser o primeiro a ser processado

  while fila_prioridade:#loop principal enquanto houver vertices e caminhos ele continua

    #remove a tupla com o menor custo atual (custo_atual) da fila de prioridade e armazena os valores em custo_atual e vertice_atual Isso significa que o vértice vertice_atual é o próximo candidato a ter sua distância mínima atualizada.
    custo_atual, vertice_atual = heapq.heappop(fila_prioridade)

    # Se o custo atual for maior que a distância mínima do vértice, significa que já encontramos um caminho mais curto.
    if custo_atual > distancias_minimas[vertice_atual]:
      continue

    # Atualiza as distâncias mínimas dos vizinhos.
    for vizinho, peso in grafo[vertice_atual].items():
      novo_custo = custo_atual + peso
      if novo_custo < distancias_minimas[vizinho]:
        distancias_minimas[vizinho] = novo_custo
        heapq.heappush(fila_prioridade, (novo_custo, vizinho))

  return distancias_minimas

# Exemplo de uso

# montando grafo com as ligaçoe e seus repectivos pesos
grafo = {
  '1': {'2': 4},
  '2': {'1': 5, '4': 7, '5':11},
  '3': {'1': 7, '5':1},
  '4': {'5': 3, '3': 11},
  '5': {}
}

origem = '1' #ponto de onde a gente deseja sair

distancias_minimas = dijkstra(grafo, origem)

print('distancias minimas até os outros pontos:', distancias_minimas) #resultado de todas as distancias minimass da origem ate os demais