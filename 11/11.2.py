import math

# dict(stone, dict(iteration, number))
prev_stones_dict = dict()

def check_stone(stone, counter):
    counter += 1
    
    if counter == 76:
        return 1
    
    add_to_dict = False

    if stone in prev_stones_dict.keys():
        if counter in prev_stones_dict[stone].keys():
            return prev_stones_dict[stone][counter]
    else:
        add_to_dict = True
    
    if stone != 0:
        digits_num = math.floor(math.log10(stone) + 1)
    
    num = 0
    
    if stone == 0:
        num = check_stone(1, counter)
    elif digits_num % 2 == 0:
        power = 10**(digits_num // 2)
        num = check_stone(stone // power, counter) + check_stone(stone % power, counter)
    else:
        num = check_stone(stone * 2024, counter)
    
    if add_to_dict:
        prev_stones_dict[stone] = dict()
    
    prev_stones_dict[stone][counter] = num
    
    return num

def run():
    stones = []
    with open("11.txt", "r") as input_file:
        stones = [int(element) for element in input_file.readline().strip().split(" ")]
    print(stones)
    
    total_num = 0
    for stone in stones:
        num = check_stone(stone, 0)
        print(num)
        total_num += num
        
    print()
    print(total_num)

if __name__ == "__main__":
    run()
