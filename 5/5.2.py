def fix_update(update, rules):
    for i in range(len(update)):
            if update[i] in rules:
                for j in range(i):
                    if update[j] in rules[update[i]]:
                        invalid_page = update[j]
                        del update[j]
                        update.append(invalid_page)
                        update = fix_update(update, rules)
            elif not i == len(update) - 1:
                invalid_page = update[i]
                del update[i]
                update.append(invalid_page)
                update = fix_update(update, rules)
    return update

def is_update_valid(update, rules):
    for i in range(len(update)):
        if update[i] in rules:
            for j in range(i):
                if update[j] in rules[update[i]]:
                    return False
        elif not i == len(update) - 1:
            return False
    return True

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
    
    invalid_updates = []
    
    for update in updates_input:
        if not is_update_valid(update, rules):
            invalid_updates.append(update)

    valid_updates = []

    for update in invalid_updates:
        valid_updates.append(fix_update(update, rules))
        print(update)
    
    result = 0
    
    for update in valid_updates:
        result += int(update[len(update)//2])
    
    print(len(invalid_updates))
    print(len(valid_updates))
    print(result)
    
if __name__ == '__main__':
    run()
