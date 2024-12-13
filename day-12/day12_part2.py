def calculate_total_price(map_input):
    rows = len(map_input)
    cols = len(map_input[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def is_valid(x, y, plant_type):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and map_input[x][y] == plant_type
    
    def flood_fill(x, y, plant_type):
        stack = [(x, y)]
        region = []
        while stack:
            cx, cy = stack.pop()
            if not visited[cx][cy]:
                visited[cx][cy] = True
                region.append((cx, cy))
                # Check all four directions
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny, plant_type):
                        stack.append((nx, ny))
        return region
    
    def calculate_sides(region):
        sides = 0
        for x, y in region:
            # Check all four sides
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < rows and 0 <= ny < cols) or map_input[nx][ny] != map_input[x][y]:
                    sides += 1
        return sides
    
    total_price = 0
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = map_input[i][j]
                region = flood_fill(i, j, plant_type)
                area = len(region)
                sides = calculate_sides(region)
                price = area * sides
                total_price += price
    
    return total_price

# Read the map from a file
def read_map_from_file(filename):
    with open(filename, 'r') as file:
        map_input = [line.strip() for line in file.readlines()]
    return map_input

# Example usage:
filename = '/home/mworkman/advent-of-code-2024/day-12/input12.txt'  # Replace with your actual file name
map_input = read_map_from_file(filename)
total_price = calculate_total_price(map_input)
print(total_price)