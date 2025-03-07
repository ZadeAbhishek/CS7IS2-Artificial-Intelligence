import matplotlib.pyplot as plt

# Define grid sizes (n x n)
grid_sizes = [10, 30, 60, 100]

# Data for difficulty = 3 (example values extracted from the results)
# Runtime in seconds
dfs_runtime = [0.00216, 0.00242, 0.00705, 0.05490]
bfs_runtime = [0.00016, 0.00214, 0.00500, 0.09579]
astar_runtime = [0.00018, 0.00270, 0.00803, 0.17272]
mdp_policy_runtime = [0.03034, 0.28736, 3.17464, 21.08331]
mdp_value_runtime = [0.01085, 0.94559, 9.56316, 79.38281]

# Path Length
dfs_path_length = [63, 631, 1459, 4759]
bfs_path_length = [63, 631, 1459, 4759]
astar_path_length = [63, 631, 1459, 4759]
mdp_policy_path_length = [63, 631, 1459, 4759]
mdp_value_path_length = [63, 631, 1459, 4759]

# Memory usage in kB (example values)
dfs_memory = [1008, 544, 768, 6096]
bfs_memory = [16, 320, 336, 992]
astar_memory = [48, 208, 416, 2240]
mdp_policy_memory = [2688, 4176, -14672, -44176]
mdp_value_memory = [80, -31104, -66016, -56848]

# Create a figure with three subplots
plt.figure(figsize=(15, 5))

# Plot Runtime Comparison
plt.subplot(1, 3, 1)
plt.plot(grid_sizes, dfs_runtime, marker='o', label='DFS')
plt.plot(grid_sizes, bfs_runtime, marker='o', label='BFS')
plt.plot(grid_sizes, astar_runtime, marker='o', label='A*')
plt.plot(grid_sizes, mdp_policy_runtime, marker='o', label='MDP Policy')
plt.plot(grid_sizes, mdp_value_runtime, marker='o', label='MDP Value')
plt.xlabel('Grid Size (n x n)')
plt.ylabel('Runtime (sec)')
plt.title('Runtime Comparison (Difficulty = 3)')
plt.legend()
plt.grid(True)

# Plot Path Length Comparison
plt.subplot(1, 3, 2)
plt.plot(grid_sizes, dfs_path_length, marker='o', label='DFS')
plt.plot(grid_sizes, bfs_path_length, marker='o', label='BFS')
plt.plot(grid_sizes, astar_path_length, marker='o', label='A*')
plt.plot(grid_sizes, mdp_policy_path_length, marker='o', label='MDP Policy')
plt.plot(grid_sizes, mdp_value_path_length, marker='o', label='MDP Value')
plt.xlabel('Grid Size (n x n)')
plt.ylabel('Path Length')
plt.title('Path Length Comparison (Difficulty = 3)')
plt.legend()
plt.grid(True)

# Plot Memory Usage Comparison
plt.subplot(1, 3, 3)
plt.plot(grid_sizes, dfs_memory, marker='o', label='DFS')
plt.plot(grid_sizes, bfs_memory, marker='o', label='BFS')
plt.plot(grid_sizes, astar_memory, marker='o', label='A*')
plt.plot(grid_sizes, mdp_policy_memory, marker='o', label='MDP Policy')
plt.plot(grid_sizes, mdp_value_memory, marker='o', label='MDP Value')
plt.xlabel('Grid Size (n x n)')
plt.ylabel('Memory Usage (kB)')
plt.title('Memory Usage Comparison (Difficulty = 3)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()