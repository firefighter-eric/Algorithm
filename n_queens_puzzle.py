# 1 General method
def solveNQueens(n: int) -> list:
    """backtrack

    Args:
        n (int): n queen puzzle

    Returns:
        list: all board state
    """
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

# 2
def solveNQueens2(n: int) -> list:
    """backtrack

    Args:
        n (int): n queen puzzle

    Returns:
        list: all board state
    """
    def change_flag(y, x, d1, d2, flag):
        board[y][x] = 'Q' if flag else '.'
        col[x] = flag
        diag1[d1] = flag
        diag2[d2] = flag

    def record():
        ans.append([])
        for line in board:
            ans[-1].append(''.join(line))

    def backtrack(y):
        if y == n:
            record()
            return

        for x in range(n):
            d1, d2 = x + y, x - y + n - 1
            if col[x] or diag1[d1] or diag2[d2]:
                continue
            
            change_flag(y, x, d1, d2, True)
            backtrack(y + 1)
            change_flag(y, x, d1, d2, False)
        return

    board = [['.'] * n for _ in range(n)]
    col = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    ans = []

    backtrack(0)
    return ans

# 3
def totalNQueens(n: int) -> int:
    """Calculate the result number of n queens puzzle

    Args:
        n (int): n queen puzzle

    Returns:
        int: the result number
    """
    def change_flag(y, x, d1, d2, flag):
        col[x] = flag
        diag1[d1] = flag
        diag2[d2] = flag

    def backtrack(y):
        if y == n:
            nonlocal ans
            ans += 1
            return

        for x in range(n):
            d1, d2 = x + y, x - y + n - 1
            if col[x] or diag1[d1] or diag2[d2]:
                continue
            
            change_flag(y, x, d1, d2, True)
            backtrack(y + 1)
            change_flag(y, x, d1, d2, False)
        return

    col = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    ans = 0

    backtrack(0)
    return ans

if __name__ == '__main__':
    queens4 = solveNQueens(4)
    print('queens4:', queens4)

    queens8 = solveNQueens(8)
    print('queens8:', len(queens8))

    queens4_2 = solveNQueens2(4)
    print('queens4:', queens4_2)

    queens8_2 = solveNQueens2(8)
    print('queens8:', len(queens8_2))

    n_queens8 = totalNQueens(8)
    print('queens8:', n_queens8)
