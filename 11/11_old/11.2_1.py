def check_stone(stone, counter):
    counter += 1
    
    if counter < 40:
        print(counter)

    if counter == 76:
        return 1
    
    num = 0

    stone_str = str(stone)
    if stone == 0:
        new_stone = 1
        num = check_stone(new_stone, counter)
    elif len(stone_str) % 2 == 0:
        split_index = int(len(stone_str) / 2)
        new_stone_1 = int(stone_str[:split_index])
        new_stone_2 = int(stone_str[split_index:])
        num_1 = check_stone(new_stone_1, counter)
        num_2 = check_stone(new_stone_2, counter)
        num = num_1 + num_2
    else:
        new_stone = stone * 2024
        num = check_stone(new_stone, counter)

    return num


def run():
    input_data = []
    with open("11.txt", "r") as input_file:
        input_data = [int(element) for element in input_file.readline().strip().split(" ")]
    print(input_data)
    stones = input_data.copy()

    total_stones_num = 0

    for stone in stones:
        stones_num = check_stone(stone, 0)
        print(stones_num)
        total_stones_num += stones_num
    
    #print(stones)
    print()
    print(total_stones_num)



if __name__ == "__main__":
    run()
