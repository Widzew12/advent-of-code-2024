# x = vertical, y = horizontal


def check_plot(curr_index, garden_map, prev_plots):
    curr_x, curr_y = curr_index
    curr_plant = garden_map[curr_x][curr_y]
    new_indexes = ((curr_x + 1, curr_y), # down
                   (curr_x - 1, curr_y), # up
                   (curr_x, curr_y + 1), # right
                   (curr_x, curr_y - 1)) # left

    prev_plots.add(curr_index)
    for new_index in new_indexes:
        new_x, new_y = new_index
        if new_x >= 0 and new_x < len(garden_map) and new_y >= 0 and new_y < len(garden_map[new_x]):
            if new_index not in prev_plots and garden_map[new_x][new_y] == curr_plant:
                new_plots = (check_plot(new_index, garden_map, prev_plots))
                for plot_index in new_plots:
                    prev_plots.add(plot_index)
    return prev_plots

def create_sides(region_indexes, curr_index):
    region_map = dict()
    for index in region_indexes:
        print(index)
        region_map[index] = "X"
    max_x = 0
    max_y = 0
    for index in region_indexes:
        curr_x, curr_y = index
        max_x = max(curr_x, max_x)
        max_y = max(curr_y, max_y)
        new_indexes = ((curr_x + 1, curr_y), # down
                   (curr_x - 1, curr_y), # up
                   (curr_x, curr_y + 1), # right
                   (curr_x, curr_y - 1)) # left
        for new_index in new_indexes:
            if new_index not in region_map.keys():
                region_map[new_index] = "."
    
    region_map_list = [[" " for _ in range(max_y + 3)] for _ in range(max_x + 3)]
    for index in region_map.keys():
        region_map_list[index[0] + 1][index[1] + 1] = region_map[index]
        print(index)
    region_map_list[curr_index[0] + 1][curr_index[1] + 1] = "O"
    for line in region_map_list:
        string = ""
        for element in line:
            string += element
        print(string)

def track_sides(start_index, start_direction, region_map):
    direction_dict_right = {(1, 0): (0, -1),
                      (0, -1): (-1, 0),
                      (-1, 0): (0, 1),
                      (0, 1) : (1, 0)}
    direction_dict_left = {(1, 0): (0, 1),
                     (0, 1): (-1, 0),
                     (-1, 0): (0, -1),
                     (0, -1): (1, 0)}

    curr_direction = start_direction
    curr_index = start_index
    
    checked_indexes_set = set()
    sides_number = 0
    
    
    
    moves = 0
    should_move = False
    should_move_false_counter = 0
    counter = 0
    
    # Check if starts in a inner corner
    a_index_x, a_index_y = curr_index
    b_index_x = a_index_x + 1
    b_index_y = a_index_y
    b_index = (b_index_x, b_index_y)
    if b_index in region_map:
        print(b_index)
        sides_number = 1
    
    while True:
        counter += 1
        curr_dir_x, curr_dir_y = curr_direction
        curr_x, curr_y = curr_index
        moves += 1
        if should_move:
            curr_x = curr_x + curr_dir_x
            curr_y = curr_y + curr_dir_y
            # should_move_false_counter = 0
        else:
            should_move_false_counter += 1
            # print(should_move_false_counter)
        if should_move_false_counter >= 0:
        #if start_index == (3, 34):
            #create_sides(region_map, curr_index)
            #print("a")
            pass
        curr_index = (curr_x, curr_y)
        checked_indexes_set.add(curr_index)
        should_move = True
        if curr_index == start_index and moves > 3:
            break
        # Check if we have "wall" to the right
        check_index_x = curr_x + curr_dir_y
        check_index_y = curr_y - curr_dir_x
        check_index = (check_index_x, check_index_y)
        if check_index not in region_map:
            # there is no wall to the right, we turn right
            new_direction = direction_dict_right[curr_direction]
            curr_direction = new_direction
            sides_number += 1
            continue
        # Check if we have wall in front
        check_index_x = curr_x + curr_dir_x
        check_index_y = curr_y + curr_dir_y
        check_index = (check_index_x, check_index_y)
        if check_index in region_map:
            # there is a wall in front, we turn left
            new_direction = direction_dict_left[curr_direction]
            curr_direction = new_direction
            sides_number += 1
            should_move = False
            continue
        # if none of the previous conditions were met, we continue

    if sides_number == 1:
        #create_sides(region_map, (-1, -1))
        print("EEE")
    
    print(f"sides: {sides_number}")
    return sides_number, checked_indexes_set

def get_sides_number(region_map):
    checked_indexes = set()
    total_sides_num = 0
    for index in region_map:
        index_x, index_y = index
        new_index_x = index_x
        new_index_y = index_y - 1
        new_index = (new_index_x, new_index_y)
        if new_index not in region_map:
            # print("A")
            if new_index not in checked_indexes:
                sides_num, new_checked_indexes = track_sides(new_index, (-1, 0), region_map)
                # print(sides_num)
                total_sides_num += sides_num
                for new_new_index in new_checked_indexes:
                    checked_indexes.add(new_new_index)
    # print(checked_indexes)
    return total_sides_num


def run():
    garden_map = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\12\\12.txt", "r") as input_file:
        garden_map = [line.strip() for line in input_file.readlines()]

    regions = []
    visited_indexes = set()

    for x in range(len(garden_map)):
        for y in range(len(garden_map[x])):
            index = (x, y)
            if index not in visited_indexes:
                region = check_plot(index, garden_map, set())
                regions.append(region)
                for plot_index in region:
                    visited_indexes.add(plot_index)
                # print(regions)
    
    total_price = 0
    
    # region = regions[1]
    # print(region)
    # sides_num, checked_indexes = track_sides((1, 0), (-1, 0), region)
    # print(sides_num)
    # print(checked_indexes)
    
    for region in regions:
        area = len(region)
        sides_num = get_sides_number(region)
        price = area * sides_num
        print(price)
        total_price += price
    
    print()
    print(total_price)


if __name__ == "__main__":
    run()
