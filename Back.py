from Sudoku import center_cords, Digit


def Backtrack(CENTERS, digit_typed):

    for i in center_cords:
        if CENTERS[i[0]][i[1]] == -1:
            for j in range(1, 10):
                digit_typed[(i[0], i[1])] = Digit(i[0], i[1], j)
                if digit_typed.possible:
                    if Backtrack(CENTERS, digit_typed):
                        return True
                digit_typed.pop((i[0], i[1]))
                CENTERS[i[0]][i[1]] = -1
    return False
