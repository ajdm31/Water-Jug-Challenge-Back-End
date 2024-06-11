from collections import deque

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def water_jug_solver(jug1_capacity, jug2_capacity, target):
    if target % gcd(jug1_capacity, jug2_capacity) != 0:
        return {"solution": "No solution possible"}

    visited = set()
    queue = deque([(0, 0)])
    steps = []

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        steps.append((jug1, jug2))

        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            return format_solution(steps)

        # Fill jug1
        queue.append((jug1_capacity, jug2))

        # Fill jug2
        queue.append((jug1, jug2_capacity))

        # Empty jug1
        queue.append((0, jug2))

        # Empty jug2
        queue.append((jug1, 0))

        # Transfer jug1 -> jug2
        transfer = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - transfer, jug2 + transfer))

        # Transfer jug2 -> jug1
        transfer = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + transfer, jug2 - transfer))

    return {"solution": "No solution possible"}

def format_solution(steps):
    result = []
    for i, (jug1, jug2) in enumerate(steps, 1):
        action = determine_action(steps, i)
        result.append({
            "step": i,
            "bucketX": jug1,
            "bucketY": jug2,
            "action": action
        })
    result[-1]["status"] = "Solved"
    return {"solution": result}

def determine_action(steps, i):
    if i == 1:
        return "Initial state"
    jug1_prev, jug2_prev = steps[i-2]
    jug1_curr, jug2_curr = steps[i-1]

    if jug1_curr > jug1_prev:
        return "Fill bucket X"
    elif jug2_curr > jug2_prev:
        return "Fill bucket Y"
    elif jug1_curr < jug1_prev:
        return "Empty bucket X"
    elif jug2_curr < jug2_prev:
        return "Empty bucket Y"
    elif jug1_curr == jug1_prev:
        return "Transfer from bucket Y to X"
    else:
        return "Transfer from bucket X to Y"
