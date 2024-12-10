# x = vertical, y = horizontal

def check_position(position, trail_map):
    x, y = position
    return not (x < 0 or x >= len(trail_map) or y < 0 or y >= len(trail_map[0]))

def get_new_positions(pos, trail_map):
    x, y = pos
    new_positions = ((x + 1, y),
                     (x - 1, y),
                     (x, y + 1),
                     (x, y - 1))
    valid_positions = []
    for position in new_positions:
        valid_positions.append(position) if check_position(position, trail_map) else None
    return tuple(valid_positions)

def check(trail_map, start_pos):
    x_0, y_0 = start_pos
    if trail_map[x_0][y_0] == "9":
        return 1
    height_0 = int(trail_map[x_0][y_0])
    new_positions_1 = get_new_positions(start_pos, trail_map)
    number = 0
    for pos_1 in new_positions_1:
        x_1, y_1 = pos_1
        height_1 = int(trail_map[x_1][y_1])
        if height_1 == height_0 + 1:
            num = check(trail_map, pos_1)
            number += num
    return number

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
                num = check(trail_map, pos)
                print(num)
                total_score += num
    
    print()
    print(total_score)
    

if __name__ == "__main__":
    run()
