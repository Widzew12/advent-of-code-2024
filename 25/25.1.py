


def run():
    input_data = []
    with open("25.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    keys = []
    locks = []
    
    input_gap = 8
    pin_height = 5
    lock_key_length = 5
    
    for i in range(0, len(input_data), input_gap):
        first_line = input_data[i]
        if first_line[0] == "#":
            lock = []
            for j in range(lock_key_length):
                counter = 0
                for k in range(i + 1, i + pin_height + 1):
                    if input_data[k][j] == ".":
                        break
                    counter += 1
                lock.append(counter)
            locks.append(tuple(lock))
        else:
            key = []
            for j in range(lock_key_length):
                counter = 0
                for k in range(i + pin_height, i, -1):
                    if input_data[k][j] == ".":
                        break
                    counter += 1
                key.append(counter)
            keys.append(tuple(key))
    
    available_space = 5
    
    answer = 0
    
    for key in keys:
        for lock in locks:
            is_good = True
            for i in range(len(key)):
                taken_space = key[i] + lock[i]
                if taken_space > available_space:
                    is_good = False
                    break
            if is_good:
                answer += 1
    
    print()
    print(answer)


if __name__ == "__main__":
    run()    
