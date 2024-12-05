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

def convert_line_2(line):
    output = ""
    is_do = True
    do_str = "do()"
    dont_str = "don't()"
    while True:
        if is_do:
            dont_index = line.find(dont_str)
            if dont_index >= 0:
                output += line[:dont_index]
                line = line[dont_index + len(dont_str):]
                is_do = False
            else:
                output += line
                break
        else:
            do_index = line.find(do_str)
            if do_index >= 0:
                line = line[do_index + len(do_str):]
                is_do = True
            else:
                break
    return output

def convert_line(line):
    output_1 = []
    output_2 = []
    not_qualified_1 = []
    not_qualified_2 = []
    should_add = True
    do_count = 0
    dont_count = 0
    while True:
        start_index = line.find("mul(")
        
        if not should_add:
            do_index = line.find("do()")
            if do_index >= 0:
                should_add = True
                line = line[do_index:]
                continue
            else:
                break
        
        do_index = line.find("do()")
        dont_index = line.find("don't()")
        if dont_index >= 0 and dont_index <= start_index:
           if dont_index < do_index or do_index < 0:
               dont_count += 1
               should_add = False
               line = line[dont_index:]
               continue
        
        
        #do_index = line.find("do()")
        #dont_index = line.find("don't()")
        #if do_index >= 0 and do_index <= start_index:
        #    if do_index < dont_index or dont_index < 0:
        #        do_count += 1
        #        should_add = True
        #if dont_index >= 0 and dont_index <= start_index:
        #    if dont_index < do_index or do_index < 0:
        #        dont_count += 1
        #        should_add = False
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
        if num1_str == "251":
            print(True)
        num_1 = int(num1_str)
        num_2 = int(num2_str)
        if should_add:
            output_1.append(num_1)
            output_2.append(num_2)
        else:
            not_qualified_1.append(num_1)
            not_qualified_2.append(num_2)
        line = new_line
    print(do_count)
    print(dont_count)
    return output_1, output_2, not_qualified_1, not_qualified_2
        

def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\3_old\\day3.txt", "r") as input_file:
        input_data = input_file.readlines()
    
    data = [""]
    for line in input_data:
        data[0] += line
    
    output_data_1 = []
    output_data_2 = []
    not_qualified_data_1 = []
    not_qualified_data_2 = []
    for line in data:
        output_1, output_2, not_qualified_1, not_qualified_2 = convert_line(line)
        for element in output_1:
            output_data_1.append(element)
        for element in output_2:
            output_data_2.append(element)
        for element in not_qualified_1:
            not_qualified_data_1.append(element)
        for element in not_qualified_2:
            not_qualified_data_2.append(element)
    
    with open("day3.2_output.txt", "w") as output_file:
        for i in range(len(output_data_1)):
            output_file.write(f"{output_data_1[i]} {output_data_2[i]}\n")
    
    with open("day3.2_1_output.txt", "w") as output_file:
        for i in range(len(not_qualified_data_1)):
            output_file.write(f"{not_qualified_data_1[i]} {not_qualified_data_2[i]}\n")
    
    output_num = 0

    for i in range(len(output_data_1)):
        num1 = output_data_1[i]
        num2 = output_data_2[i]
        num = num1 * num2
        output_num += num
    
    print(len(output_data_1))
    print(len(output_data_2))
    print(output_num)
    print()
    

run()
