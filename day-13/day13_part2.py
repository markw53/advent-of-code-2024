from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def solve_diophantine(a, b, c):
    g, x0, y0 = extended_gcd(a, b)
    if c % g != 0:
        return None  # No solution
    x0 *= c // g
    y0 *= c // g
    return g, x0, y0

def find_minimum_tokens(machines):
    total_prizes = 0
    total_cost = 0

    for machine in machines:
        A_x, A_y = machine['A']
        B_x, B_y = machine['B']
        Prize_x, Prize_y = machine['Prize']
        
        # Solve for X
        solution_x = solve_diophantine(A_x, B_x, Prize_x)
        # Solve for Y
        solution_y = solve_diophantine(A_y, B_y, Prize_y)

        if solution_x is None or solution_y is None:
            continue  # No solution for this machine

        g_x, x0_x, y0_x = solution_x
        g_y, x0_y, y0_y = solution_y

        # Check if the solutions can be made consistent
        if g_x != g_y:
            continue  # Inconsistent solutions

        # Calculate the minimum cost
        # We need to find a common solution (n_A, n_B) that satisfies both equations
        # This involves finding a linear combination of the solutions
        # For simplicity, we can iterate over a range to find the minimum cost
        min_cost = float('inf')
        for k in range(-1000, 1000):  # Arbitrary range to find a feasible solution
            n_A = x0_x + k * (B_x // g_x)
            n_B = y0_x - k * (A_x // g_x)
            if n_A >= 0 and n_B >= 0:
                cost = 3 * n_A + 1 * n_B
                if cost < min_cost:
                    min_cost = cost

        if min_cost < float('inf'):
            total_prizes += 1
            total_cost += min_cost

    return total_prizes, total_cost

def parse_input(filename):
    machines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip() == "":
                i += 1
                continue

            a_line = lines[i].strip()
            b_line = lines[i+1].strip()
            prize_line = lines[i+2].strip()

            # Parse the A button
            a_parts = a_line.split(',')
            A_x = int(a_parts[0].split('+')[1].strip())
            A_y = int(a_parts[1].split('+')[1].strip())

            # Parse the B button
            b_parts = b_line.split(',')
            B_x = int(b_parts[0].split('+')[1].strip())
            B_y = int(b_parts[1].split('+')[1].strip())

            # Parse the Prize and adjust for the offset
            prize_parts = prize_line.split(',')
            Prize_x = int(prize_parts[0].split('=')[1].strip()) + 10000000000000
            Prize_y = int(prize_parts[1].split('=')[1].strip()) + 10000000000000

            machines.append({'A': (A_x, A_y), 'B': (B_x, B_y), 'Prize': (Prize_x, Prize_y)})

            i += 4  # Move to the next set of lines

    return machines

# Example usage:
filename = '/home/mworkman/advent-of-code-2024/day-13/input13.txt'  # Replace with your actual file name
machines = parse_input(filename)
prizes, cost = find_minimum_tokens(machines)
print(f"Maximum prizes won: {prizes}")
print(f"Minimum tokens spent: {cost}")