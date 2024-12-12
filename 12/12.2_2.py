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



def check_side_x(start_index, region_map):
    side_x = set()
    curr_x, curr_y = start_index
    new_x = curr_x
    # side x right
    while True:
        new_x += 1
        index = (new_x, curr_y)
        if index in region_map.keys() and region_map[index] == ".":
            side_x.add(index)
        else:
            break
    # side x left
    new_x = curr_x
    while True:
        new_x -= 1
        index = (new_x, curr_y)
        if index in region_map.keys() and region_map[index] == ".":
            side_x.add(index)
        else:
            break
    return tuple(side_x)

def check_side_y(start_index, region_map):
    side_y = set()
    curr_x, curr_y = start_index
    # side y down
    new_y = curr_y
    while True:
        new_y += 1
        index = (curr_x, new_y)
        if index in region_map.keys() and region_map[index] == ".":
            side_y.add(index)
        else:
            break
    # side y up
    while True:
        new_y -= 1
        index = (curr_x, new_y)
        if index in region_map.keys() and region_map[index] == ".":
            side_y.add(index)
        else:
            break
    return tuple(side_y)

def create_sides(region_indexes):
    region_map = dict()
    for index in region_indexes:
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
    for line in region_map_list:
        print(line)
    
    sides_num = 0
    
    checked_sides = set()
    for index in region_map.keys():
        if region_map[index] == ".":
            curr_x, curr_y = index
            new_indexes_x = ((curr_x + 1, curr_y), # down
                   (curr_x - 1, curr_y)) # up
            new_indexes_y = ((curr_x, curr_y + 1), # right
                   (curr_x, curr_y - 1)) # left
            check_y = False
            for new_index in new_indexes_x:
                if new_index in region_map.keys() and region_map[new_index] == "X":
                    # There is an X on the left or right, so we check down/up for side
                    check_y = True
                    break
            
            check_x = False
            for new_index in new_indexes_y:
                if new_index in region_map.keys() and region_map[new_index] == "X":
                    # There is an X above or under, so we check left/right for side
                    check_x = True
                    break
            
            if check_x:
                new_side = check_side_x(index, region_map)
                if new_side not in checked_sides:
                    sides_num += 1
                checked_sides.add(new_side)
            if check_y:
                new_side = check_side_y(index, region_map)
                if new_side not in checked_sides:
                    sides_num += 1
                checked_sides.add(new_side)
    
    print(sides_num, len(checked_sides))

def run():
    garden_map = []
    with open("12.txt", "r") as input_file:
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
    
    create_sides(regions[0])
    
    for region in regions:
        area = len(region)
        sides_num = 1
        price = area * sides_num
        total_price += price
    
    print()
    print(total_price)


if __name__ == "__main__":
    run()
