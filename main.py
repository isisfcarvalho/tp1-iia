import numpy as np
import sys
import bfs
import dijkstra
import ids
import greedy
import common

args = sys.argv
argc = len(args)

alg = args[1]
array_size = int(args[2])
array = []
for i in range(array_size):
    array.append(int(args[i + 3]))
array = np.array(array)

if argc >= array_size + 4 and args[array_size + 3] == 'PRINT':
    opt_print = True
else:
    opt_print = False

if alg == 'B':
    result = bfs.BFS(array, opt_print)

elif alg == 'I':
    result = ids.IDS(array, opt_print)

elif alg == 'U':
    result = dijkstra.Dijkstra(array, opt_print)
    
elif alg == 'A':
    #A*
    pass

elif alg == 'G':
    result = greedy.Greedy(array, opt_print)

else:
    #error
    pass

if result == 0:
    print('failure')