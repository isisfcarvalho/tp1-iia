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

  # Fronteira é lista de tuplas, inicializada com nó raiz e transformada em heap
  frontier = [(root.total_cost, root.str_rep)]
  heapq.heapify(frontier)
  frontier_dict = {root.str_rep: root}
  explored_dict = {}

  # Enquanto fronteira não estiver vazia, damos um pop no heap e recuperamos os dados do nó no dict
  while len(frontier) > 0:
    _, node_str_rep = heapq.heappop(frontier)
    # Se nó já tiver sido explorado, vamos para próxima iteração
    if node_str_rep in explored_dict:
      continue
    node = frontier_dict.get(node_str_rep)
    # Se nó não for válido, vamos para próxima iteração    
    if not node.valid:
      continue

    # Goal test e atualização do conjunto de nós explorados
    if np.array_equal(node.array, goal):
      print(f'{node.real_cost} {len(explored_dict)}')
      if opt_print:
        get_path(node)
      return 1
    explored_dict.update({node.str_rep: node})
    # Para cada nó filho, criamos objeto NodeAStar
    for child_array in explore_node(node):
      child = NodeAStar(child_array[0], node.real_cost + child_array[1], heuristic(child_array[0], goal), node)
      # Se nó não está na fronteira nem nos explorados, inserimos ele na fronteira
      if (child.str_rep not in frontier_dict) and (child.str_rep not in explored_dict):
        new_node = (child.total_cost, child.str_rep)
        heapq.heappush(frontier, new_node)
        frontier_dict.update({child.str_rep: child})
      # Se nó na fronteira, checamos se seu custo é menor que o nó que já está na fronteira
      elif child.str_rep in frontier_dict:
        old_node = frontier_dict.get(child.str_rep)
        # Se for o caso, invalidamos o nó antigo e inserimos o novo nó na fronteira
        if old_node.total_cost > child.total_cost:
          new_node = (child.total_cost, child.str_rep)
          heapq.heappush(frontier, new_node)
          frontier_dict.update({child.str_rep: child})
          old_node.invalid_node()
  
  return 0