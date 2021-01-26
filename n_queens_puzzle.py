def solveNQueens(n: int):
    def change_flag(y, x, d1, d2, flag):
        board[y][x] = 'Q' if flag else '.'
        row[y] = flag
        col[x] = flag
        diag1[d1] = flag
        diag2[d2] = flag

    def record():
        ans.append([])
        for line in board:
            ans[-1].append(''.join(line))

    def backtrack(pos_start, count):
        if count == n:
            record()
            return

        for pos in range(pos_start, n * n):
            y, x = pos // n, pos % n
            d1, d2 = x + y, x - y + n - 1
            if row[y] or col[x] or diag1[d1] or diag2[d2]:
                continue
            
            change_flag(y, x, d1, d2, True)
            backtrack(pos + 1, count + 1)
            change_flag(y, x, d1, d2, False)
        return

    board = [['.'] * n for _ in range(n)]
    row = [False] * n
    col = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    ans = []

    backtrack(0, 0)
    return ans

if __name__ == '__main__':
    queens4 = solveNQueens(4)
    print('queens4:', queens4)

    queens8 = solveNQueens(8)
    print('queens8:', len(queens8))
