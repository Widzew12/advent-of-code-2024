# x = vertical, y = horizontal

def check_position(x, y, trail_map):
    return not (x < 0 or x >= len(trail_map) or y < 0 or y >= len(trail_map[0]))

def check_possible_positions(trail_map, current_pos, prev_paths_list, this_path_index):
    pos_x, pos_y = current_pos
    current_height = int(trail_map[pos_x][pos_y])
    # print("b")
    if current_height == 9:
        return prev_paths_list
    desired_height = current_height + 1 
    new_positions = ((pos_x + 1, pos_y), # down
                     (pos_x - 1, pos_y), # up
                     (pos_x, pos_y + 1), # right
                     (pos_x, pos_y - 1)) # left
    
    this_path = prev_paths_list[this_path_index].copy()
    # print(prev_paths_list)
    del prev_paths_list[this_path_index]
    
    for new_pos in new_positions:
        new_pos_x, new_pos_y = new_pos
        if not (check_position(new_pos_x, new_pos_y, trail_map)):
            continue
        new_height = int(trail_map[new_pos_x][new_pos_y])
        # print("A")
        if new_height == desired_height:
            this_path.append(new_pos)
            prev_paths_list.append(this_path)
            new_paths = check_possible_positions(trail_map, new_pos, prev_paths_list.copy(), len(prev_paths_list) - 1)
            # print(len(new_paths))
            for path in new_paths:
                if path not in prev_paths_list:
                    prev_paths_list.append(path)
                else:
                    # print("E")
                    pass
    ex = False
    try:
        print(prev_paths_list[1][0][0][0])
    except:
        ex = True
    if not ex:
        print("S")
    
    return prev_paths_list
    

def run():
    input_data = []
    with open("10.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    trail_map = input_data.copy()

    total_score = 0
    for line_enum in enumerate(trail_map):
        for element_enum in enumerate(line_enum[1]):
            height = int(element_enum[1])
            if height == 0:
                pos = (line_enum[0], element_enum[0])
                path_list = check_possible_positions(trail_map, pos, [[pos]], 0)
                new_path_list = [element for element in path_list if len(element) == 10]
                total_score += len(new_path_list)
                print(new_path_list)
    
    print()
    print(total_score)
    

if __name__ == "__main__":
    run()
