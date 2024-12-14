# x = horizontal, y = vertical
MAX_X = 101
MAX_Y = 103
TIME = 100

def display_robots(robots_dict):
    robots_map = [[" " for _ in range(MAX_X)] for _ in range(MAX_Y)]
    for robot_pos in robots_dict:
        x, y = robot_pos
        robots_map[y][x] = "#"
    output = []
    for line in robots_map:
        output_line = ""
        for c in line:
            output_line += c
        output_line += "\n"
        output.append(output_line)
    output.append("\n")
    return output

def run():
    input_data = []
    with open("14.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    print(input_data)

    robots_list = []
    robots_dict = dict()
    for line in input_data:
        pos = line[2:].split(" ")[0].split(",")
        position = (int(pos[0]), int(pos[1]))
        vel = line.split(" ")[1][2:].split(",")
        velocity = (int(vel[0]), int(vel[1]))
        robots_list.append([position, velocity])
        if position in robots_dict:
            robots_dict[position].append(velocity)
        else:
            robots_dict[position] = [velocity]
    
    for item in robots_dict:
        print(item, robots_dict[item])

    curr_dict = robots_dict.copy()
    sec = 0

    output = []
    
    for sec in range(10000):
        new_dict = dict()
        for robot_pos in curr_dict:
            pos_x, pos_y = robot_pos
            for robot_vel in curr_dict[robot_pos]:
                vel_x, vel_y = robot_vel
                new_pos_x = pos_x + vel_x
                new_pos_y = pos_y + vel_y

                if new_pos_x < 0:
                    new_pos_x = MAX_X + new_pos_x
                if new_pos_x >= MAX_X:
                    new_pos_x -= MAX_X
                if new_pos_y < 0:
                    new_pos_y = MAX_Y + new_pos_y
                if new_pos_y >= MAX_Y:
                    new_pos_y -= MAX_Y
                
                new_pos = (new_pos_x, new_pos_y)
                if new_pos in new_dict:
                    new_dict[new_pos].append(robot_vel)
                else:
                    new_dict[new_pos] = [robot_vel]
        curr_dict = new_dict
        
        output_text = display_robots(curr_dict)
        for line in output_text:
            output.append(line)
            if len(output) == 782019:
                print(sec + 1)
        
        sec += 1

    with open("output_1.txt", "w") as output_file:
        output_file.writelines(output)

if __name__ == "__main__":
    run()
