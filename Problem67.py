import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
   
    def empty(self):
        return len(self.elements) == 0
   
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
   
    def get(self):
        return heapq.heappop(self.elements)[1]

def neighbors(point):
    return (point[0], str(int(point[1]) + 1)), (str(int(point[0]) + 1), str(int(point[1]) + 1))

def cost(next):
    try:
        return int(rows[int(next[0])][int(next[1])])
    except IndexError:
        return -1

def reconstruct_path(came_from, start, goal):
   current = goal
   path = [current]
   while current != start:
      current = came_from[current]
      path.append(current)
   return path

f = open('triangle.txt', 'r')

def opposite(n):
    return str(100 - int(n))

rows = [[n for n in p.split(" ")] for p in f.read().split('\n')]
rows = [[opposite(n) for n in rows[x]] for x in xrange(100)]

def heuristic(a, b):
   (x1, y1) = a
   (x2, y2) = b
   return abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            return came_from, cost_so_far
      
        for next in neighbors(current):
            if cost(next) >= 0:
                new_cost = cost_so_far[current] + cost(next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current
   
    return came_from, cost_so_far

came_from, cost_so_far = a_star_search(rows, ("0","0"), ("99", "99"))

path = reconstruct_path(came_from, ("0","0"), ("99","99"))
print path

pathSum = 0
for p in path:
   pathSum = pathSum + cost(p)

print pathSum
