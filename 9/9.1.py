def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\9\\9.txt", "r") as input_file:
        input_data = input_file.readline().strip()
    
    blocks_input = []
    block_id = 0
    for i in range(0, len(input_data), 2):
        for _ in range(0, int(input_data[i])):
            blocks_input.append(block_id)
        if i+1 < len(input_data):
            for _ in range(0, int(input_data[i+1])):
                blocks_input.append(".")
        block_id += 1
    
    lower_index = 0
    upper_index = len(blocks_input) - 1
    
    while lower_index < upper_index:
        if blocks_input[lower_index] != ".":
            lower_index += 1
        elif blocks_input[upper_index] == ".":
            upper_index -= 1
        else:
            blocks_input[lower_index], blocks_input[upper_index] = blocks_input[upper_index], blocks_input[lower_index]
    
    print(blocks_input)

    checksum = 0
    i = 0
    while blocks_input[i] != ".":
        checksum += i * int(blocks_input[i])
        i += 1
    
    print()
    print(checksum)


if __name__ == "__main__":
    run()
