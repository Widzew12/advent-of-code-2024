# x = horizontal, y = vertical
MAX_X = 101
MAX_Y = 103
TIME = 100

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
    for sec in range(TIME):
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

    print(sec)

    for item in curr_dict:
        print(item, curr_dict[item])
    
    middl_x = MAX_X // 2
    middl_y = MAX_Y // 2

    quad_1 = 0 # left up
    quad_2 = 0 # right up
    quad_3 = 0 # right down
    quad_4 = 0 # left down
    for pos in curr_dict:
        x, y = pos
        num = len(curr_dict[pos])
        if x < middl_x and y < middl_y:
            quad_1 += num
        elif x > middl_x and y < middl_y:
            quad_2 += num
        elif x > middl_x and y > middl_y:
            quad_3 += num
        elif x < middl_x and y > middl_y:
            quad_4 += num
    
    safety_factor = quad_1 * quad_2 * quad_3 * quad_4
    print(safety_factor)
    


if __name__ == "__main__":
    run()
