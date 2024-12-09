def get_indexes_of_character(input_list, character):
    output = []
    for i in enumerate(input_list):
        for j in enumerate(i[1]):
            output.append((i[0], j[0])) if j[1] == character else None
    return output
    
def get_antinode_indexes(node_index_1, node_index_2, max_x, max_y):
    x1 = node_index_1[0]
    x2 = node_index_2[0]
    y1 = node_index_1[1]
    y2 = node_index_2[1]
    shift_x = x2 - x1
    shift_y = y2 - y1
    antinode_indexes = []
    # Subtract shift
    x, y = x1, y1
    while x >= 0 and x < max_x and y >= 0 and y < max_y:
        antinode_indexes.append((x, y))
        x -= shift_x
        y -= shift_y
    
    # Add shift
    x, y = x1, y1
    while x >= 0 and x < max_x and y >= 0 and y < max_y:
        antinode_indexes.append((x, y))
        x += shift_x
        y += shift_y
    
    return antinode_indexes


def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\8\\8.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    max_x = len(input_data)
    max_y = len(input_data[0])
    
    possible_characters = {c for c in ''.join(input_data) if c != "."}
    indexes_dict = {character:get_indexes_of_character(input_data, character) for character in possible_characters}
    
    all_antinode_indexes = set()
    
    for letter_indexes in indexes_dict.values():
        for letter_index_1 in letter_indexes:
            for letter_index_2 in letter_indexes:
                if letter_index_1 != letter_index_2:
                    for index in get_antinode_indexes(letter_index_1, letter_index_2, max_x, max_y):
                        all_antinode_indexes.add(index)
    
    print(len(all_antinode_indexes))


if __name__ == "__main__":
    run()
    