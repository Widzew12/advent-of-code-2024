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

def get_sides_number(region_map):
    # Get edges number (sides number = edges number)
    sides_num = 0
    for index in region_map:
        curr_x, curr_y = index
        # External edges
        new_index_1 = (curr_x + 1, curr_y) # down
        new_index_2 = (curr_x, curr_y + 1) # right
        if new_index_1 not in region_map and new_index_2 not in region_map:
            sides_num += 1
        new_index_2 = (curr_x, curr_y - 1) # left
        if new_index_1 not in region_map and new_index_2 not in region_map:
            sides_num += 1
        new_index_1 = (curr_x - 1, curr_y) # up
        new_index_2 = (curr_x, curr_y + 1) # right
        if new_index_1 not in region_map and new_index_2 not in region_map:
            sides_num += 1
        new_index_2 = (curr_x, curr_y - 1) # left
        if new_index_1 not in region_map and new_index_2 not in region_map:
            sides_num += 1
        
        # Internal edges
        new_index_1 = (curr_x + 1, curr_y) # down
        new_index_2 = (curr_x, curr_y + 1) # right
        new_index_3 = (curr_x + 1, curr_y + 1) # down-right
        if new_index_1 in region_map and new_index_2 in region_map and new_index_3 not in region_map:
            sides_num += 1
        new_index_2 = (curr_x, curr_y - 1) # left
        new_index_3 = (curr_x + 1, curr_y - 1) # down-left
        if new_index_1 in region_map and new_index_2 in region_map and new_index_3 not in region_map:
            sides_num += 1
        new_index_1 = (curr_x - 1, curr_y) # up
        new_index_2 = (curr_x, curr_y + 1) # right
        new_index_3 = (curr_x - 1, curr_y + 1) # up-right
        if new_index_1 in region_map and new_index_2 in region_map and new_index_3 not in region_map:
            sides_num += 1
        new_index_2 = (curr_x, curr_y - 1) # left
        new_index_3 = (curr_x - 1, curr_y - 1) # up-left
        if new_index_1 in region_map and new_index_2 in region_map and new_index_3 not in region_map:
            sides_num += 1
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
    
    total_price = 0
    
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
