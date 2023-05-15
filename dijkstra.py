import numpy as np
import heapq
from common import concatenate_array, get_path, explore_node

class NodeDijkstra:
  def __init__(self, array, cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
    self.parent = parent
    self.valid = 1
  
  def invalid_node(self):
    self.valid = 0

def Dijkstra(origArray, opt_print=False):
  root = NodeDijkstra(origArray, 0, None)
  goal = np.arange(1, origArray.size + 1)

  frontier = [(root.total_cost, root.str_rep)]
  heapq.heapify(frontier)
  frontier_dict = {root.str_rep: root}
  explored_dict = {}

  while len(frontier) > 0:
    node_cost, node_str_rep = heapq.heappop(frontier)
    if node_str_rep in explored_dict:
      continue
    node = frontier_dict.get(node_str_rep)
    if not node.valid:
      continue
    if np.array_equal(node.array, goal):
      print(f'Found solution using Dijkstra: {node.total_cost}, {len(explored_dict)}')
      #print('Path:')
      if opt_print:
        get_path(node)
      #return explored_dict
      return 1
    explored_dict.update({node.str_rep: node})
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}, custo = {node.total_cost}")
    for child_array in explore_node(node):
      child = NodeDijkstra(child_array[0], node.total_cost + child_array[1], node)
      if (child.str_rep not in frontier_dict) and (child.str_rep not in explored_dict):
        new_node = (child.total_cost, child.str_rep)
        heapq.heappush(frontier, new_node)
        frontier_dict.update({child.str_rep: child})
        #print(f"Novo array adicionado à fronteira: {child.array}, custo = {child.total_cost}")
      elif child.str_rep in frontier_dict:
        old_node = frontier_dict.get(child.str_rep)
        if old_node.total_cost > child.total_cost:
          new_node = (child.total_cost, child.str_rep)
          heapq.heappush(frontier, new_node)
          frontier_dict.update({child.str_rep: child})
          old_node.invalid_node()
          #print(f"Atualização do custo de {child.array} ({child.total_cost}), substituiu antigo de custo {old_node.total_cost}")
  return 0
