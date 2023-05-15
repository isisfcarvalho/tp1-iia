import numpy as np
import heapq
from common import concatenate_array, get_path, heuristic, explore_node

class NodeAStar:
  def __init__(self, array, step_cost, heuristic_cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.real_cost = step_cost
    self.heuristic = heuristic_cost
    self.parent = parent
    self.total_cost = self.real_cost + self.heuristic
    self.valid = 1
  
  def invalid_node(self):
    self.valid = 0

def AStar(origArray, opt_print):
  goal = np.arange(1, origArray.size + 1)
  root = NodeAStar(origArray, 0, heuristic(origArray, goal), None)

  frontier = [(root.total_cost, root.str_rep)]
  heapq.heapify(frontier)
  frontier_dict = {root.str_rep: root}
  explored_dict = {}

  while len(frontier) > 0:
    _, node_str_rep = heapq.heappop(frontier)
    if node_str_rep in explored_dict:
      continue
    node = frontier_dict.get(node_str_rep)
    if not node.valid:
      continue
    if np.array_equal(node.array, goal):
      print(f'Found solution using A*: {node.real_cost}, {len(explored_dict)}')
      #print('Path:')
      if opt_print:
        get_path(node)
      #return explored_list
      return 1
    explored_dict.update({node.str_rep: node})
    frontier_dict.pop(node.str_rep)
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}, custo = {node.heuristic}")
    for child_array in explore_node(node):
      child = NodeAStar(child_array[0], node.real_cost + child_array[1], heuristic(child_array[0], goal), node)
      if (child.str_rep not in frontier_dict) and (child.str_rep not in explored_dict):
        new_node = (child.total_cost, child.str_rep)
        heapq.heappush(frontier, new_node)
        frontier_dict.update({child.str_rep: child})
        #print(f"Novo array adicionado à fronteira: {child.array}, custo = {child.heuristic}")
      elif child.str_rep in frontier_dict:
        old_node = frontier_dict.get(child.str_rep)
        # Precisa fazer isso?
        if old_node.total_cost > child.total_cost:
          new_node = (child.total_cost, child.str_rep)
          heapq.heappush(frontier, new_node)
          frontier_dict.update({child.str_rep: child})
          old_node.invalid_node()
          #print(f"Atualização do custo de {child.array} ({child.real_cost}), substituiu antigo de custo {old_node.real_cost}")
  
  return 0