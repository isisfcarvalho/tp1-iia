# Gera representação de um array em string
def concatenate_array(array, sep):
  return sep.join(map(str, array))

# Explora nós apenas se o elemento da esquerda for maior que o da direita, insere numa lista de tuplas
# Tupla (array, custo), dados necessários para inicializar novos nós
def explore_node(node):
  children_arrays = []
  for i in range(node.array.size):
    for j in range(i + 1, node.array.size):
      new_array = node.array.copy()
      if new_array[i] > new_array[j]:
        new_array[i], new_array[j] = new_array[j], new_array[i]
        if abs(j - i) == 1:
          cost = 2
        else:
          cost = 4
        children_arrays.append((new_array, cost))
  return children_arrays

# Percorre caminho de nós, da solução até a raiz, inverte esse caminho e imprime
def get_path(node):
  path = []
  while node is not None:
    path.append(node.array)
    node = node.parent

  path.reverse()
  for i in path:
    print(*i, sep=" ")

# Heurística implementada, soma número de elementos fora de ordem
def heuristic(array, goal):
  n = array.size
  cost = (goal!=array).sum()
  return cost