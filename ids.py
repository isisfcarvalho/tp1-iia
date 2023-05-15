import numpy as np
from common import concatenate_array, get_path, explore_node

class NodeIDS:
  def __init__(self, array, cost, parent, depth):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
    self.parent = parent
    self.depth = depth

def DFSLimited(origArray, limit, opt_print=False):
  root = NodeIDS(origArray, 0, None, 0)
  goal = np.arange(1, origArray.size + 1)

  # Fronteira é apenas uma lista, já que não temos que fazer nenhuma busca nessa fronteira 
  # (não precisamos da eficiência de busca dos dicts)
  frontier = []
  frontier.append(root)
  count_explored = 0

  # Enquanto fronteira não estiver vazia
  while len(frontier) > 0:
    node = frontier.pop()
    count_explored += 1
    # Goal test
    if np.array_equal(node.array, goal):
      print(f'{node.total_cost} {count_explored}')
      if opt_print:
        get_path(node)
      result = 1
      break

    # Se nó está no limite de profundidade, vamos para próxima iteração
    if node.depth + 1 > limit:
      result = 0
      continue

    # Para cada filho, cria-se objeto NodeIDS e o insere na fronteira
    for child_array in explore_node(node):
      child = NodeIDS(child_array[0], node.total_cost + child_array[1], node, node.depth + 1)
      frontier.append(child)

  return result
    

def IDS(array, opt_print):
  n = array.size
  # Para cada profundidade possível (2n é limite arbitrário), chamamos busca limitada por profundidade
  for depth in range(n*2):
    result = DFSLimited(array, depth, opt_print)
    if result == 1:
      return 1
    else:
      continue
  return 0