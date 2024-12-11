def blink(prev_stones):
    new_stones = []
    for stone in prev_stones:
        stone_str = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(stone_str) % 2 == 0:
            split_index = int(len(stone_str) / 2)
            new_stones.append(int(stone_str[:split_index]))
            new_stones.append(int(stone_str[split_index:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

def run():
    input_data = []
    with open("11.txt", "r") as input_file:
        input_data = [int(element) for element in input_file.readline().strip().split(" ")]
    print(input_data)
    stones = input_data.copy()

    for i in range(25):
        stones = blink(stones)
        print(i)
        print(len(stones))
    
    #print(stones)
    print()
    print(len(stones))



if __name__ == "__main__":
    run()
