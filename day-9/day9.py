def parse_disk_map(disk_map):
    """Parses the disk map into a list of blocks with file IDs and free spaces."""
    blocks = []
    is_file = True 
    file_id = 0
    
    for length in map(int, disk_map):
        if is_file:
            blocks.extend([file_id] * length) 
            file_id += 1
        else:
            blocks.extend(["."] * length)  
        is_file = not is_file 
    
    return blocks

def compact_disk(blocks):
    """Compacts the disk layout by moving file blocks to the leftmost free space."""
    write_index = 0 
    
    for read_index, block in enumerate(blocks):
        if block != ".":  
            blocks[write_index] = block
            write_index += 1
    
    for i in range(write_index, len(blocks)):
        blocks[i] = "."
    
    return blocks

def calculate_checksum(blocks):
    """Calculates the checksum of the compacted disk layout."""
    checksum = 0
    for position, block in enumerate(blocks):
        if block != ".":  
            checksum += position * block
    return checksum

def main(file_path):
    with open(file_path, 'r') as file:
        disk_map = file.read().strip()
    
    blocks = parse_disk_map(disk_map)
    compacted_blocks = compact_disk(blocks)
    checksum = calculate_checksum(compacted_blocks)
    
    return checksum

file_path = "/home/mworkman/advent-of-code-2024/day-9/input9.txt"  
result = main(file_path)
print(f"Filesystem checksum: {result}")
