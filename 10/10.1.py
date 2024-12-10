# x = vertical, y = horizontal

def check_position(x, y, trail_map):
    return not (x < 0 or x >= len(trail_map) or y < 0 or y >= len(trail_map[0]))

def check_possible_positions(trail_map, current_pos):
    pos_x, pos_y = current_pos
    current_height = int(trail_map[pos_x][pos_y])
    if current_height == 9:
        return True, True, (pos_x, pos_y)
    desired_height = current_height + 1
    new_positions = ((pos_x + 1, pos_y), # down
                     (pos_x - 1, pos_y), # up
                     (pos_x, pos_y + 1), # right
                     (pos_x, pos_y - 1)) # left
    end_pos_set = set()
    for new_pos in new_positions:
        new_pos_x, new_pos_y = new_pos
        if not check_position(new_pos_x, new_pos_y, trail_map):
            continue
        new_height = int(trail_map[new_pos_x][new_pos_y])
        if new_height == desired_height:
            found_end, is_end, end_positions = check_possible_positions(trail_map, new_pos)
            if found_end:
                if is_end:
                    end_pos_set.add(end_positions)
                else:
                    for end_pos in end_positions:
                        end_pos_set.add(end_pos)

    if len(end_pos_set) > 0:
        return True, False, list(end_pos_set)
    return False, False, None

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
                _, _, positions = check_possible_positions(trail_map, pos)
                print(positions)
                score = len(positions)
                total_score += score
    
    print()
    print(total_score)
    

if __name__ == "__main__":
    run()
