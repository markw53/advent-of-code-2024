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

def calculate_score(grid, trailhead):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [trailhead]
    reachable_nines = set()
    
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # If height is 9, add to reachable nines
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
            continue
        
        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c] + 1:  # Valid hiking trail step
                    stack.append((nr, nc))
    
    return len(reachable_nines)

def sum_of_trailhead_scores(filename):
    grid = read_topographic_map(filename)
    trailheads = find_trailheads(grid)
    total_score = sum(calculate_score(grid, trailhead) for trailhead in trailheads)
    return total_score

# Example usage:
filename = "/home/mworkman/advent-of-code-2024/day-10/input10.txt"
result = sum_of_trailhead_scores(filename)
print(f"Sum of scores of all trailheads: {result}")
