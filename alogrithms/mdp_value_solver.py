import time

def solve_mdp_value_iteration(maze, start, goal, discount=0.99, theta=0.001):
    start_time = time.time()

    # Ensure start and goal are integer tuples
    start = (int(start[0]), int(start[1]))
    goal = (int(goal[0]), int(goal[1]))

    rows, cols = maze.shape
    # Use a set for fast membership checking of passable states.
    states = {(r, c) for r in range(rows) for c in range(cols) if maze[r, c] == 0}

    if start not in states or goal not in states:
        raise ValueError("Start or Goal state is not passable!")

    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Precompute transitions for each state and each action.
    # For a given state, if an action leads out of the passable region,
    # the state remains unchanged.
    transitions = {}
    for s in states:
        r, c = s
        transitions[s] = {}
        for a in actions:
            ns = (r + a[0], c + a[1])
            if ns not in states:
                ns = s
            transitions[s][a] = ns

    # Initialize the value function to 0 for all states.
    V = {s: 0.0 for s in states}

    # VALUE ITERATION LOOP
    while True:
        delta = 0.0
        newV = {}
        for s in states:
            if s == goal:
                newV[s] = 0.0  # The goal state's value remains 0.
                continue

            best_val = float('-inf')
            # Check all actions for state s
            for a in actions:
                ns = transitions[s][a]
                # Inline reward: +1 if next state is goal, -0.01 otherwise.
                rwd = 1.0 if ns == goal else -0.01
                val = rwd + discount * V[ns]
                best_val = max(best_val, val)

            newV[s] = best_val
            delta = max(delta, abs(newV[s] - V[s]))
        V = newV
        if delta < theta:
            break

    # EXTRACT PATH USING A GREEDY POLICY
    s = start
    path = [s]
    while s != goal:
        best_val = float('-inf')
        best_ns = s
        for a in actions:
            ns = transitions[s][a]
            rwd = 1.0 if ns == goal else -0.01
            val = rwd + discount * V[ns]
            if val > best_val:
                best_val = val
                best_ns = ns
        if best_ns == s:  # No further progress can be made
            break
        s = best_ns
        path.append(s)

    runtime = time.time() - start_time
    return path, len(path), runtime
