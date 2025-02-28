"""
mdp_value_solver.py

Implements a Value Iteration approach to solve the maze as an MDP with
an adjusted reward structure to incentivize reaching the goal.
"""

import time

def solve_mdp_value_iteration(maze, start, goal, discount=0.99, theta=0.001):
    """
    Solve the maze using a Value Iteration approach that dynamically converges:
      1. Initialize V(s) = 0 for all passable states.
      2. Update iteratively until max delta < theta:
           V(s) = max_{a in actions} [ R(s, ns) + discount * V(ns) ]
      3. Extract a path by choosing the action that maximizes
         R(s, ns) + discount * V(ns), stopping early if stable.

    Reward function:
      - +1.0 if the next state is the goal
      - -0.01 otherwise (small penalty per step)

    Args:
        maze (np.ndarray): 2D array of 0s (passable) and 1s (walls).
        start (tuple): (row, col) for the start cell.
        goal (tuple): (row, col) for the goal cell.
        discount (float): Discount factor (gamma). Default 0.99.
        theta (float): Convergence threshold. Default 0.001.

    Returns:
        path (list): Sequence of (row, col) from start to goal.
        path_length (int): Number of steps in the path.
        runtime (float): Time taken to compute the solution.
    """
    start_time = time.time()

    start = (int(start[0]), int(start[1]))
    goal = (int(goal[0]), int(goal[1]))

    states = [(r, c) for r in range(maze.shape[0])
                    for c in range(maze.shape[1]) if maze[r, c] == 0]

    if start not in states or goal not in states:
        raise ValueError("Start or Goal state is not passable!")

    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def reward(s, ns):
        return 1.0 if ns == goal else -0.01

    def safe_ns(s, ns):
        return ns if ns in states else s

    V = {s: 0.0 for s in states}

    # --- VALUE ITERATION (Runs until convergence) ---
    iteration = 0
    while True:
        delta = 0.0
        newV = {}

        for s in states:
            if s == goal:
                newV[s] = 0.0  # Goal state remains at 0
                continue

            best_val = float('-inf')
            for a in actions:
                candidate_ns = safe_ns(s, (s[0] + a[0], s[1] + a[1]))
                val = reward(s, candidate_ns) + discount * V[candidate_ns]
                best_val = max(best_val, val)

            newV[s] = best_val
            delta = max(delta, abs(newV[s] - V[s]))

        V = newV
        iteration += 1

        # Converged when change is below theta
        if delta < theta:
            break

    # --- EXTRACT PATH (Greedy Policy) ---
    s = start
    path = [s]
    while s != goal:
        best_val = float('-inf')
        best_ns = s

        for a in actions:
            candidate_ns = safe_ns(s, (s[0] + a[0], s[1] + a[1]))
            val = reward(s, candidate_ns) + discount * V[candidate_ns]
            if val > best_val:
                best_val = val
                best_ns = candidate_ns

        if best_ns == s:
            break  # No better move available

        s = best_ns
        path.append(s)

    runtime = time.time() - start_time
    return path, len(path), runtime

if __name__ == "__main__":
    pass