def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\4\\4.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    total_num = 0
    
    # Horizontal, to the right and to the left (1, 2)
    for line in input_data:
        for i in range(len(line) - 3):
            checked_str = line[i:i+4]
            if checked_str == "XMAS" or checked_str == "SAMX":
                total_num += 1
    
    # Vertical, down and up (3, 4)
    for i in range(len(input_data) - 3):
        for j in range(len(input_data[i])):
            checked_str = input_data[i][j] + input_data[i+1][j] + input_data[i+2][j] + input_data[i+3][j]
            if checked_str == "XMAS" or checked_str == "SAMX":
                total_num += 1
    
    # Diagonal, down-right or up-left (5, 6)
    for i in range(len(input_data) - 3):
        for j in range(len(input_data) - 3):
            checked_str = input_data[i][j] + input_data[i+1][j+1] + input_data[i+2][j+2] + input_data[i+3][j+3]
            if checked_str == "XMAS" or checked_str == "SAMX":
                total_num += 1
    
    # Diagonal, down-left or up-right (7, 8)
    for i in range(len(input_data) - 3):
        for j in range(3, len(input_data)):
            checked_str = input_data[i][j] + input_data[i+1][j-1] + input_data[i+2][j-2] + input_data[i+3][j-3]
            if checked_str == "XMAS" or checked_str == "SAMX":
                total_num += 1
    
    print(total_num)
    
run()