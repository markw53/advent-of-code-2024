from collections import defaultdict, deque

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

def reorder_update(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    
    for before, after in rules:
        if before in update_set and after in update_set:
            graph[before].append(after)
            in_degree[after] += 1
            if before not in in_degree:
                in_degree[before] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def main(file_path):
    rules, updates = parse_input(file_path)
    
    rule_map = defaultdict(list)
    for before, after in rules:
        rule_map[before].append(after)
    
    incorrect_updates = []
    corrected_middle_pages = []
    for update in updates:
        if not validate_update(update, rule_map):
            incorrect_updates.append(update)
            corrected_update = reorder_update(update, rules)
            middle_page = corrected_update[len(corrected_update) // 2]
            corrected_middle_pages.append(middle_page)
    
    return sum(corrected_middle_pages)

file_path = '/home/mworkman/advent-of-code-2024/day-5/input5.txt'  

print(main(file_path))
