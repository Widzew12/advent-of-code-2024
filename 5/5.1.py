def run():
    rules_input = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\5\\5_rules.txt", "r") as input_file:
        rules_input = [line.strip().split("|") for line in input_file.readlines()]
    updates_input = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\5\\5_updates.txt", "r") as input_file:
        updates_input = [line.strip().split(",") for line in input_file.readlines()]
    
    rules = {}
    
    for rule in rules_input:
        left = rule[0]
        right = rule[1]
        if left in rules:
            rules[left].add(right)
        else:
            # Create a set
            rules[left] = {right}
    
    valid_updates = []
    
    for update in updates_input:
        is_valid = True
        for i in range(len(update)):
            if update[i] in rules:
                for j in range(i):
                    if update[j] in rules[update[i]]:
                        is_valid = False
                        break
            elif not i == len(update) - 1:
                is_valid = False
            if not is_valid:
                break
        if is_valid:
            valid_updates.append(update)
    
    result = 0
    
    for update in valid_updates:
        result += int(update[len(update)//2])
    
    print(valid_updates)
    print(result)
    
    #print(rules)
    #print(updates_input)
    
if __name__ == '__main__':
    run()
