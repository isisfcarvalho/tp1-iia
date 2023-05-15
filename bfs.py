import numpy as np
from collections import OrderedDict
from common import concatenate_array, get_path, explore_node

class NodeBFS:
  def __init__(self, array, cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
    self.parent = parent

def BFS(origArray, opt_print=False): #imprime custo e número de nós explorados

  root = NodeBFS(origArray, 0, None)
  goal = np.arange(1, origArray.size + 1)
  # Se root == goal, já achamos a solução
  if np.array_equal(origArray, goal):
    #explored_list = [origArray]
    print("0 0")
    if opt_print:
      get_path(root)
    #return explored_list
    return 1

  #explored_list = []
  explored = {}
  frontier = OrderedDict()
  frontier.update({root.str_rep: root})
  k = 0
  while len(frontier) != 0:
    (_, node) = frontier.popitem(last=False)
    explored.update({node.str_rep: node})
    #explored_list.append(node.array)
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}")
    for child_array in explore_node(node):
      child = NodeBFS(child_array[0], node.total_cost + child_array[1], node)
      if (child.str_rep not in frontier) and (child.str_rep not in explored):
        if np.array_equal(child_array[0], goal):
          print(f'Found solution using BFS: {child.total_cost}, {len(explored)}')
          if opt_print:
            get_path(child)
          #explored_list.append(new_array)
          #return explored_list
          return 1
        frontier.update({child.str_rep: child})
        #print(f"Novo array adicionado à fronteira: {child.array}")

  return 0