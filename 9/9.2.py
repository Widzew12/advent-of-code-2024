def find_free_space(filesystem, lenght):
    for index in range(len(filesystem)):
        if filesystem[index][0] == "." and filesystem[index][1] >= lenght:
            return index
    return False

def find_id_index(filesystem, id):
    for index in range(len(filesystem)):
        if filesystem[index][0] == id:
            return index
    return False

def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\9\\9.txt", "r") as input_file:
        input_data = input_file.readline().strip()

    blocks_input = []
    block_id = 0
    for i in range(0, len(input_data), 2):
        blocks_input.append([block_id, int(input_data[i])])
        blocks_input.append([".", int(input_data[i+1])]) if i+1 < len(input_data) else None
        block_id += 1
    
    print(blocks_input)
    
    current_id = blocks_input[len(blocks_input) - 1][0]
    
    while current_id > 0:
        id_index = find_id_index(blocks_input, current_id)
        length = blocks_input[id_index][1]
        free_space_index = find_free_space(blocks_input, length)
        
        if free_space_index and free_space_index < id_index:
            blocks_input[free_space_index][1] -= length
            blocks_input.insert(free_space_index, [current_id, length])
            if id_index > free_space_index:
                id_index += 1
            blocks_input[id_index] = [".", length]
        
        current_id -= 1
    
    print(blocks_input)
    
    blocks_output = []
    for element in blocks_input:
        for _ in range(element[1]):
            blocks_output.append(element[0])
    
    checksum = 0
    for num in enumerate(blocks_output):
        if num[1] != ".":
            checksum += num[0] * num[1]

    print()
    print(checksum)


if __name__ == "__main__":
    run()

