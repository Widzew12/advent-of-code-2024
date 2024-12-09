

def get_indexes_of_character(input_list, character):
    output = []
    for i in enumerate(input_list):
        for j in enumerate(i[1]):
            output.append((i[0], j[0])) if j[1] == character else 0
    return output
    
def get_antinode_indexes(node_index_1, node_index_2):
    x1 = node_index_1[0]
    x2 = node_index_2[0]
    y1 = node_index_1[1]
    y2 = node_index_2[1]
    shift_x = x2 - x1
    shift_y = y2 - y1
    output1_x = x2 + shift_x
    output1_y = y2 + shift_y
    output2_x = x1 - shift_x
    output2_y = y1 - shift_y
    return ((output1_x, output1_y), (output2_x, output2_y))


def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\8\\8.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    max_x = len(input_data)
    max_y = len(input_data[0])
    
    possible_characters = {c for c in ''.join(input_data) if c != "."}
    indexes_dict = {character:get_indexes_of_character(input_data, character) for character in possible_characters}
    
    print(possible_characters)
    
    print(indexes_dict)
    
    all_antinode_indexes = set()
    
    for letter in indexes_dict.keys():
        letter_indexes = indexes_dict[letter]
        print(letter, letter_indexes)
        for letter_index_1 in letter_indexes:
            for letter_index_2 in letter_indexes:
                if letter_index_1 != letter_index_2:
                    antinode_index_1, antinode_index_2 = get_antinode_indexes(letter_index_1, letter_index_2)
                    print(antinode_index_1, antinode_index_2)
                    if antinode_index_1[0] >= 0 and antinode_index_1[0] < max_x and antinode_index_1[1] >= 0 and antinode_index_1[1] < max_y:
                        all_antinode_indexes.add(antinode_index_1)
                    if antinode_index_2[0] >= 0 and antinode_index_2[0] < max_x and antinode_index_2[1] >= 0 and antinode_index_2[1] < max_y:
                        all_antinode_indexes.add(antinode_index_2)

    print(all_antinode_indexes)
    print()
    print(len(all_antinode_indexes))


if __name__ == "__main__":
    run()
    