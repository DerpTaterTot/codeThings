def check(lst):
    lst = [i for i in lst if i != 0]
    return len(lst) == len(set(lst))

def horizontal(sudoku):
    for row in sudoku:
        if not check(row):
            return False
    return True


def box(sudoku): 
    for row in (0, 3, 6):
        for col in (0, 3, 6):
            square = [sudoku[x][y] for x in range(row, row + 3) for y in range(col, col + 3)]
            if not check(square):
                return False
    return True

def box2(sudoku):
    for row in (0, 3, 6):
        cklist = [0]*9
        for col in (0, 3, 6):
            i = 0          
            for x in range(row, row + 3):
                for y in range(col, col + 3):
                    cklist[i] = sudoku[x][y]
                    i += 1
            if not check(cklist):
                return False
    return True
    

def vertical(sudoku):
    vertical_sudoku = [[], [], [], [], [], [], [], [], [], []]
    for i in range(9):
        for row in sudoku:
            vertical_sudoku[i].append(row[i])

    return horizontal(vertical_sudoku)

def vertical_check(sudoku):
    for col in range(9):
        cklst=[0]*9
        for row in range(9):
            cklst[row]=sudoku[row][col]
        if not check(cklst):
            return False
    return True

def sudokucheck(sudoku):
    return horizontal(sudoku) and vertical(sudoku) and box2(sudoku)

sudoku = [
[9, 7, 4, 2, 3, 6, 1, 5, 8], 
[6, 3, 8, 5, 9, 1, 7, 4, 2],
[1, 2, 5, 4, 8, 7, 9, 3, 6],
[3, 1, 6, 7, 5, 4, 2, 8, 9],
[7, 4, 2, 9, 1, 8, 5, 6, 3],
[5, 8, 9, 3, 6, 2, 4, 1, 7],
[8, 6, 7, 1, 2, 5, 3, 9, 4],
[2, 5, 3, 6, 4, 9, 8, 7, 1],
[4, 9, 1, 8, 7, 3, 6, 2, 5]
    ]

print(box2(sudoku))

def main():
    sudoku = [
    [9, 7, 4, 2, 3, 6, 1, 5, 8], 
    [6, 3, 8, 5, 9, 1, 7, 4, 2],
    [1, 2, 5, 4, 8, 7, 9, 3, 6],
    [3, 1, 6, 7, 5, 4, 2, 8, 9],
    [7, 4, 2, 9, 1, 8, 5, 6, 3],
    [5, 8, 9, 3, 6, 2, 4, 1, 7],
    [8, 6, 7, 1, 2, 5, 3, 9, 4],
    [2, 5, 3, 6, 4, 9, 8, 7, 1],
    [4, 9, 1, 8, 7, 3, 6, 2, 5]
        ]

    print(sudokucheck(sudoku))


if __name__ == "__main__":
    main()

