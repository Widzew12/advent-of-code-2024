def to_base(number, base):
    if not number:
        return "0"
    digits = ""
    while number:
        digits = str(number % base) + digits
        number //= base
    return digits

def calculate(equation):
    num = equation[0] if equation[1] != "||" else 0
    current_num = str(equation[0]) if equation[1] == "||" else ""
    for i in range(1, len(equation), 2):
        if equation[i] == "||":
            num = int(str(num) + current_num + str(equation[i+1]))
        current_num += str(equation[i+1])
        if equation[i] == "*":
            num *= int(current_num)
        elif equation[i] == "+":
            num += int(current_num)
        current_num = ""
    
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
        possible_calc = [("+", "*", "||") for _ in range(len(numbers))]
        possible_indexes = []

        possible_indexes_length = len(possible_calc)

        for i in range(3**possible_indexes_length):
            a = to_base(i, 3)
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

    print()
    
    print(output_num)

if __name__ == "__main__":
    run()
