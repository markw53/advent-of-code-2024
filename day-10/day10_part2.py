def read_topographic_map(filename):
    with open(filename, "r") as file:
        return [[int(char) for char in line.strip()] for line in file]

def find_trailheads(grid):
    trailheads = []
    for r, row in enumerate(grid):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def calculate_rating(grid, trailhead):
    rows, cols = len(grid), len(grid[0])
    stack = [(trailhead, [])] 
    visited_paths = set()
    
    while stack:
        (r, c), path = stack.pop()
        path = path + [(r, c)] 
        
        if grid[r][c] == 9:
            visited_paths.add(tuple(path))
            continue        
       
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c] + 1: 
                    stack.append(((nr, nc), path))
    
    return len(visited_paths)

def sum_of_trailhead_ratings(filename):
    grid = read_topographic_map(filename)
    trailheads = find_trailheads(grid)
    total_rating = sum(calculate_rating(grid, trailhead) for trailhead in trailheads)
    return total_rating

filename = "/home/mworkman/advent-of-code-2024/day-10/input10.txt"
result = sum_of_trailhead_ratings(filename)
print(f"Sum of ratings of all trailheads: {result}")
