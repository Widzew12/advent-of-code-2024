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

def get_sides(curr_index, region_indexes):
    side_x = set()
    side_y = set()
    curr_x, curr_y = curr_index
    new_x = curr_x
    # side x right
    while True:
        new_x += 1
        index = (new_x, curr_y)
        if index in region_indexes:
            side_x.add(index)
        else:
            break
    # side x left
    new_x = curr_x
    while True:
        new_x -= 1
        index = (new_x, curr_y)
        if index in region_indexes:
            side_x.add(index)
        else:
            break
    # side y down
    new_y = curr_y
    while True:
        new_y += 1
        index = (curr_x, new_y)
        if index in region_indexes:
            side_y.add(index)
        else:
            break
    # side y up
    while True:
        new_y -= 1
        index = (curr_x, new_y)
        if index in region_indexes:
            side_y.add(index)
        else:
            break
    return tuple(side_x), tuple(side_y)

def get_sides_number(region_indexes):
    checked_indexes = dict()
    checked_sides = set()
    sides_num = 0
    for index in region_indexes:
        if index not in checked_indexes.keys() or checked_indexes[index] < 2:
            index_side_x, index_side_y = get_sides(index, region_indexes)
            if index_side_x not in checked_sides:
                sides_num += 1
            if index_side_y not in checked_sides:
                sides_num += 1
            checked_sides.add(index_side_x)
            checked_sides.add(index_side_y)
            # if len(index_side_x) == 0:
            #     print("a")
            # if len(index_side_y) == 0:
            #     print("b")
            # for side_index in index_side_x:
            #     if side_index in checked_indexes.keys():
            #         checked_indexes[side_index] += 1
            #     else:
            #         checked_indexes[side_index] = 1
            # for side_index in index_side_y:
            #     if side_index in checked_indexes.keys():
            #         checked_indexes[side_index] += 1
            #     else:
            #         checked_indexes[side_index] = 1
    return sides_num

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

    for region in regions:
        area = len(region)
        sides_num = get_sides_number(region)
        price = area * sides_num
        total_price += price
    
    print()
    print(total_price)


if __name__ == "__main__":
    run()
