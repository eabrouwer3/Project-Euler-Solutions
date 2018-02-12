#Problem 18/67 using A* Search 
#Problem 18: "Problem 18 nums.txt" to 14
#Problem 67: "triangle.txt" to 99

from collections import deque
import sys
import uuid;

class node:
	def __init__(self, a, m, p, t, ny, nx):
	    self.actualScore = a
            self.minScore = m
	    self.previous = p
	    self.totalScore = t
	    self.y = ny
            self.x = nx

sys.setrecursionlimit(10000)
f = open('triangle.txt', 'r')
actualRows = [[n for n in p.split(" ")] for p in f.read().split('\n')]
actualRows.pop()
actualRows = [[int(n) for n in p] for p in actualRows]
rows = [{str(uuid.uuid4().get_hex().upper()[0:6]): 100 - n for n in p} for p in actualRows]

print len(actualRows)

def astar(pq):
    m = min(pq,key=lambda w: w[3])
    if len(m[2]) + 1 is len(actualRows):
        return m
    pq.remove(m)
    toAdd = list(m[2])
    toAdd.append(m[0])
    pq.append((actualRows[m[4]+1][m[5]], rows[m[4]+1][m[5]], toAdd, m[3] + m[1], m[4]+1, m[5]))
    pq.append((actualRows[m[4]+1][m[5]+1], rows[m[4]+1][m[5]+1], toAdd, m[3] + m[1], m[4]+1, m[5]+1))
    return astar(pq)
	
def dijkstra(root, goal):
    D = {} # Final distances dict
    P = {} # Predecessor dict
	
	# Fill the dicts with the default values
	D[root] = root.minScore
	
	while len(D) < 100:
	    # Select the node with the lowest value in D (final distance)
		shortest = None
		node = ''
		m = min([node(actualRows[root.y + 1][root.x], rows[root.y + 1][root.x], root.previous + root, root.totalScore + root.actualScore, root.y + 1, root.x),node(actualRows[root.y + 1][root.x + 1], rows[root.y + 1][root.x + 1], root.previous + root, root.totalScore + root.actualScore, root.y + 1, root.x + 1)],key=lambda w: w[3])

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def bfs(graph, start):
    visited, queue = set(), [start]
	while queue:
	    vertex = queue.pop(0)
		if vertex not in visited:
		    visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

# Each tuple is: (actualScore, minScore, previous, totalScore, y, x)
priorityQueue = [(actualRows[0][0], rows[0][0], [], 0, 0, 0)]
a = bfs(rows, rows[0][])
print a
print str(sum(a[2]) + a[0])
