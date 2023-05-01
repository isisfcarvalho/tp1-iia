def concatenate_array(array, sep):
  return sep.join(map(str, array))

class Node:
  def __init__(self, array, cost, parent):
    self.array = array
    self.str_rep = concatenate_array(array, '-')
    self.total_cost = cost
    self.parent = parent

def getPath(node):
  path = []
  while node is not None:
    path.append(node.array)
    node = node.parent

  path.reverse()
  for i in path:
    print(i)