import time
import numpy as np

def solve_mdp_policy_iteration(maze, start, goal, discount=0.9, theta=0.001):
    start_time = time.time()
    rows, cols = maze.shape
    passable = (maze == 0)
    
    r_idx, c_idx = np.indices((rows, cols))

    actions = np.array([[-1, 0],
                        [ 1, 0],
                        [ 0, -1],
                        [ 0,  1]])
    num_actions = actions.shape[0]
    

    V = np.zeros((rows, cols))
    policy = -1 * np.ones((rows, cols), dtype=int)
    random_policy = np.random.randint(0, num_actions, size=(rows, cols))
    mask = passable.copy()
    mask[goal] = False
    policy[mask] = random_policy[mask]
    
    def safe_next_state(a_idx):
        dr, dc = actions[a_idx]
        cand_r = r_idx + dr
        cand_c = c_idx + dc
        in_bounds = (cand_r >= 0) & (cand_r < rows) & (cand_c >= 0) & (cand_c < cols)
        valid = np.zeros_like(in_bounds, dtype=bool)
        valid[in_bounds] = passable[cand_r[in_bounds], cand_c[in_bounds]]
        next_r = np.where(valid, cand_r, r_idx)
        next_c = np.where(valid, cand_c, c_idx)
        return next_r, next_c


    cand_r = np.empty((num_actions, rows, cols), dtype=int)
    cand_c = np.empty((num_actions, rows, cols), dtype=int)
    for a in range(num_actions):
        cand_r[a], cand_c[a] = safe_next_state(a)
    
    def compute_candidate_values():
        reward = np.where((cand_r == goal[0]) & (cand_c == goal[1]), 0, -1)
        candidate_vals = reward + discount * V[cand_r, cand_c]
        return candidate_vals
    
    policy_stable = False
    iteration = 0
    while not policy_stable:
        iteration += 1
        while True:
            candidate_vals = compute_candidate_values()
            update_mask = (policy != -1)
            V_new = V.copy()
            idx = np.where(update_mask)
            V_new[idx] = candidate_vals[policy[idx], idx[0], idx[1]]
            delta = np.max(np.abs(V_new - V))
            V = V_new
            if delta < theta:
                break

        candidate_vals = compute_candidate_values()
        best_actions = np.argmax(candidate_vals, axis=0)
        new_policy = policy.copy()
        new_policy[update_mask] = best_actions[update_mask]
        if np.all(new_policy[update_mask] == policy[update_mask]):
            policy_stable = True
        else:
            policy = new_policy

    print(f"Policy Iteration converged after {iteration} iterations.")

    path = [start]
    current = start
    for _ in range(10000):
        if current == goal:
            break
        r, c = current
        a = policy[r, c]
        if a == -1:
            print("No valid action found at state", current, "stopping path extraction.")
            break
        next_r, next_c = safe_next_state(a)
        next_state = (next_r[r, c], next_c[r, c])
        if next_state == current:
            print("Stuck in local optimum at", current, "stopping path extraction.")
            break
        current = next_state
        path.append(current)

    runtime = time.time() - start_time
    return path, len(path), runtime
