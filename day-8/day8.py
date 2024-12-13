def parse_map(filename):
    antennas = {}
    with open(filename, 'r') as file:
        map_input = file.readlines()
        for y, line in enumerate(map_input):
            line = line.strip()
            for x, char in enumerate(line):
                if char != '.':
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((x, y))
    return antennas, len(map_input), len(map_input[0]) if map_input else 0

def calculate_antinodes(antennas, width, height):
    antinodes = set()
    
    for frequency, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Calculate potential antinodes
                # Antinode 1: (2*x1 - x2, 2*y1 - y2)
                ax1, ay1 = 2 * x1 - x2, 2 * y1 - y2
                if 0 <= ax1 < width and 0 <= ay1 < height:
                    antinodes.add((ax1, ay1))
                
                # Antinode 2: (2*x2 - x1, 2*y2 - y1)
                ax2, ay2 = 2 * x2 - x1, 2 * y2 - y1
                if 0 <= ax2 < width and 0 <= ay2 < height:
                    antinodes.add((ax2, ay2))
    
    return antinodes

def count_unique_antinodes(filename):
    antennas, height, width = parse_map(filename)
    antinodes = calculate_antinodes(antennas, width, height)
    return len(antinodes)

# Example usage:
filename = '/home/mworkman/advent-of-code-2024/day-8/input8.txt'  # Replace with your actual file name
unique_antinodes = count_unique_antinodes(filename)
print(f"Number of unique antinode locations: {unique_antinodes}")