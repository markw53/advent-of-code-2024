def parse_input(file_path):
    with open(file_path, 'r') as f:
        sections = f.read().strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].split('\n')]
    updates = [list(map(int, line.split(','))) for line in sections[1].split('\n')]
    return rules, updates

def validate_update(update, rule_map):
    position = {page: i for i, page in enumerate(update)}
    
    for before, afters in rule_map.items():
        if before in position:
            for after in afters:
                if after in position and position[before] > position[after]:
                    return False
    return True

def main(file_path):
    rules, updates = parse_input(file_path)
    
    rule_map = {}
    for before, after in rules:
        if before not in rule_map:
            rule_map[before] = []
        rule_map[before].append(after)
    
    valid_middle_pages = []
    for update in updates:
        if validate_update(update, rule_map):
            middle_page = update[len(update) // 2]
            valid_middle_pages.append(middle_page)
    
    return sum(valid_middle_pages)

file_path = '/home/mworkman/advent-of-code-2024/day-5/input5.txt'  

print(main(file_path))
