from collections import defaultdict

def parse_map(file_path):
    """Reads the antenna map from a file and returns a dictionary of positions by frequency."""
    antennas = defaultdict(list)
    with open(file_path, 'r') as file:
        map_data = file.readlines()
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row.strip()):
            if cell != ".":
                antennas[cell].append((x, y))
    return antennas, len(map_data[0].strip()), len(map_data)

def calculate_antinodes(antennas, map_width, map_height):
    """Calculate all unique antinode positions."""
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        # Check each pair of antennas with the same frequency
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Check if they are collinear (horizontal, vertical, or diagonal)
                dx, dy = x2 - x1, y2 - y1
                if dx != 0 and dy != 0 and abs(dx) != abs(dy):
                    continue

                # Calculate midpoint
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2

                # Check for integer midpoints
                if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
                    # Add the midpoint as an antinode
                    antinodes.add((mid_x, mid_y))

                # Calculate extended antinode positions
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                # Add valid antinodes within bounds
                if 0 <= antinode1[0] < map_width and 0 <= antinode1[1] < map_height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < map_width and 0 <= antinode2[1] < map_height:
                    antinodes.add(antinode2)

    # Include all antenna positions (they are also antinodes)
    for positions in antennas.values():
        antinodes.update(positions)

    return len(antinodes)

# File path to the map
file_path = '/home/markworkman/Documents/coding/advent-of-code-2024/day-8/input8.txt'

# Parse the antenna map
antennas, map_width, map_height = parse_map(file_path)

# Calculate the number of unique antinodes
unique_antinode_count = calculate_antinodes(antennas, map_width, map_height)
print(f"Unique antinode locations: {unique_antinode_count}")
