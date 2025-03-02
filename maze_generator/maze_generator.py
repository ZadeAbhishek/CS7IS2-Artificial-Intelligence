import numpy as np
import random
import matplotlib.pyplot as plt

def enforce_borders(maze):
    maze[0, :] = 1
    maze[-1, :] = 1
    maze[:, 0] = 1
    maze[:, -1] = 1
    return maze

def create_maze_dfs(dim):
    maze = np.ones((dim * 2 + 1, dim * 2 + 1), dtype=int)
    x, y = 0, 0
    maze[2 * x + 1, 2 * y + 1] = 0
    stack = [(x, y)]
    
    while stack:
        x, y = stack[-1]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        found = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < dim and 0 <= ny < dim and maze[2 * nx + 1, 2 * ny + 1] == 1:
                maze[2 * nx + 1, 2 * ny + 1] = 0
                maze[2 * x + 1 + dx, 2 * y + 1 + dy] = 0
                stack.append((nx, ny))
                found = True
                break
        if not found:
            stack.pop()
    

    maze[1, 0] = 0
    maze[-2, -1] = 0

    maze = enforce_borders(maze)
    maze[1, 0] = 0
    maze[-2, -1] = 0
    
    return maze

def create_maze_prims(dim, extra_openings=0):
    maze = np.ones((2 * dim + 1, 2 * dim + 1), dtype=int)
    start_x = random.randint(0, dim - 1)
    start_y = random.randint(0, dim - 1)
    maze[2 * start_x + 1, 2 * start_y + 1] = 0
    walls = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = start_x + dx
        ny = start_y + dy
        if 0 <= nx < dim and 0 <= ny < dim:
            wx = 2 * start_x + 1 + dx
            wy = 2 * start_y + 1 + dy
            walls.append((start_x, start_y, nx, ny, wx, wy))
    visited = {(start_x, start_y)}
    
    while walls:
        idx = random.randint(0, len(walls) - 1)
        cell_x, cell_y, nx, ny, wx, wy = walls.pop(idx)
        if (nx, ny) not in visited:
            maze[wy, wx] = 0
            maze[2 * nx + 1, 2 * ny + 1] = 0
            visited.add((nx, ny))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nxx = nx + dx
                nyy = ny + dy
                if 0 <= nxx < dim and 0 <= nyy < dim and (nxx, nyy) not in visited:
                    wx2 = 2 * nx + 1 + dx
                    wy2 = 2 * ny + 1 + dy
                    walls.append((nx, ny, nxx, nyy, wx2, wy2))
                    

    for _ in range(extra_openings):
        i = random.randint(1, 2 * dim - 1)
        j = random.randint(1, 2 * dim - 1)
        maze[i, j] = 0
        
    maze[1, 0] = 0
    maze[-2, -1] = 0

    maze = enforce_borders(maze)
    maze[1, 0] = 0
    maze[-2, -1] = 0
    
    return maze

def create_maze_aldous_broder(n, m, complexity=0):
    maze = np.ones((2 * n + 1, 2 * m + 1), dtype=int)
    visited = np.zeros((n, m), dtype=bool)
    start_x = random.randint(0, n - 1)
    start_y = random.randint(0, m - 1)
    visited[start_x, start_y] = True
    cells_visited = 1
    total_cells = n * m
    maze[2 * start_x + 1, 2 * start_y + 1] = 0
    current = (start_x, start_y)
    
    while cells_visited < total_cells:
        x, y = current
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y, 'N'))
        if x < n - 1:
            neighbors.append((x + 1, y, 'S'))
        if y > 0:
            neighbors.append((x, y - 1, 'W'))
        if y < m - 1:
            neighbors.append((x, y + 1, 'E'))
        nx, ny, direction = random.choice(neighbors)
        if not visited[nx, ny]:
            if direction == 'N':
                maze[2 * x, 2 * y + 1] = 0
            elif direction == 'S':
                maze[2 * x + 2, 2 * y + 1] = 0
            elif direction == 'W':
                maze[2 * x + 1, 2 * y] = 0
            elif direction == 'E':
                maze[2 * x + 1, 2 * y + 2] = 0
            visited[nx, ny] = True
            cells_visited += 1
        maze[2 * nx + 1, 2 * ny + 1] = 0
        current = (nx, ny)
    

    maze[1, 0] = 0
    maze[-2, -1] = 0
    

    for _ in range(complexity):
        i = random.randint(1, 2 * n - 1)
        j = random.randint(1, 2 * m - 1)
        maze[i, j] = 0

    maze = enforce_borders(maze)
    maze[1, 0] = 0
    maze[-2, -1] = 0
    
    return maze

def generate_maze(difficulty=5, dim=20):
    if difficulty <= 3:
        print("Using DFS algorithm (perfect maze)")
        return create_maze_dfs(dim)
    elif difficulty <= 6:
        extra = (difficulty - 3) * 2
        print("Using Prim's algorithm with extra openings =", extra)
        return create_maze_prims(dim, extra_openings=extra)
    else:
        complexity = (difficulty - 6) * 10
        print("Using Aldous-Broder algorithm with complexity =", complexity)
        return create_maze_aldous_broder(dim, dim, complexity=complexity)

def plot_maze(maze, title=None):
    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap='binary')
    if title:
        plt.title(title)
    plt.axis('off')
    plt.show()