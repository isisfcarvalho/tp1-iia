import numpy as np
from collections import OrderedDict

def concatenate_array(array, sep):
  return sep.join(map(str, array))

class NodeBFS:
  def __init__(self, array, cost):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
  
  def putOnDict(self, dict):
    dict.update({self.str_rep: self.total_cost})

def BFS(origArray): #imprime custo e número de nós explorados
  root = NodeBFS(origArray, 0)
  goal = np.sort(origArray)
  # Se root == goal, já achamos a solução
  if np.array_equal(origArray, goal):
    explored_list = [origArray]
    print("0 0")
    return explored_list

  explored_list = []
  explored = {}
  frontier = OrderedDict()
  frontier.update({root.str_rep: root})
  k = 0
  while len(frontier) != 0:
    (_, node) = frontier.popitem(last=False)
    explored.update({node.str_rep: node})
    explored_list.append(node.array)
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}")
    for i in range(node.array.size):
      for j in range(i + 1, node.array.size):
        k +=1
        new_array = node.array.copy()
        new_array[i], new_array[j] = new_array[j], new_array[i]
        if abs(j - i) == 1:
          cost = 2
        else:
          cost = 4
        child = NodeBFS(new_array, node.total_cost + cost)
        if (child.str_rep not in frontier) and (child.str_rep not in explored):
          if np.array_equal(new_array, goal):
            print(f'Found solution: {child.total_cost}, {len(explored)}')
            explored_list.append(new_array)
            return explored_list
          frontier.update({child.str_rep: child})
          #print(f"Novo array adicionado à fronteira {k}: {child.array}")
