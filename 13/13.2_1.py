BIG_NUMBER = 1000000000000000000

def check_machine(machine):
    butt_a, butt_b, prize = machine
    butt_a_x, butt_a_y = butt_a
    butt_b_x, butt_b_y = butt_b
    prize_x, prize_y = prize
    
    min_tokens_num = BIG_NUMBER
    
    # button a first
    max_a_x = prize_x // butt_a_x
    max_a_y = prize_y // butt_a_y
    max_a_presses = min(max_a_x, max_a_y)
    print(max_a_presses)
    
    for a_presses in range(max_a_presses):
        if a_presses % 10000000 == 0:
            print(a_presses)
            pass
        tokens_num = a_presses * 3
        curr_x = butt_a_x * a_presses
        curr_y = butt_a_y * a_presses
        
        curr_b_x = prize_x - curr_x
        curr_b_y = prize_y - curr_y
        
        if curr_b_x % butt_b_x == 0 and curr_b_y % butt_b_y == 0:
            b1 = curr_b_x // butt_b_x
            b2 = curr_b_y // butt_b_y
            if b1 == b2:
                b_presses = b1
                tokens_num += b_presses * 1
                min_tokens_num = min(tokens_num, min_tokens_num)
            
    # button b first
    max_b_x = prize_x // butt_b_x
    max_b_y = prize_y // butt_b_y
    max_b_presses = min(max_b_x, max_b_y)
    
    for b_presses in range(max_b_presses):
        tokens_num = b_presses * 1
        curr_x = butt_b_x * b_presses
        curr_y = butt_b_y * b_presses
            
        curr_a_x = prize_x - curr_x
        curr_a_y = prize_y - curr_y
        
        if curr_a_x % butt_a_x == 0 and curr_a_y % butt_a_y == 0:
            a1 = curr_a_x // butt_a_x
            a2 = curr_a_y // butt_a_y
            if a1 == a2:
                a_presses = a1
                tokens_num += a_presses * 3
                min_tokens_num = min(tokens_num, min_tokens_num)
    
    return min_tokens_num


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
            #x = int(element[1].split(",")[0])
            y = int(element[2]) + 10000000000000
            #y = int(element[2])
            machine.append((x, y))
        elif i % 4 == 3:
            machines.append(machine)
            machine = []
    
    total_tokens_num = 0
    for machine in machines:
        tokens_num = check_machine(machine)
        can_win = tokens_num < BIG_NUMBER
        # print(can_win)
        if can_win:
            #print(tokens_num)
            total_tokens_num += tokens_num
    
    print()
    print(total_tokens_num)


if __name__ == "__main__":
    run()
