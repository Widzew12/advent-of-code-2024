def calculate(equation):
    num = equation[0]
    for i in range(1, len(equation), 2):
        if equation[i] == "*":
            num *= equation[i+1]
        elif equation[i] == "+":
            num += equation[i+1]
        else:
            return False
    return num


def run():
    input_data = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\7\\7.txt", "r") as input_file:
        input_data = [[element.strip() for element in line.split(":")] for line in input_file.readlines()]
    
    for line in input_data:
        line[0] = int(line[0])
        line[1] = [int(num) for num in line[1].split(" ")]

    output_num = 0

    for line in input_data:
        target = line[0]
        numbers = line[1]
        possible_calc = [("+", "*") for i in range(len(numbers))]
        possible_indexes = []

        possible_indexes_length = len(possible_calc)

        for i in range(2**possible_indexes_length):
            a = bin(i)[2:]
            a = "0" * (possible_indexes_length - len(a)) + a
            possible_indexes.append([int(num) for num in a])
        
        is_good = False

        for indexes in possible_indexes:
            numbers_new = numbers.copy()
            for i in range(len(numbers)-1, 0, -1):
                numbers_new.insert(i, possible_calc[i][indexes[i]])
            
            if calculate(numbers_new) == target:
                is_good = True
                break
        
        if is_good:
            print(target)
            output_num += target
        
    print(output_num)

if __name__ == "__main__":
    run()
