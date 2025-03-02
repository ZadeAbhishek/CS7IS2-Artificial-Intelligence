import os
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from alogrithms.dfs_solver import solve_dfs
from alogrithms.bfs_solver import solve_bfs
from alogrithms.astar_solver import solve_astar
from alogrithms.mdp_policy_solver import solve_mdp_policy_iteration
from alogrithms.mdp_value_solver import solve_mdp_value_iteration
from maze_generator.maze_generator import generate_maze


def create_results_directory():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    results_dir = Path(f"results_{timestamp}")
    results_dir.mkdir(parents=True, exist_ok=True)
    return results_dir

def save_maze_solution(maze, path, algorithm, results_dir):
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap="gray_r")

    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker="o", color="red", markersize=4, linewidth=2, label=algorithm)

    plt.title(f"Solution using {algorithm}")
    plt.legend()
    plt.axis("off")
    
    image_path = results_dir / f"{algorithm}_solution.png"
    plt.savefig(image_path)
    plt.close()

def save_results_to_csv(results, results_dir):
    csv_filename = results_dir / "algorithm_performance.csv"
    fieldnames = ["Algorithm", "Path Length", "Runtime (sec)", "Memory (kB)", "Discount", "Theta"]
    
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for alg, data in results.items():
            writer.writerow({
                "Algorithm": alg,
                "Path Length": data["Path Length"],
                "Runtime (sec)": data["Runtime"],
                "Memory (kB)": data["Memory"],
                "Discount": data.get("Discount", "N/A"),
                "Theta": data.get("Theta", "N/A"),
            })
    print(f"Performance data saved in {csv_filename}")

def plot_performance_comparison(results, results_dir):
    algorithms = list(results.keys())
    runtimes = [results[alg]["Runtime"] for alg in algorithms]
    path_lengths = [results[alg]["Path Length"] for alg in algorithms]
    memories = [results[alg]["Memory"] for alg in algorithms]

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.bar(algorithms, runtimes, color="skyblue")
    plt.ylabel("Runtime (seconds)")
    plt.title("Algorithm Runtime Comparison")

    plt.subplot(1, 3, 2)
    plt.bar(algorithms, path_lengths, color="salmon")
    plt.ylabel("Path Length (steps)")
    plt.title("Algorithm Path Length Comparison")

    plt.subplot(1, 3, 3)
    plt.bar(algorithms, memories, color="lightgreen")
    plt.ylabel("Memory (kB)")
    plt.title("Algorithm Memory Usage Comparison")

    plt.suptitle("Maze Solver Performance Comparison")
    performance_image_path = results_dir / "performance_comparison.png"
    plt.savefig(performance_image_path)
    plt.close()
    print(f"Performance comparison graph saved at {performance_image_path}")


def analyze_algorithms(maze, start, goal, algorithms, solve_functions, params):
    results_dir = create_results_directory()
    results = {}

    for algorithm, solve_func in solve_functions.items():
        if algorithm in algorithms:
            print(f"Running {algorithm}...")

            mem_before = os.popen("ps -o rss= -p " + str(os.getpid())).read().strip()
            path, steps, runtime = solve_func(maze, start, goal, **params.get(algorithm, {}))
            mem_after = os.popen("ps -o rss= -p " + str(os.getpid())).read().strip()
            
            mem_usage = int(mem_after) - int(mem_before)
            results[algorithm] = {
                "Path Length": steps,
                "Runtime": runtime,
                "Memory": mem_usage,
                **params.get(algorithm, {}),
            }

            save_maze_solution(maze, path, algorithm, results_dir)

    save_results_to_csv(results, results_dir)
    plot_performance_comparison(results, results_dir)

    return results

def main():
    dim = int(input("Enter maze dimension (number of cells per side): "))
    difficulty = int(input("Enter maze difficulty (1-10): "))

    maze = generate_maze(difficulty=difficulty, dim=dim)
    start = (1, 0)
    goal = (maze.shape[0]-2, maze.shape[1]-1)

    print("\nSelect algorithms to run (separate by commas):")
    print("Options: DFS, BFS, A*, MDP_POLICY, MDP_VALUE")
    selected_algorithms = input("Enter choices: ").upper().split(",")

    selected_algorithms = [alg.strip() for alg in selected_algorithms]
    valid_algorithms = {"DFS", "BFS", "A*", "MDP_POLICY", "MDP_VALUE"}
    selected_algorithms = [alg for alg in selected_algorithms if alg in valid_algorithms]

    if not selected_algorithms:
        print("No valid algorithms selected. Exiting.")
        return
    
    solve_functions = {
        "DFS": solve_dfs,
        "BFS": solve_bfs,
        "A*": solve_astar,
        "MDP_POLICY": solve_mdp_policy_iteration,
        "MDP_VALUE": solve_mdp_value_iteration,
    }

    mdp_params = {}
    if "MDP_POLICY" in selected_algorithms:
        mdp_params["MDP_POLICY"] = {
            "discount": float(input("Enter discount factor for MDP Policy Iteration (e.g., 0.9): ")),
            "theta": float(input("Enter convergence threshold for MDP Policy Iteration (e.g., 0.001): ")),
        }
    if "MDP_VALUE" in selected_algorithms:
        mdp_params["MDP_VALUE"] = {
            "discount": float(input("Enter discount factor for MDP Value Iteration (e.g., 0.9): ")),
            "theta": float(input("Enter convergence threshold for MDP Value Iteration (e.g., 0.001): ")),
        }

    analyze_algorithms(maze, start, goal, selected_algorithms, solve_functions, mdp_params)

if __name__ == "__main__":
    main()