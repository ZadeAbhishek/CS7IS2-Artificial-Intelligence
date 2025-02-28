"""
mdp_policy_solver.py

Implements a Policy Iteration approach to solve the maze as an MDP.
"""

import time
import random
import numpy as np  # Assuming maze is a numpy array

def print_value_function(V, maze):
    """
    Print the value function V as a grid corresponding to the maze.
    For passable cells (maze == 0), prints the value from V.
    For walls (maze != 0), prints 'WALL'.
    """
    for i in range(maze.shape[0]):
        row_vals = []
        for j in range(maze.shape[1]):
            if maze[i, j] == 0:
                # If the cell is passable, get its value.
                val = V.get((i, j), 0)
                row_vals.append(f"{val:6.2f}")
            else:
                row_vals.append(" WALL ")
        print(" ".join(row_vals))
    print("")  # Blank line for readability

def solve_mdp_policy_iteration(maze, start, goal,
                               discount=0.9, theta=0.001):
    """
    Solve the maze using MDP Policy Iteration:
      1. Initialize a random policy for all non-goal states.
      2. Policy Evaluation: Iterate until the value function converges (delta < theta),
         updating V(s) <- R(s, pi(s)) + discount * V(next_state).
      3. Policy Improvement: For each state, choose the action that
         maximizes R(s, a) + discount * V(next_state). If the policy
         doesn't change, the policy is stable.
      4. Extract a path by following the final policy from start to goal.
    
    Reward function:
      - 0 if next state is the goal
      - -1 otherwise

    Args:
        maze (np.ndarray): 2D array of 0s (passable) and 1s (walls).
        start (tuple): (row, col) for start cell (must be passable).
        goal (tuple): (row, col) for goal cell (must be passable).
        discount (float): Discount factor (gamma).
        theta (float): Convergence threshold for policy evaluation.

    Returns:
        path (list): Sequence of (row, col) from start to goal.
        path_length (int): Number of steps in that path.
        runtime (float): Time taken to compute the solution.
    """
    start_time = time.time()

    # Convert start, goal to plain Python ints.
    start = (int(start[0]), int(start[1]))
    goal = (int(goal[0]), int(goal[1]))

    # Gather all passable states.
    states = [(r, c) for r in range(maze.shape[0])
                    for c in range(maze.shape[1]) if maze[r, c] == 0]

    # Ensure start and goal are valid passable states.
    if start not in states:
        raise ValueError(f"Start state {start} is not passable!")
    if goal not in states:
        raise ValueError(f"Goal state {goal} is not passable!")

    # Possible actions: up, down, left, right.
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def reward(s, ns):
        """Reward = 0 if next state is goal, else -1."""
        return 0 if ns == goal else -1

    def safe_ns(s, a):
        """
        Given current state s and action a, compute next state.
        If out of bounds or a wall, remain in s.
        """
        candidate_ns = (s[0] + a[0], s[1] + a[1])
        return candidate_ns if candidate_ns in states else s

    # Initialize value function and a random policy.
    V = {s: 0 for s in states}
    policy = {}
    for s in states:
        if s == goal:
            policy[s] = None  # No action needed at goal.
        else:
            policy[s] = random.choice(actions)

    # --- POLICY ITERATION ---
    policy_stable = False
    policy_iter = 0
    while not policy_stable:
        policy_iter += 1
        print(f"--- Policy Iteration {policy_iter} ---")
        # 1. Policy Evaluation: iterate until the value function converges.
        delta = float('inf')
        eval_iter = 0
        while delta >= theta:
            eval_iter += 1
            delta = 0
            newV = {}
            for s in states:
                if s == goal:
                    newV[s] = 0
                    continue
                a = policy[s]
                ns = safe_ns(s, a)
                r = reward(s, ns)
                newV[s] = r + discount * V[ns]
                delta = max(delta, abs(newV[s] - V[s]))
            V = newV
            print(f"Policy Evaluation Iteration {eval_iter} - Delta: {delta:.6f}")
            print_value_function(V, maze)

        # 2. Policy Improvement
        policy_stable = True
        for s in states:
            if s == goal:
                continue
            old_a = policy[s]
            best_a = None
            best_val = float('-inf')
            for a in actions:
                ns = safe_ns(s, a)
                r = reward(s, ns)
                val = r + discount * V[ns]
                if val > best_val:
                    best_val = val
                    best_a = a

            policy[s] = best_a
            if best_a != old_a:
                policy_stable = False

    # --- EXTRACT PATH (following the final policy) ---
    s = start
    path = [s]
    for _ in range(10000):  # Safety limit
        if s == goal:
            break
        a = policy[s]
        if a is None:
            break
        ns = safe_ns(s, a)
        if ns == s:
            break  # No progress
        s = ns
        path.append(s)

    runtime = time.time() - start_time
    return path, len(path), runtime

if __name__ == "__main__":
    pass