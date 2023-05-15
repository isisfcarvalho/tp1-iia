import numpy as np
from collections import OrderedDict
from common import concatenate_array, get_path, explore_node

class NodeBFS:
  def __init__(self, array, cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
    self.parent = parent

def BFS(origArray, opt_print=False):

  root = NodeBFS(origArray, 0, None)
  goal = np.arange(1, origArray.size + 1)
  # Se root == goal, já achamos a solução
  if np.array_equal(origArray, goal):
    print("0 0")
    if opt_print:
      get_path(root)
    return 1

  # Criação de dicionários de nós explorados e fronteira (com política FIFO)
  explored = {}
  frontier = OrderedDict()
  frontier.update({root.str_rep: root})

  # Enquanto fronteira não estiver vazia, pega o primeiro nó da fronteira
  while len(frontier) != 0:
    (_, node) = frontier.popitem(last=False)
    # Insere nó no conjunto de explorados
    explored.update({node.str_rep: node})
    # Para cada nó filho válido, cria objeto NodeBFS
    for child_array in explore_node(node):
      child = NodeBFS(child_array[0], node.total_cost + child_array[1], node)
      # Checa se nó não tá na fronteira nem nos explorados: se não, faz goal test
      if (child.str_rep not in frontier) and (child.str_rep not in explored):
        if np.array_equal(child_array[0], goal):
          print(f'{child.total_cost} {len(explored)}')
          if opt_print:
            get_path(child)
          return 1
        # Se goal test falhar, insere nó na fronteira
        frontier.update({child.str_rep: child})

  return 0