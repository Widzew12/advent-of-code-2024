

def run():
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\3\\3.txt") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    data = [[(element.split(")")[0]).split(",") for element in line.split("mul(")] for line in input_data]
    
    print(data)
    
    number = 0
    
    for line in data:
        for element in line:
            if len(element) == 2:
                num1, num2 = element
                if num1.isnumeric() and num2.isnumeric():
                    number += int(num1) * int(num2)
    
    print()
    print(number)
    

if __name__ == "__main__":
    run()
