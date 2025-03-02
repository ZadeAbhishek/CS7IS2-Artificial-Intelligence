import time
from collections import deque
from maze_generator.common import get_neighbors

def solve_bfs(maze, start, goal):
    start_time = time.time()
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == goal:
            runtime = time.time() - start_time
            return path, len(path), runtime
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None, 0, time.time() - start_time

if __name__ == "__main__":
    pass