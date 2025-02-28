import matplotlib.pyplot as plt
import csv
import maze_generator as mg
from dfs_solver import solve_dfs
from bfs_solver import solve_bfs
from astar_solver import solve_astar
from mdp_policy_solver import solve_mdp_policy_iteration  # Policy Iteration version
from mdp_value_solver import solve_mdp_value_iteration
from common import overlay_path_on_maze
import resource  # To measure memory usage

def get_memory_usage():
    # Returns memory usage in kilobytes (peak usage of the process).
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

def main():
    # Prompt for maze parameters.
    dim = int(input("Enter maze dimension (number of cells per side): "))
    difficulty = int(input("Enter maze difficulty (1-10): "))
    
    # Generate maze and define start and goal positions.
    while True:
        maze = mg.generate_maze(difficulty=difficulty, dim=dim)
        start = (1, 0)  # Entry should match maze_generator (e.g., (1,0))
        goal = (maze.shape[0]-2, maze.shape[1]-1)
        
        # Verify using BFS if there is a valid path.
        path, steps, runtime = solve_bfs(maze, start, goal)
        if path and path[-1] == goal:
            print("Valid maze generated with a path from start to goal.")
            break
        else:
            print("No valid path found in generated maze. Generating a new maze...")
    
    # Prompt for solver selection.
    print("\nSelect solver algorithms to use (separate by comma):")
    print("Options: DFS, BFS, A*, MDP_Policy, MDP_Value")
    selected = input("Enter your choices: ")
    choices = [s.strip().upper() for s in selected.split(",")]
    
    # Separate parameters for MDP Policy Iteration and Value Iteration.
    mdp_policy_params = {}
    mdp_value_params = {}

    if "MDP_POLICY" in choices:
        mdp_policy_params['discount'] = float(input("Enter discount factor for MDP Policy Iteration (e.g. 0.9): "))
        mdp_policy_params['theta'] = float(input("Enter convergence threshold for MDP Policy Iteration (e.g. 0.001): "))

    if "MDP_VALUE" in choices:
        mdp_value_params['discount'] = float(input("Enter discount factor for MDP Value Iteration (e.g. 0.9): "))
        mdp_value_params['theta'] = float(input("Enter convergence threshold for MDP Value Iteration (e.g. 0.001): "))

    results = {}
    
    # Run each solver and measure runtime, path length, and memory usage.
    if "DFS" in choices:
        print("Running DFS...")
        mem_before = get_memory_usage()
        path, steps, runtime = solve_dfs(maze, start, goal)
        mem_after = get_memory_usage()
        mem_usage = mem_after - mem_before
        results["DFS"] = {"Path Length": steps, "Runtime": runtime, "Memory": mem_usage}
        overlay_path_on_maze(maze, path, "DFS", steps, runtime, "dfs_solution.png")
        
    if "BFS" in choices:
        print("Running BFS...")
        mem_before = get_memory_usage()
        path, steps, runtime = solve_bfs(maze, start, goal)
        mem_after = get_memory_usage()
        mem_usage = mem_after - mem_before
        results["BFS"] = {"Path Length": steps, "Runtime": runtime, "Memory": mem_usage}
        overlay_path_on_maze(maze, path, "BFS", steps, runtime, "bfs_solution.png")
        
    if "A*" in choices or "ASTAR" in choices:
        print("Running A*...")
        mem_before = get_memory_usage()
        path, steps, runtime = solve_astar(maze, start, goal)
        mem_after = get_memory_usage()
        mem_usage = mem_after - mem_before
        results["A*"] = {"Path Length": steps, "Runtime": runtime, "Memory": mem_usage}
        overlay_path_on_maze(maze, path, "A*", steps, runtime, "astar_solution.png")
        
    if "MDP_POLICY" in choices:
        print("Running MDP Policy Iteration...")
        mem_before = get_memory_usage()
        path, steps, runtime = solve_mdp_policy_iteration(
            maze, start, goal,
            discount=mdp_policy_params['discount'],
            theta=mdp_policy_params['theta']
        )
        mem_after = get_memory_usage()
        mem_usage = mem_after - mem_before
        results["MDP_Policy"] = {"Path Length": steps, "Runtime": runtime, "Memory": mem_usage}
        overlay_path_on_maze(maze, path, "MDP Policy Iteration", steps, runtime, "mdp_policy_solution.png")
        
    if "MDP_VALUE" in choices:
        print("Running MDP Value Iteration...")
        mem_before = get_memory_usage()
        path, steps, runtime = solve_mdp_value_iteration(
            maze, start, goal,
            discount=mdp_value_params['discount'],
            theta=mdp_value_params['theta']
        )
        mem_after = get_memory_usage()
        mem_usage = mem_after - mem_before
        results["MDP_Value"] = {"Path Length": steps, "Runtime": runtime, "Memory": mem_usage}
        overlay_path_on_maze(maze, path, "MDP Value Iteration", steps, runtime, "mdp_value_solution.png")
    
    # Generate performance comparison graph.
    algorithms = list(results.keys())
    runtimes = [results[alg]["Runtime"] for alg in algorithms]
    path_lengths = [results[alg]["Path Length"] for alg in algorithms]
    memories = [results[alg]["Memory"] for alg in algorithms]
    
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.bar(algorithms, runtimes, color='skyblue')
    plt.ylabel("Runtime (sec)")
    plt.title("Solver Runtime Comparison")
    
    plt.subplot(1, 3, 2)
    plt.bar(algorithms, path_lengths, color='salmon')
    plt.ylabel("Path Length (steps)")
    plt.title("Solver Path Length Comparison")
    
    plt.subplot(1, 3, 3)
    plt.bar(algorithms, memories, color='lightgreen')
    plt.ylabel("Memory (kB)")
    plt.title("Solver Memory Usage Comparison")
    
    plt.suptitle("Maze Solver Performance Comparison")
    plt.savefig("performance_comparison.png")
    plt.close()
    
    # Generate CSV performance report.
    csv_filename = "solver_performance.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["Algorithm", "Path Length", "Runtime (sec)", "Memory (kB)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for alg in algorithms:
            writer.writerow({
                "Algorithm": alg,
                "Path Length": results[alg]["Path Length"],
                "Runtime (sec)": results[alg]["Runtime"],
                "Memory (kB)": results[alg]["Memory"]
            })
    print(f"Performance comparison saved as {csv_filename} and performance_comparison.png.")

if __name__ == "__main__":
    main()