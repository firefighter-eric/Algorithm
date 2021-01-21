def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def dfs(pos):
        nonlocal valid

        if  valid or pos == 81:
            valid = True
            return

        
        if not space[pos]:
            dfs(pos + 1)
            return

        y, x = pos // 9, pos % 9
        y_block, x_block = y // 3, x // 3
        for d in range(9):
            if row[y][d] or col[x][d] or block[y_block][x_block][d]:
                continue

            row[y][d] = True
            col[x][d] = True
            block[y_block][x_block][d] = True
            board[y][x] = str(d + 1)

            dfs(pos + 1)
            if valid:
                return

            row[y][d] = False
            col[x][d] = False
            block[y_block][x_block][d] = False
            board[y][x] = '.'
        return

    row = [[False] * 9 for _ in range(9)]
    col = [[False] * 9 for _ in range(9)]
    block = [[[False] * 9 for i in range(3)] for j in range(3)]
    space = []
    valid = False

    for y in range(9):
        for x in range(9):
            d = board[y][x]
            if d != '.':
                d = int(d) - 1
                row[y][d] = True
                col[x][d] = True
                y_block, x_block = y // 3, x // 3
                block[y_block][x_block][d] = True
                space.append(False)
            else:
                space.append(True)

    dfs(0)

def show_board(board):
    for line in board:
        for x in line:
            print(x, end=' ')
        print()
    print()

if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]                                                                                                                                                                                                
    show_board(board)

    solveSudoku(board)

    show_board(board)
