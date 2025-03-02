import time
import heapq
from maze_generator.common import get_neighbors

def solve_astar(maze, start, goal):
    start_time = time.time()
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    visited = {}
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            runtime = time.time() - start_time
            return path, len(path), runtime
        if current in visited and visited[current] <= g:
            continue
        visited[current] = g
        for neighbor in get_neighbors(current, maze):
            new_cost = g + 1
            heapq.heappush(open_set, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))
    return None, 0, time.time() - start_time
