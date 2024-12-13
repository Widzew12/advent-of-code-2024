def check_machine(machine):
    butt_a, butt_b, prize = machine
    a1, a2 = butt_a
    b1, b2 = butt_b
    c1, c2 = prize
    
    W = a1 * b2 - a2 * b1
    Wx = b2 * c1 - b1 * c2
    Wy = a1 * c2 - a2 * c1
    
    a_presses = Wx / W  # x
    b_presses = Wy / W  # y
    
    if a_presses.is_integer() and b_presses.is_integer():
        tokens_num = 3 * int(a_presses) + 1 * int(b_presses)
        return tokens_num
    
    return False

def run():
    input_data = []
    with open("13.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    machines = []
    machine = []
    for i in range(len(input_data)):
        if i % 4 == 0 or i % 4 == 1:
            x = int(input_data[i][12:14])
            y = int(input_data[i][18:20])
            machine.append((x, y))
        elif i % 4 == 2:
            element = input_data[i].split("=")
            x = int(element[1].split(",")[0]) + 10000000000000
            y = int(element[2]) + 10000000000000
            machine.append((x, y))
        elif i % 4 == 3:
            machines.append(machine)
            machine = []
    
    total_tokens_num = 0
    for machine in machines:
        tokens_num = check_machine(machine)
        if tokens_num:
            print(tokens_num)
            total_tokens_num += tokens_num
    
    print()
    print(total_tokens_num)


if __name__ == "__main__":
    run()
