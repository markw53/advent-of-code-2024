def process_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                mid = len(digits) // 2
                left, right = int(digits[:mid]), int(digits[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

initial_stones = [5688, 62084, 2, 3248809, 179, 79, 0, 172169]

# Number of blinks
num_blinks = 75

# Simulate the evolution of stones
final_stones = process_stones(initial_stones, num_blinks)

# Output the number of stones after 75 blinks
print(len(final_stones))
