def get_num(input):
    output_str = ""
    index = 0
    for c in input:
        if c.isnumeric():
            output_str += c
            index += 1
        else:
            break
    return output_str, index


def parse_instructions(line):
    enabled = True  # mul instructions start as enabled
    results = []

    while line:
        if line.startswith("do()"):
            enabled = True
            line = line[4:]  # Skip "do()"
        elif line.startswith("don't()"):
            enabled = False
            line = line[7:]  # Skip "don't()"
        elif line.startswith("mul(") and enabled:
            line = line[4:]  # Skip "mul("
            num1_str, idx1 = get_num(line)
            if not num1_str:
                continue
            line = line[idx1:]
            if not line.startswith(","):
                continue
            line = line[1:]  # Skip ","
            num2_str, idx2 = get_num(line)
            if not num2_str:
                continue
            line = line[idx2:]
            if not line.startswith(")"):
                continue
            line = line[1:]  # Skip ")"
            results.append(int(num1_str) * int(num2_str))
        else:
            line = line[1:]  # Skip invalid characters
    return results


def run():
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\3\\day3.txt", "r") as input_file:
        input_data = input_file.readlines()

    total_sum = 0
    for line in input_data:
        total_sum += sum(parse_instructions(line))

    print("Total:", total_sum)

run()
