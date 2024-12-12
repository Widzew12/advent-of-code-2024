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

def calculate_perimeter(region_indexes):
    perimeter = 0
    calculated_plots = set()

    for index in region_indexes:
        if index in calculated_plots:
            continue
        curr_x, curr_y = index
        new_indexes = ((curr_x + 1, curr_y), # down
                       (curr_x - 1, curr_y), # up
                       (curr_x, curr_y + 1), # right
                       (curr_x, curr_y - 1)) # left
        for new_index in new_indexes:
            if new_index not in region_indexes:
                perimeter += 1

    return perimeter

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
        perimeter = calculate_perimeter(region)
        price = area * perimeter
        print(price)
        total_price += price
    
    print()
    print(total_price)


if __name__ == "__main__":
    run()
