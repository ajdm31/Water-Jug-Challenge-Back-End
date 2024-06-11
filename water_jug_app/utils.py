from collections import deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def water_jug_solver(x, y, z):
    if z > max(x, y) or z % gcd(x, y) != 0:
        return {"solution": "No solution possible"}

    # Breadth-First Search
    queue = deque([(0, 0)])  # starting state (0, 0)
    visited = set([(0, 0)])
    parent_map = {}
    solution = []
    max_depth = 10000  # Limiting depth to prevent memory overflow

    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == z or cur_y == z:
            # backtrack to find the solution path
            while (cur_x, cur_y) in parent_map:
                action, (prev_x, prev_y) = parent_map[(cur_x, cur_y)]
                solution.append({"bucketX": cur_x, "bucketY": cur_y, "action": action})
                cur_x, cur_y = prev_x, prev_y
            solution.append({"bucketX": 0, "bucketY": 0, "action": "Start"})
            solution.reverse()
            solution[-1]["status"] = "Solved"
            return {"solution": solution}

        # Possible actions
        states = [
            (x, cur_y, "Fill bucket X"),
            (cur_x, y, "Fill bucket Y"),
            (0, cur_y, "Empty bucket X"),
            (cur_x, 0, "Empty bucket Y"),
            (cur_x - min(cur_x, y - cur_y), cur_y + min(cur_x, y - cur_y), "Transfer from bucket X to Y"),
            (cur_x + min(cur_y, x - cur_x), cur_y - min(cur_y, x - cur_x), "Transfer from bucket Y to X")
        ]

        for next_x, next_y, action in states:
            if (next_x, next_y) not in visited and len(visited) < max_depth:
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                parent_map[(next_x, next_y)] = (action, (cur_x, cur_y))

    return {"solution": "No solution possible"}
