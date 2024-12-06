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

def simulate_guard(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pos, direction = start_pos, start_dir
    
    while True:
        visited.add(pos)
        front_pos = (pos[0] + direction[0], pos[1] + direction[1])
        
        if not (0 <= front_pos[0] < rows and 0 <= front_pos[1] < cols):
            break  
        
        if grid[front_pos[0]][front_pos[1]] == '#':
            direction = turn_right(direction)
        else:
            pos = front_pos
    
    return visited

with open('/home/mworkman/advent-of-code-2024/day-6/input6.txt', 'r') as file:
    input_map = file.read()

grid, start_pos, start_dir = parse_input(input_map)
visited_positions = simulate_guard(grid, start_pos, start_dir)

print(f"Distinct positions visited: {len(visited_positions)}")
