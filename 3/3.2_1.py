

def run():
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\3\\3.txt") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
    
    input_data_2 = ""
    for line in input_data:
        input_data_2 += line
    
    data = [element.split("don't()")[0] for element in input_data_2.split("do()")]
    
    data = [[(element_2.split(")")[0]).split(",") for element_2 in element.split("mul(")] for element in data]
    
    print(data)
    
    number = 0
    
    for element in data:
        for element_2 in element:
            if len(element_2) == 2:
                num1, num2 = element_2
                if num1.isnumeric() and num2.isnumeric():
                    number += int(num1) * int(num2)
    
    print()
    print(number)
    

if __name__ == "__main__":
    run()
