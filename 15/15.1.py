# x = vertical, y = horizontal
# (-1, 0) - up
# (1, 0) - down
# (0, -1) - left
# (0, 1) - right


def find_player(warehouse_map):
    for row_enum in enumerate(warehouse_map):
        for col_enum in enumerate(row_enum[1]):
            if col_enum[1] == "@":
                return (row_enum[0], col_enum[0])


def check_for_move(warehouse_map, current_pos, move_dir):
    curr_x, curr_y = current_pos
    move_x, move_y = move_dir
    while True:
        curr_x += move_x
        curr_y += move_y
        curr_field = warehouse_map[curr_x][curr_y]
        if curr_field == "#":
            return False
        if curr_field == ".":
            return True

def make_move(warehouse_map, current_pos, move_dir):
    curr_x, curr_y = current_pos
    move_x, move_y = move_dir
    new_x = curr_x + move_x
    new_y = curr_y + move_y
    curr_field = warehouse_map[curr_x][curr_y]
    new_field = warehouse_map[new_x][new_y]
    if new_field == ".":
        warehouse_map[curr_x][curr_y] = new_field
        warehouse_map[new_x][new_y] = curr_field
    else:
        make_move(warehouse_map, (new_x, new_y), move_dir)
        new_field = warehouse_map[new_x][new_y]
        warehouse_map[curr_x][curr_y] = new_field
        warehouse_map[new_x][new_y] = curr_field
    return (new_x, new_y)
    

def print_map(warehouse_map):
    for row in warehouse_map:
        output_str = ""
        for field in row:
            output_str += field
        print(output_str)
        output_str = ""
            
def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\15\\15.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    index = input_data.index("")
    warehouse_map = [[element for element in line] for line in input_data[:index]]
    moves = ''.join(input_data[index:])
    
    moves_dict = {"^": (-1, 0),
                  "v": (1, 0),
                  "<": (0, -1),
                  ">": (0, 1)}

    curr_pos = find_player(warehouse_map)
    
    for move in moves:
        move_dir = moves_dict[move]
        if check_for_move(warehouse_map, curr_pos, move_dir):
            curr_pos = make_move(warehouse_map, curr_pos, move_dir)
    
    print_map(warehouse_map)
    
    coordinate_sum = 0
    for row_enum in enumerate(warehouse_map):
        for field_enum in enumerate(row_enum[1]):
            if field_enum[1] == "O":
                coordinate = row_enum[0] * 100 + field_enum[0]
                print(coordinate)
                coordinate_sum += coordinate
    
    print()
    print(coordinate_sum)
    

if __name__ == "__main__":
    run()

