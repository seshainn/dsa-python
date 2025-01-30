#sorted squared array - calculate squares and arrange them in ascending order, given a sorted array of integers (Time complexity should be O(n) and not nlog(n))
def squared_sorted(array):
    n = len(array)
    squared = [0] * n
    i=0
    j=n-1
    for k in reversed(range(n)):
        if array[i]**2 > array[j]**2:
            squared[k] = array[i]**2
            i += 1
        else:
            squared[k] = array[j]**2
            j -= 1
    return squared
print(squared_sorted([-5, -3, 1, 2, 4, 5, 7]))

#monotonic array - array should either be in increasing order or decreasing order (can have duplicates also)
def monotonic_array(array):
    if len(array) <= 1:
        return True
    for i in range(1, len(array)):
        if (array[i] >= array[0] and array[i] < array[i-1]):
            return False
        if (array[i] <= array[0] and array[i] > array[i-1]):
            return False
    return True
print(monotonic_array([-5, -3, -3, 3, 6, 7, 7, 9, 9]))
print(monotonic_array([9, 9, 7, 7, 6, 3, -3, -3, -5]))

#kth element of grammer (first row has '0'; every subsequent row is based on previous row where 0 is replaced by 01 and 1 is replaced by 10)
#first half of each row is same as previous row and 2nd half is NOT of first half
# print n rows
def print_kth_element_grammer(n):
    if n == 1:
        return '0'
    current = ""
    for i in print_kth_element_grammer(n-1):
        current += str((1-int(i)))

    return print_kth_element_grammer(n-1) + current

print(print_kth_element_grammer(4))

def find_kth_element_grammar(n, k):
    if n == 1:
        return 0
    mid = 2**(n-2)
    if k <= mid:
        return find_kth_element_grammar(n-1, k)
    else:
        return 1 - find_kth_element_grammar(n-1, k - mid)
print(find_kth_element_grammar(3,3))

# arrangin n queens on a nXn chess board so that no queen is in danger from any other queen
def isSafe(row, col, board, n):
    i = row - 1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i -= 1
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
def n_queens_helper(row, n, board):
    if row == n:
        print(board)
        return
    for col in range(n):
        if isSafe(row, col, board, n):
            board[row][col] = 1
            n_queens_helper(row+1, n, board)
            board[row][col] = 0
    return
def n_queens(n):
    board = [[0 for j in range(n)] for i in range(n)]
    n_queens_helper(0, n, board)

n_queens(8)

#sudoku solver
def is_valid(board, row, col, num):
    # Check row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # 0 represents an empty cell
                # Try placing numbers 1-9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        
                        if solve_sudoku(board):  # Recursively solve the rest
                            return True
                        
                        # Backtrack
                        board[row][col] = 0
                
                return False  # No valid number found for this cell

    return True  # Puzzle solved
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_board(puzzle)

if solve_sudoku(puzzle):
    print("\nSolved Sudoku:")
    print_board(puzzle)
else:
    print("\nNo solution exists.")

# paths for rat in a maze
def printPathHelper(x,y,maze,n,solution):
    if x == n-1 and y == n-1:
        solution[x][y] = 1
        print(solution)
        return
    if x < 0 or y < 0 or x>=n or y >= n or maze[x][y] == 0 or solution[x][y] == 1:
        return
    solution[x][y] = 1
    printPathHelper(x+1, y, maze, n, solution)
    printPathHelper(x, y+1, maze, n, solution)
    printPathHelper(x-1, y, maze, n, solution)
    printPathHelper(x, y-1, maze, n, solution)
    solution[x][y] = 0
    return

def printPath(maze):
    n = len(maze)
    solution=[[0 for j in range(n)] for i in range(n)]
    printPathHelper(0,0,maze,n,solution)

n = int(input())
maze = []
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)
printPath(maze)

