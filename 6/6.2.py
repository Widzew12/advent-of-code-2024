def run():
    b = []
    with open("D:\\Programowanie\\Advent of code\\advent-of-code-2024\\6\\6.txt") as input_file:
        b = [[c for c in line.strip()] for line in input_file.readlines()]
    
    d = 0
    
    e = 0
    
    for x in range(len(b)):
        for y in range(len(b[x])):
            a = [b[i].copy() for i in range(len(b))]
            if a[x][y] not in ("^", "v", "<", ">"):
                a[x][y] = "#"

            # print("\n"*60)
            # for line in a:
            #     out = ""
            #     for ch in line:
            #         out += ch
            #     print(out)
            
            row = col = 0
            for m in range(len(a)):
                for n in range(len(a[m])):
                    if a[m][n] in ("^", "v", "<", ">"):
                        row = m
                        col = n

            c = 0
            
            prev_moves = set()

            while True:
                move = a[row][col]
                
                if (row, col, move) in prev_moves:
                    e += 1
                    print(row, col, move)
                    break
                
                prev_moves.add((row, col, move))
                
                if row in (x - 1, x, x + 1) and col in (y - 1, y, y + 1):
                    #print(row, col)
                    pass
                
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
            d += 1
            # print(c)
            # print(d)
    
    print()
    print(e)

if __name__ == "__main__":
    run()
