# x = vertical, y = horizontal

maze_map = []
#checked_indexes_set = set()
not_good_indexes_set = set()


def check_field(curr_index, prev_dir, checked_indexes_set):
    print(number[0])
    number[0] += 1
    #print(curr_index)

    curr_x, curr_y = curr_index

    if maze_map[curr_x][curr_y] == "E":
        return 0

    new_indexes = ((curr_x + 1, curr_y), # down
                   (curr_x - 1, curr_y), # up
                   (curr_x, curr_y + 1), # right
                   (curr_x, curr_y - 1)) # left
    
    checked_fields = []
    walls_counter = 0
    not_good_counter = 0
    good_counter = 0
    for new_index in new_indexes:
        new_x, new_y = new_index

        if new_x < 0 or new_x >= len(maze_map) or new_y < 0 or new_y >= len(maze_map[new_x]):
            continue

        if maze_map[new_x][new_y] == "#":
            walls_counter += 1
            continue
        
        if new_index in not_good_indexes_set:
            not_good_counter += 1
            continue


        if new_index in checked_indexes_set:
            continue
        
        new_checked_indexes = checked_indexes_set.copy()
        new_checked_indexes.add(new_index)

        

        prev_dir_x, prev_dir_y = prev_dir
        curr_dir_x = new_x - curr_x
        curr_dir_y = new_y - curr_y
        curr_dir = (curr_dir_x, curr_dir_y)
        checked_field = check_field(new_index, curr_dir, new_checked_indexes)


        if checked_field is None:
            continue
        
        good_counter += 1
        
        print(new_index, checked_field)
        
        if curr_dir_x == prev_dir_x and curr_dir_y == curr_dir_y:
            path_len = checked_field + 1
        elif curr_dir_x == prev_dir_x or curr_dir_y == prev_dir_y:
            path_len = checked_field + 2001
        else:
            path_len = checked_field + 1001
        
        checked_fields.append(path_len)

    if walls_counter >= 3: 
        not_good_indexes_set.add(curr_index)
    
    if not_good_counter > 0 and good_counter == 0:
        not_good_indexes_set.add(curr_index)

    if len(checked_fields) == 0:
        return None

    return min(checked_fields)


if __name__ == "__main__":
    with open("/home/szymon/Documents/Programowanie/advent_2024/16/16.txt", "r") as input_file:
        maze_map = [line.strip() for line in input_file.readlines()]
    
    start_index = None
    end_index = None
    for line_enum in enumerate(maze_map):
        for c_enum in enumerate(line_enum[1]):
            if c_enum[1] == "S":
                start_index = (line_enum[0], c_enum[0])
            if c_enum[1] == "E":
                end_index = (line_enum[0], c_enum[0])
    
    number = check_field(start_index, (0, 1), set())

    print()
    print(number)