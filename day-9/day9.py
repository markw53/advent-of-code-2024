def parse_disk_map(disk_map):
    """
    Parse the dense disk map format into a detailed string representation.
    """
    if len(disk_map) % 2 != 0:
        print("Warning: Input length is odd. Adding a default free space of 0.")
        disk_map += "0"  # Append a free space of size 0

    detailed_map = []
    file_id = 0
    for i in range(0, len(disk_map), 2):
        file_size = int(disk_map[i])
        free_space_size = int(disk_map[i + 1])
        # Add file blocks
        detailed_map.extend([str(file_id)] * file_size)
        file_id += 1
        # Add free space blocks
        detailed_map.extend(['.'] * free_space_size)
    return ''.join(detailed_map)


def compact_disk(detailed_map):
    """
    Simulate the compaction process.
    """
    disk = list(detailed_map)
    write_pos = 0  # Pointer to where the next file block should be written
    for read_pos in range(len(disk)):
        if disk[read_pos] != '.':
            disk[write_pos] = disk[read_pos]
            if write_pos != read_pos:
                disk[read_pos] = '.'
            write_pos += 1
        # Debugging output
        print(f"Step {read_pos}: {''.join(disk)}")
    return ''.join(disk)


def calculate_checksum(compacted_map):
    """
    Calculate the checksum from the compacted disk map.
    """
    checksum = 0
    for pos, block in enumerate(compacted_map):
        if block != '.':
            block_value = pos * int(block)
            print(f"Position: {pos}, Block ID: {block}, Contribution: {block_value}")
            checksum += block_value
    return checksum


# Read input from the file
input_file = "/home/mworkman/advent-of-code-2024/day-9/input9.txt"  # Replace with your actual file name
with open(input_file, "r") as file:
    disk_map_input = file.read().strip()  # Read and remove any extra spaces or newlines

# Process the input
try:
    detailed_map = parse_disk_map(disk_map_input)
    print("Detailed Map Before Compaction:", detailed_map)

    compacted_map = compact_disk(detailed_map)
    print("Compacted Map After Compaction:", compacted_map)

    checksum = calculate_checksum(compacted_map)

    # Print results
    print("Checksum:", checksum)

except ValueError as e:
    print("Error:", e)
