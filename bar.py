import matplotlib.pyplot as plt
import numpy as np
import os

data = {
    "10x10": {
        "diff3": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00216, 0.00016, 0.00018, 0.03034, 0.01085],
            "path": [63, 63, 63, 63, 63],
            "memory": [1008, 16, 48, 2688, 80]
        },
        "diff6": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00040, 0.00031, 0.00022, 0.02961, 0.00722],
            "path": [51, 39, 39, 39, 39],
            "memory": [304, 16, 48, 2224, 80]
        },
        "diff10": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00031, 0.00033, 0.00032, 0.03174, 0.00891],
            "path": [53, 47, 47, 47, 47],
            "memory": [640, 32, 48, 2592, 96]
        }
    },
    "30x30": {
        "diff3": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00242, 0.00214, 0.00270, 0.28736, 0.94559],
            "path": [631, 631, 631, 631, 631],
            "memory": [544, 320, 208, 4176, -31104]
        },
        "diff6": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00178, 0.00204, 0.00327, 0.21013, 0.36687],
            "path": [225, 199, 199, 199, 199],
            "memory": [3552, 272, 272, 1904, 464]
        },
        "diff10": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00376, 0.00179, 0.00077, 0.13086, 0.18653],
            "path": [127, 127, 127, 127, 127],
            "memory": [816, 64, 176, 3696, 528]
        }
    },
    "60x60": {
        "diff3": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00705, 0.00500, 0.00803, 3.17464, 9.56316],
            "path": [1459, 1459, 1459, 1459, 1459],
            "memory": [768, 336, 416, -14672, -66016]
        },
        "diff6": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00794, 0.01108, 0.00746, 1.81709, 1.86494],
            "path": [283, 283, 283, 283, 283],
            "memory": [1056, 960, 1104, -9344, 3792]
        },
        "diff10": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00677, 0.01161, 0.01203, 2.10212, 3.24705],
            "path": [631, 475, 475, 475, 475],
            "memory": [5936, 1424, 864, -35456, -46384]
        }
    },
    "100x100": {
        "diff3": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.05490, 0.09579, 0.17272, 21.08331, 79.38281],
            "path": [4759, 4759, 4759, 4759, 4759],
            "memory": [6096, 992, 2240, -44176, -56848]
        },
        "diff6": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.00807, 0.03108, 0.01792, 6.93101, 10.29167],
            "path": [439, 439, 439, 439, 439],
            "memory": [1072, 3408, 2848, -42080, -3264]
        },
        "diff10": {
            "algorithms": ['DFS', 'BFS', 'A*', 'MDP_POLICY', 'MDP_VALUE'],
            "runtime": [0.04979, 0.02647, 0.03606, 11.30529, 29.57764],
            "path": [719, 703, 703, 703, 703],
            "memory": [11632, 1136, 1104, -60032, -10096]
        }
    }
}

# Create an output directory for the figures
output_dir = "performance_figures"
os.makedirs(output_dir, exist_ok=True)

# Loop over each grid size and difficulty level
for grid, diff_dict in data.items():
    for diff, metrics in diff_dict.items():
        algorithms = metrics["algorithms"]
        runtime = metrics["runtime"]
        path_length = metrics["path"]
        memory = metrics["memory"]
        
        x = np.arange(len(algorithms))
        width = 0.5
        
        # Create a figure with three subplots
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        fig.suptitle(f"Performance Metrics for {grid} Maze, Difficulty = {diff[-1]}", fontsize=16)
        
        # Runtime subplot
        axs[0].bar(x, runtime, width, color='skyblue')
        axs[0].set_title('Runtime (sec)')
        axs[0].set_xticks(x)
        axs[0].set_xticklabels(algorithms)
        axs[0].set_ylabel('Seconds')
        
        # Path Length subplot
        axs[1].bar(x, path_length, width, color='lightgreen')
        axs[1].set_title('Path Length')
        axs[1].set_xticks(x)
        axs[1].set_xticklabels(algorithms)
        axs[1].set_ylabel('Number of Cells')
        
        # Memory Usage subplot
        axs[2].bar(x, memory, width, color='salmon')
        axs[2].set_title('Memory Usage (kB)')
        axs[2].set_xticks(x)
        axs[2].set_xticklabels(algorithms)
        axs[2].set_ylabel('Kilobytes')
        
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        
        # Save the figure with a unique name based on grid and difficulty
        filename = f"{grid}_{diff}_performance.png"
        plt.savefig(os.path.join(output_dir, filename))
        plt.close(fig)

print("Bar diagrams have been saved in the folder:", output_dir)