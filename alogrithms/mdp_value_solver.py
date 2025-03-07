import time

def solve_mdp_value_iteration(maze, start, goal, discount=0.99, theta=0.001):
    start_time = time.time()

    start = (int(start[0]), int(start[1]))
    goal = (int(goal[0]), int(goal[1]))

    rows, cols = maze.shape
    states = {(r, c) for r in range(rows) for c in range(cols) if maze[r, c] == 0}

    if start not in states or goal not in states:
        raise ValueError("Start or Goal state is not passable!")

    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    transitions = {}
    for s in states:
        r, c = s
        transitions[s] = {}
        for a in actions:
            ns = (r + a[0], c + a[1])
            if ns not in states:
                ns = s
            transitions[s][a] = ns
            
    V = {s: 0.0 for s in states}

    while True:
        delta = 0.0
        newV = {}
        for s in states:
            if s == goal:
                newV[s] = 0.0
                continue

            best_val = float('-inf')
            for a in actions:
                ns = transitions[s][a]
                rwd = 1.0 if ns == goal else -0.01
                val = rwd + discount * V[ns]
                best_val = max(best_val, val)

            newV[s] = best_val
            delta = max(delta, abs(newV[s] - V[s]))
        V = newV
        if delta < theta:
            break

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
        if best_ns == s:
            break
        s = best_ns
        path.append(s)

    runtime = time.time() - start_time
    return path, len(path), runtime
