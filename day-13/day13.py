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

            a_parts = a_line.split(',')
            A_x = int(a_parts[0].split('+')[1].strip())
            A_y = int(a_parts[1].split('+')[1].strip())

            b_parts = b_line.split(',')
            B_x = int(b_parts[0].split('+')[1].strip())
            B_y = int(b_parts[1].split('+')[1].strip())

            prize_parts = prize_line.split(',')
            Prize_x = int(prize_parts[0].split('=')[1].strip())
            Prize_y = int(prize_parts[1].split('=')[1].strip())

            machines.append({'A': (A_x, A_y), 'B': (B_x, B_y), 'Prize': (Prize_x, Prize_y)})

            i += 4  

    return machines

def find_minimum_tokens(machines):
    max_presses = 100
    total_prizes = 0
    total_cost = 0

    for machine in machines:
        A_x, A_y = machine['A']
        B_x, B_y = machine['B']
        Prize_x, Prize_y = machine['Prize']
        
        min_cost = float('inf')
        found_solution = False

        for n_A in range(max_presses + 1):
            for n_B in range(max_presses + 1):
                if (n_A * A_x + n_B * B_x == Prize_x) and (n_A * A_y + n_B * B_y == Prize_y):
                    cost = 3 * n_A + 1 * n_B
                    if cost < min_cost:
                        min_cost = cost
                        found_solution = True

        if found_solution:
            total_prizes += 1
            total_cost += min_cost

    return total_prizes, total_cost

filename = '/home/mworkman/advent-of-code-2024/day-13/input13.txt'  
machines = parse_input(filename)
prizes, cost = find_minimum_tokens(machines)
print(f"Maximum prizes won: {prizes}")
print(f"Minimum tokens spent: {cost}")