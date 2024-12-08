def parse_memory(memory_line):
    """
    Parses a line of corrupted memory and calculates the sum of valid `mul(X, Y)` results,
    respecting the current enabled/disabled state based on `do()` and `don't()` instructions.
    """
    enabled = True  # Initial state: mul instructions are enabled
    total_sum = 0
    i = 0

    while i < len(memory_line):
        # Check for `do()`
        if memory_line[i:i+4] == "do()":
            enabled = True
            i += 4  # Skip past `do()`

        # Check for `don't()`
        elif memory_line[i:i+7] == "don't()":
            enabled = False
            i += 7  # Skip past `don't()`

        # Check for `mul(`
        elif memory_line[i:i+4] == "mul(":
            i += 4  # Skip past `mul(`
            num1 = ""
            num2 = ""
            
            # Parse the first number
            while i < len(memory_line) and memory_line[i].isdigit():
                num1 += memory_line[i]
                i += 1

            # Check for comma
            if i < len(memory_line) and memory_line[i] == ",":
                i += 1
            else:
                continue  # Invalid format, skip

            # Parse the second number
            while i < len(memory_line) and memory_line[i].isdigit():
                num2 += memory_line[i]
                i += 1

            # Check for closing parenthesis
            if i < len(memory_line) and memory_line[i] == ")":
                i += 1  # Skip past `)`
            else:
                continue  # Invalid format, skip

            # If enabled, calculate and add the multiplication
            if enabled and num1.isdigit() and num2.isdigit():
                total_sum += int(num1) * int(num2)

        # Skip invalid characters
        else:
            i += 1

    return total_sum

def main():
    # Read the input from the file
    input_file_path = "D:\\Programowanie\\Advent of code\\advent-of-code-2024\\3\\day3.txt"
    with open(input_file_path, "r") as file:
        memory_lines = file.readlines()

    # Process each line of corrupted memory and compute the total sum
    total_sum = sum(parse_memory(line.strip()) for line in memory_lines)

    # Output the result
    print("Total Sum of Enabled Multiplications:", total_sum)

if __name__ == "__main__":
    main()
