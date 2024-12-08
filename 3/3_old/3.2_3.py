def get_num(input):
    output_str = ""
    index = 0
    for c in input:
        if c.isnumeric():
            output_str += c
            index += 1
        else:
            break
    return output_str, index

def convert_line_for_task_2(line):
    output = ""
    do_str = "do()"
    dont_str = "don't()"
    while True:
        dont_index = line.find(dont_str)
        if dont_index >= 0:
            output += line[:dont_index]
            line = line[dont_index + len(dont_str):]
        else:
            output += line
            break
        do_index = line.find(do_str)
        if do_index >= 0:
            line = line[do_index + len(do_str):]
        else:
            break
    return output

def convert_line(line):
    output_1 = []
    output_2 = []
    while True:
        start_index = line.find("mul(")

        do_index = line.find("do()")
        dont_index = line.find("don't()")

        if do_index < dont_index:
            if do_index >= 0 and do_index < start_index:
                output_1.append("do()")
                output_2.append("do()")
                line = line[do_index:]
                continue
        else:
            if dont_index >= 0 and dont_index < start_index:
                output_1.append("don't()")
                output_2.append("don't()")
                line = line[dont_index:]
                continue

        if start_index == -1:
            break
        start_index += 4
        new_line = line[start_index:]
        num1_str, num1_end_index = get_num(new_line)
        if num1_str == "":
            line = new_line
            continue
        new_line = new_line[num1_end_index:]
        if not new_line[0] == ",":
            line = new_line
            continue
        new_line = new_line[1:]
        num2_str, num2_end_index = get_num(new_line)
        if num2_str == "":
            line = new_line
            continue
        new_line = new_line[num2_end_index:]
        if not new_line[0] == ")":
            line = new_line
            continue
        num_1 = int(num1_str)
        num_2 = int(num2_str)
        output_1.append(num_1)
        output_2.append(num_2)
        line = new_line
    return output_1, output_2
        

def run():
    input_data = []
    #with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\3\\day3.txt", "r") as input_file:
    with open("/home/szymon/Documents/Programowanie/advent_2024/3/day3.txt") as input_file:
        input_data = input_file.readlines()
    
    input_data_new = []
    for line in input_data:
        new_line = convert_line_for_task_2(line)
        input_data_new.append(new_line)
    
    input_data_new = input_data

    output_data_1 = []
    output_data_2 = []
    for line in input_data_new:
        output_1, output_2 = convert_line(line)
        for element in output_1:
            output_data_1.append(element)
        for element in output_2:
            output_data_2.append(element)
    
    with open("day3.2_3_output.txt", "w") as output_file:
        for i in range(len(output_data_1)):
            output_file.write(f"{output_data_1[i]} {output_data_2[i]}\n")
    
    with open("day3.2_3_output_1.txt", "w") as output_file:
        for line in input_data_new:
            pass
    
    output_num = 0

    for i in range(len(output_data_1)):
        num1 = output_data_1[i]
        num2 = output_data_2[i]
        num = num1 * num2
        output_num += num
    
    print(len(output_data_1))
    print(len(output_data_2))
    print()
    print(output_num)

run()
