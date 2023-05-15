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

  frontier = []
  frontier.append(root)
  count_explored = 0

  while len(frontier) > 0:
    node = frontier.pop()
    #print(f"NOVO NÓ SENDO EXPLORADO: {node.array}")
    count_explored += 1
    if np.array_equal(node.array, goal):
      print(f'Found solution using IDS, depth {node.depth}: {node.total_cost}, {count_explored}')
      if opt_print:
        get_path(node)
      result = 1
      break

    if node.depth + 1 > limit:
      result = 0
      continue
    for child_array in explore_node(node):
    
      child = NodeIDS(child_array[0], node.total_cost + child_array[1], node, node.depth + 1)
      #print(f"Novo array adicionado à fronteira: {child.array}, depth = {child.depth}")
      frontier.append(child)

  return result
    

def IDS(array, opt_print):
  n = array.size
  for depth in range(n*2):
    #print(f'Iteração com depth = {depth} ------------------------------------------------------------------------------------------')
    result = DFSLimited(array, depth, opt_print)
    if result == 1:
      return 1
    else:
      continue
  return 0