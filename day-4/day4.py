def read_grid_from_file(file_path):
    """Reads the grid from a .txt file and returns it as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def count_xmas_patterns(grid):
    """Counts the number of X-MAS patterns in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0

    def is_mas_diagonal(r1, c1, r2, c2, r3, c3):
        try:
            return (
                grid[r1][c1] in "MS" and
                grid[r2][c2] == "A" and
                grid[r3][c3] in "MS"
            )
        except IndexError:
            return False

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if (
                is_mas_diagonal(r - 1, c - 1, r, c, r + 1, c + 1) and
                is_mas_diagonal(r + 1, c - 1, r, c, r - 1, c + 1)
            ):
                xmas_count += 1

    return xmas_count

file_path = "/home/mworkman/advent-of-code-2024/day-4/input4.txt"  
grid = read_grid_from_file(file_path)
result = count_xmas_patterns(grid)
print(f"Number of X-MAS patterns: {result}")
