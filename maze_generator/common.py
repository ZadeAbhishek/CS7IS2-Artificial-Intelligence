import matplotlib.pyplot as plt

def get_neighbors(cell, maze):
    r, c = cell
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < maze.shape[0] and 0 <= nc < maze.shape[1] and maze[nr, nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

def overlay_path_on_maze(maze, path, algorithm_name, steps, runtime, filename):
    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap='binary')
    if path:
        rows = [p[0] for p in path]
        cols = [p[1] for p in path]
        plt.plot(cols, rows, color='red', linewidth=2, label='Solution Path')
    plt.title(f"{algorithm_name}\nSteps: {steps} | Runtime: {runtime:.4f} sec")
    plt.axis('off')
    plt.legend()
    plt.savefig(filename)
    plt.close()