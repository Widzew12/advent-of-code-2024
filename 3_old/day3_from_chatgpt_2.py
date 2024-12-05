import re

def parse_memory(memory_line):
    """
    Parses a line of corrupted memory and calculates the sum of valid `mul(X, Y)` results,
    respecting the current enabled/disabled state based on `do()` and `don't()` instructions.
    """
    # Regular expressions to find `do()`, `don't()`, and `mul(X, Y)`
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Initial state: mul instructions are enabled
    enabled = True
    total_sum = 0

    # Position pointer to iterate through the memory line
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

        # Check for `mul(X, Y)`
        elif match := re.match(mul_pattern, memory_line[i:]):
            if enabled:  # Only process `mul` if enabled
                num1, num2 = map(int, match.groups())
                total_sum += num1 * num2
            i += match.end()  # Move past the matched `mul(X, Y)`

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
