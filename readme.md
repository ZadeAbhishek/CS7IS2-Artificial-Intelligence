# Maze Solving Algorithms - AI Assignment (CS7IS2)

This project is part of the **CS7IS2 Artificial Intelligence** course and involves implementing and evaluating various **maze-solving algorithms** including traditional search methods and **Markov Decision Process (MDP)-based approaches**.

## 📌 Table of Contents
- [Introduction](#introduction)
- [Implemented Algorithms](#implemented-algorithms)
- [Setup Instructions](#setup-instructions)
- [How to Run the Code](#how-to-run-the-code)
- [Contact](#contact)

---

## 📖 Introduction
This project explores different maze-solving techniques, focusing on:
- **Traditional Search Algorithms**: Depth-First Search (DFS), Breadth-First Search (BFS), and A*.
- **MDP-Based Methods**: Policy Iteration and Value Iteration.

The goal is to analyze and compare their efficiency in terms of **runtime, memory usage, and path length**.

## ⚙️ Implemented Algorithms
### 1️⃣ **Traditional Search Algorithms**
- **Depth-First Search (DFS)**: Explores paths deeply before backtracking.
- **Breadth-First Search (BFS)**: Guarantees the shortest path using level-wise traversal.
- **A* Search**: Uses a heuristic (Manhattan distance) to efficiently find an optimal path.

### 2️⃣ **Markov Decision Process (MDP) Methods**
- **MDP Policy Iteration**: Iteratively improves policies based on rewards and transition probabilities.
- **MDP Value Iteration**: Uses Bellman equations to find the optimal value function.


## 🔧 Setup Instructions
### Prerequisites
Ensure you have **Python 3.x** installed along with the following dependencies:
```sh
python -m venv maze_env
source maze_env/bin/activate  # Mac/Linux
maze_env\Scripts\activate     # Windows
```

```sh
pip install numpy matplotlib
```

---

## ▶️ How to Run the Code
Run the main **driver script**:
```sh
python driver.py
```
### Interactive Inputs:
1. **Maze Dimension** (e.g., `20` for a 20×20 maze)
2. **Maze Difficulty** (between `1` to `10`)
3. **Algorithm Selection** (comma-separated list of DFS, BFS, A*, MDP_POLICY, MDP_VALUE)
4. **MDP Parameters** (for Policy and Value Iteration methods)

Example Run:
```sh
Enter maze dimension (number of cells per side): 20
Enter maze difficulty (1-10): 10
Select algorithms to run (separate by commas): DFS, BFS, A*, MDP_POLICY, MDP_VALUE
Enter discount factor for MDP Policy Iteration (e.g., 0.9): 0.9
Enter convergence threshold for MDP Policy Iteration (e.g., 0.001): 0.001
Enter discount factor for MDP Value Iteration (e.g., 0.9): 0.9
Enter convergence threshold for MDP Value Iteration (e.g., 0.001): 0.001
```

Results will be saved in a **timestamped folder inside the `results/` directory**:
```
📂 results_20250302_094347
   ├── algorithm_performance.csv   # CSV file with runtime, path length, memory usage
   ├── performance_comparison.png  # Graph comparing algorithms
   ├── DFS_solution.png            # Visual representation of DFS solution
   ├── BFS_solution.png            # Visual representation of BFS solution
   ├── A*_solution.png             # Visual representation of A* solution
   ├── MDP_POLICY_solution.png     # MDP Policy Iteration path
   ├── MDP_VALUE_solution.png      # MDP Value Iteration path
```

## 📌 Contact
For queries or issues, reach out to **Abhishek Zade** at:
📧 **zabhidoc@gmail.com** or **zadea@tcd.ie**

---

🚀 **Happy Coding & Maze Solving!** 🏆

