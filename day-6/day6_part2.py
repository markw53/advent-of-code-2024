def parse_input(input_map):
    grid = [list(row) for row in input_map.splitlines()]
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                start_pos = (r, c)
                start_dir = directions[cell]
                grid[r][c] = '.' 
    return grid, start_pos, start_dir

def turn_right(direction):
    turns = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    return turns[direction]

def simulate_guard(grid, start_pos, start_dir, max_iterations=10000):
    rows, cols = len(grid), len(grid[0])
    seen_states = set()
    pos, direction = start_pos, start_dir
    
    for _ in range(max_iterations):
        if (pos, direction) in seen_states:
            return True 
        seen_states.add((pos, direction))
        
        front_pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        if not (0 <= front_pos[0] < rows and 0 <= front_pos[1] < cols):
            break 
        
        if grid[front_pos[0]][front_pos[1]] == '#':
          direction = turn_right(direction)
        else:
            pos = front_pos
    
    return False 

def count_loop_positions(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    valid_positions = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != start_pos:
                grid[r][c] = '#'
                if simulate_guard(grid, start_pos, start_dir):
                    valid_positions += 1
                grid[r][c] = '.'
    
    return valid_positions

with open('/home/mworkman/advent-of-code-2024/day-6/input6.txt', 'r') as file:
    input_map = file.read()

grid, start_pos, start_dir = parse_input(input_map)
result = count_loop_positions(grid, start_pos, start_dir)

print(f"Number of valid positions to place an obstruction: {result}")
