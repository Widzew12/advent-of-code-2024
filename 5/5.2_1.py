from itertools import permutations

def fix_update(update, rules):
    for i in range(len(update)):
            if update[i] in rules:
                for j in range(i):
                    if update[j] in rules[update[i]]:
                        invalid_page = update[j]
                        page_index = i
                        del update[j]
                        update.insert(page_index, invalid_page)
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
        #update = fix_update(update, rules)
        update_permutations = permutations(update)
        for possible_update in update_permutations:
            if is_update_valid(possible_update, rules):
                valid_updates.append(possible_update)
        print(update)

    # for update in invalid_updates:
    #     for i in range(len(update)):
    #         if update[i] in rules:
    #             for j in range(i):
    #                 if update[j] in rules[update[i]]:
    #                     invalid_page = update[j]
    #                     page_index = i + 1
    #                     del update[j]
    #                     update.insert(page_index, invalid_page)
    #         elif not i == len(update) - 1:
    #             invalid_page = update[i]
    #             del update[i]
    #             update.append(invalid_page)
    
    # up = []
    
    # for update in updates_input:
    #     is_valid = True
    #     for i in range(len(update)):
    #         if update[i] in rules:
    #             for j in range(i):
    #                 if update[j] in rules[update[i]]:
    #                     is_valid = False
    #                     break
    #         elif not i == len(update) - 1:
    #             is_valid = False
    #         if not is_valid:
    #             break
    #     if not is_valid:
    #         up.append(update)
    
    result = 0
    
    for update in valid_updates:
        result += int(update[len(update)//2])
    
    print(len(invalid_updates))
    print(len(valid_updates))
    print(result)
    
    #print(rules)
    #print(updates_input)
    
if __name__ == '__main__':
    run()