def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\4\\4.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    total_num = 0
    
    for i in range(1, len(input_data) - 1):
        for j in range(1, len(input_data[i]) - 1):
            if input_data[i][j] == "A":
                # Right-down or left-up
                diagonal_1_correct = ((input_data[i-1][j-1] == "M" and input_data[i+1][j+1] == "S") 
                                      or (input_data[i-1][j-1] == "S" and input_data[i+1][j+1] == "M"))
                
                # Right-up or left-down
                diagonal_2_correct = ((input_data[i+1][j-1] == "M" and input_data[i-1][j+1] == "S") 
                                      or (input_data[i+1][j-1] == "S" and input_data[i-1][j+1] == "M"))
                
                if diagonal_1_correct and diagonal_2_correct:
                    total_num += 1
    
    print(total_num)
    
run()