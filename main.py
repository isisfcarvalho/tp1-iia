import numpy as np
import sys
import bfs

args = sys.argv
argc = len(args)

alg = args[1]
array_size = int(args[2])
array = []
for i in range(array_size):
    array.append(int(args[i + 3]))
array = np.array(array)

if argc >= array_size + 4:
    opt_print = args[array_size + 3]
else:
    opt_print = None

if alg == 'B':
    expl_list = bfs.BFS(array)
    if opt_print == "PRINT":
        for i in expl_list:
            print(i)

elif alg == 'I':
    #iterative
    pass

elif alg == 'U':
    #uniform cost (dijkstra)
    pass

elif alg == 'A':
    #A*
    pass

elif alg == 'G':
    #greedy
    pass

else:
    #error
    pass
