import time
from common import get_neighbors

def solve_dfs(maze, start, goal):
    """Solve maze using DFS. Returns (path, number of steps, runtime)."""
    start_time = time.time()
    stack = [(start, [start])]
    visited = set()
    while stack:
        current, path = stack.pop()
        if current == goal:
            runtime = time.time() - start_time
            return path, len(path), runtime
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None, 0, time.time() - start_time

if __name__ == "__main__":
    pass