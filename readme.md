# Maze Solver with Traditional and MDP-Based Algorithms

## Introduction
This project implements various maze-solving algorithms to evaluate their efficiency, path optimality, and computational resource usage. The implemented algorithms include:
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **A* Search (A-star)**
- **Markov Decision Process (MDP) Policy Iteration**
- **Markov Decision Process (MDP) Value Iteration**

Additionally, the project includes a **maze generator** that produces mazes of varying sizes and difficulties using different algorithms like **DFS, Prim's Algorithm, and Aldous-Broder Algorithm**.

---

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed along with the following dependencies:

```sh
pip install numpy matplotlib
```


## How to Run
To execute the maze solver, run the **driver.py** script and provide the necessary inputs when prompted.

```sh
python driver.py
```

### Example Execution
```
Enter maze dimension (number of cells per side): 20
Enter maze difficulty (1-10): 10
Using Aldous-Broder algorithm with complexity = 40

Select algorithms to run (separate by commas):
Options: DFS, BFS, A*, MDP_POLICY, MDP_VALUE
Enter choices: DFS, BFS, A*, MDP_POLICY, MDP_VALUE
Enter discount factor for MDP Policy Iteration (e.g., 0.9): 0.9
Enter convergence threshold for MDP Policy Iteration (e.g., 0.001): 0.001
Enter discount factor for MDP Value Iteration (e.g., 0.9): 0.9
Enter convergence threshold for MDP Value Iteration (e.g., 0.001): 0.001
```

### Outputs
After execution, results will be saved in the **results/** directory:
- **Performance Data**: `algorithm_performance.csv`
- **Maze Solutions**: `[Algorithm]_solution.png`
- **Performance Comparison Graph**: `performance_comparison.png`

---

## Algorithm Descriptions

### 1. Depth-First Search (DFS)
- Explores as far as possible along each branch before backtracking.
- Uses a **stack-based approach**.
- May not always return the shortest path but is efficient in memory.

### 2. Breadth-First Search (BFS)
- Explores all nodes at the present depth before moving deeper.
- Guarantees the **shortest path**.
- Uses a **queue-based approach**, making it more memory-intensive.

### 3. A* Search
- Uses a heuristic function to estimate the cost from the current node to the goal.
- Balances cost-to-come and estimated cost-to-go (`f(n) = g(n) + h(n)`).
- Typically provides optimal and efficient solutions.

### 4. MDP Policy Iteration
- Models the maze as a **Markov Decision Process** (MDP).
- Iteratively evaluates and improves the policy until convergence.
- Computes the **expected long-term reward** for each state.

### 5. MDP Value Iteration
- Uses **Bellman updates** to compute optimal state values.
- Selects actions that maximize discounted future rewards.
- More computationally expensive than traditional search algorithms.

---

## Performance Comparison
A bar graph comparing algorithm performance (runtime, path length, and memory usage) is generated and saved as **performance_comparison.png**.

### General Observations:
- **BFS and A***: Fast and provide shortest path guarantees.
- **DFS**: Efficient in memory but may generate longer paths.
- **MDP-Based Methods**: Optimal for decision-making but expensive in terms of computational resources.


## License
This project is for educational purposes and free for use.

---

## Contact
For queries or issues, reach out to **Abhishek Zade**.

