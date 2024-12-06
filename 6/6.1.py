def run():
    a = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\6\\6.txt") as input_file:
        a = [[c for c in line.strip()] for line in input_file.readlines()]
    
    row = col = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] in ("^", "v", "<", ">"):
                row = i
                col = j
    
    c = 0
    
    while True:
        move = a[row][col]
        if move == "^":
            # Move up
            # Check for edge of map
            if row - 1 < 0:
                break
            # Check for obstacle
            if a[row - 1][col] == "#":
                a[row][col] = ">"
                continue
            # Check if the guard visited the spot before
            if a[row - 1][col] != "X":
                c += 1
            # Move the guard
            a[row - 1][col] = "^"
            a[row][col] = "X"
            row -= 1
        elif move == "v":
            # Move down
            if row + 1 >= len(a):
                break
            if a[row + 1][col] == "#":
                a[row][col] = "<"
                continue
            if a[row + 1][col] != "X":
                c += 1
            a[row + 1][col] = "v"
            a[row][col] = "X"
            row += 1
        elif move == "<":
            # Move left
            if col - 1 < 0:
                break
            if a[row][col - 1] == "#":
                a[row][col] = "^"
                continue
            if a[row][col - 1] != "X":
                c += 1
            a[row][col - 1] = "<"
            a[row][col] = "X"
            col -= 1
        elif move == ">":
            # Move right
            if col + 1 >= len(a[row]):
                break
            if a[row][col + 1] == "#":
                a[row][col] = "v"
                continue
            if a[row][col + 1] != "X":
                c += 1
            a[row][col + 1] = ">"
            a[row][col] = "X"
            col += 1
        else:
            print(False)
    
    # Count also the last move
    c += 1
    print(c)

if __name__ == "__main__":
    run()
