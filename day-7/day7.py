from itertools import product

def evaluate_expression(nums, ops):
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
    return result

def find_matching_calibrations(equations):
    total_calibration_result = 0

    for equation in equations:
        test_value, nums = equation
        num_operators = len(nums) - 1
        found_match = False

        for ops in product(['+', '*'], repeat=num_operators):
            if evaluate_expression(nums, ops) == test_value:
                found_match = True
                break

        if found_match:
            total_calibration_result += test_value

    return total_calibration_result

def parse_input(file_path):
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  
                test_value, nums = line.split(":")
                test_value = int(test_value)
                nums = list(map(int, nums.split()))
                equations.append((test_value, nums))
    return equations

file_path = "/home/mark-workman/Documents/coding/advent-of-code-2024/day-7/input7.txt"  

equations = parse_input(file_path)
result = find_matching_calibrations(equations)
print("Total Calibration Result:", result)
