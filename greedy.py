import numpy as np
import heapq
from common import concatenate_array, getPath

def heuristic(array, goal):
  n = array.size
  cost = n * (n - (goal==array).sum())
  return cost

class NodeGreedy:
  def __init__(self, array, step_cost, heuristic_cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = step_cost
    self.heuristic = heuristic_cost
    self.parent = parent

def Greedy(origArray, opt_print):
  goal = np.sort(origArray)
  root = NodeGreedy(origArray, 0, heuristic(origArray, goal), None)

  frontier = [(root.heuristic, root.str_rep)]
  heapq.heapify(frontier)
  frontier_dict = {root.str_rep: root}
  explored_list = []

  while len(frontier) > 0:
    _, node_str_rep = heapq.heappop(frontier)
    node = frontier_dict.get(node_str_rep)
    if np.array_equal(node.array, goal):
      print(f'Found solution using Greedy: {node.total_cost}, {len(explored_list)}')
      #print('Path:')
      if opt_print:
        getPath(node)
      #return explored_list
      return 1
    explored_list.append(node.str_rep)
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}, custo = {node.heuristic}")
    for i in range(node.array.size):
      for j in range(i + 1, node.array.size):
        new_array = node.array.copy()
        new_array[i], new_array[j] = new_array[j], new_array[i]
        if abs(j - i) == 1:
          cost = 2
        else:
          cost = 4
        child = NodeGreedy(new_array, node.total_cost + cost, heuristic(new_array, goal), node)
        if (child.str_rep not in frontier_dict) and (child.str_rep not in explored_list):
          new_node = (child.heuristic, child.str_rep)
          heapq.heappush(frontier, new_node)
          frontier_dict.update({child.str_rep: child})
          #print(f"Novo array adicionado à fronteira: {child.array}, custo = {child.heuristic}")
        elif child.str_rep in frontier_dict:
          old_node = frontier_dict.get(child.str_rep)
          # Precisa fazer isso?
          if old_node.total_cost > child.total_cost:
            frontier_dict[child.str_rep] = child
            #print(f"Atualização do custo de {child.array} ({child.total_cost}), substituiu antigo de custo {old_node.total_cost}")
  
  return 0