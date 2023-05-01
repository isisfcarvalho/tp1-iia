import numpy as np
import heapq
from common import Node, concatenate_array, getPath

'''def concatenate_array(array, sep):
  return sep.join(map(str, array))

class Node:
  def __init__(self, array, cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
    self.parent = parent'''

'''def getPath(node):
  path = []
  while node is not None:
    path.append(node.array)
    node = node.parent

  path.reverse()
  for i in path:
    print(i)'''


def Dijkstra(origArray, opt_print=False):
  root = Node(origArray, 0, None)
  goal = np.sort(origArray)

  frontier = [(root.total_cost, root.str_rep)]
  heapq.heapify(frontier)
  frontier_dict = {root.str_rep: root}
  explored_list = []

  while len(frontier) > 0:
    node_cost, node_str_rep = heapq.heappop(frontier)
    node = frontier_dict.get(node_str_rep)
    if np.array_equal(node.array, goal):
      print(f'Found solution using Dijkstra: {node.total_cost}, {len(explored_list)}')
      #print('Path:')
      if opt_print:
        getPath(node)
      #return explored_list
      return 1
    explored_list.append(node.str_rep)
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}")
    for i in range(node.array.size):
      for j in range(i + 1, node.array.size):
        new_array = node.array.copy()
        new_array[i], new_array[j] = new_array[j], new_array[i]
        if abs(j - i) == 1:
          cost = 2
        else:
          cost = 4
        child = Node(new_array, node.total_cost + cost, node)
        if (child.str_rep not in frontier_dict) and (child.str_rep not in explored_list):
          new_node = (child.total_cost, child.str_rep)
          heapq.heappush(frontier, new_node)
          frontier_dict.update({child.str_rep: child})
          #print(f"Novo array adicionado à fronteira: {child.array}")
        elif child.str_rep in frontier_dict:
          old_node = frontier_dict.get(child.str_rep)
          if old_node.total_cost > child.total_cost:
            frontier_dict[child.str_rep] = child
            #print(f"Atualização do custo de {child.array} ({child.total_cost}), substituiu antigo de custo {old_node.total_cost}")
  return 0
