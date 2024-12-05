def get_number(input_string):
    num = ""
    i = 0
    c = input_string[0]
    while c.isnumeric():
        num += c
        i += 1
        c = input_string[i]
    if num == "":
        return ("", 1)
    return (int(num), i)

def check_line(line):
    index = 0
    
    number = 0
    
    while index >= 0:
        line = line[index:]
        
        num1, index = get_number(line)
        line = line[index:]
        if line[0] == ",":
            line = line[1:]
            num2, index = get_number(line)
            line = line[index:]
            if line[0] == ")":
                number += num1 * num2
        
        index = line.find("mul(")
        if index >= 0:
            index += 4
    
    return number
    # print(str(index) + ": " + line)

def run():
    input_data = []
    with open("/home/szymon/Documents/Programowanie/advent_2024/day3.txt", "r") as input_file:
        input_data = input_file.readlines()

    total_number = 0

    for line in input_data:
        total_number += check_line(line)

    print(total_number)

run()
