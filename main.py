import numpy as np
import sys
import bfs
import dijkstra
import ids
import greedy
import astar
import common
import time

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
    if argc >= array_size + 5 and args[array_size + 4] != None:
        iters = int(args[array_size + 4])
    else: 
        iters = 1
elif argc >= array_size + 4 and args[array_size + 3] != None:
    iters = int(args[array_size + 3])
    opt_print = False
elif argc < array_size + 4:
    iters = 1
    opt_print = False

times = []

for _ in range(iters):
    start = time.time()

    if alg == 'B':
        result = bfs.BFS(array, opt_print)
        end = time.time()


    elif alg == 'I':
        result = ids.IDS(array, opt_print)
        end = time.time()

    elif alg == 'U':
        result = dijkstra.Dijkstra(array, opt_print)
        end = time.time()
        
    elif alg == 'A':
        result = astar.AStar(array, opt_print)
        end = time.time()
        pass

    elif alg == 'G':
        result = greedy.Greedy(array, opt_print)
        end = time.time()

    else:
        print('Wrong algorithm parameter')

    print('Time elapsed: {:.4f}s'.format(end-start))
    times.append(end-start)

    if result == 0:
        print('failure')

print(f"Média dos tempos: {np.round(np.mean(times), 6)}")