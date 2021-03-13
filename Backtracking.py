def possible(grid, x, y):
    for i in range(9):
        if grid[i][y] == grid[x][y] and i != x:
            return False
    for i in range(9):
        if grid[x][i] == grid[x][y] and y != i:
            return False
    for i in range(3):
        for j in range(3):
            xcord = (x // 3) * 3 + i
            ycord = (y // 3) * 3 + j
            if grid[xcord][ycord] == grid[x][y] and xcord != x and ycord != y:
                return False
    return True


def empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (False, i, j)

    return (True, 0, 0)


def backtracking(grid):

    # terminating condition
    value, i, j = empty(grid)

    if value:
        return True
    for k in range(1, 10):
        grid[i][j] = k
        if possible(grid, i, j):
            if backtracking(grid):
                return True

        grid[i][j] = 0

    return False


def sudoku():
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]
    if backtracking(grid):
        print(grid)
    else:
        print("Error.")


sudoku()