# problem: this aint your grandpas checkerboard

def checkerboard(board, grid_length):
    # check rows
    for i in range(grid_length):
        row_white = 0
        consecutive_num = 0
        prev_row_val = None
        for j in range(grid_length):
            if board[i][j] == "W":
                row_white= row_white + 1
            if prev_row_val is None or prev_row_val != board[i][j]:
                prev_row_val = board[i][j]
                consecutive_num = 1
            else:
                consecutive_num = consecutive_num + 1
            if consecutive_num >= 3:
                print(0)
                return
        if row_white != grid_length/2:
            print(0)
            return

    # check columnS
    for i in range(grid_length):
        col_white = 0
        consecutive_num = 0
        prev_row_val = None
        for j in range(grid_length):
            if board[j][i] == "W":
                col_white = col_white + 1
            if prev_row_val is None or prev_row_val != board[j][i]:
                prev_row_val = board[j][i]
                consecutive_num = 1
            else:
                consecutive_num = consecutive_num + 1
            if consecutive_num >= 3:
                print(0)
                return
        if col_white != grid_length / 2:
            print(0)
            return
    print(1)

if __name__ == '__main__':
    # SHOULD RETURN 1 (CORRECT)
    board = [['W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'], ['B', 'W', 'B', 'W']]
    # board = [['W','W','B','B','W','B'],['B','B','W','W','B','W'],['W','B','W','B','W','B'],['B','W','B','W','B','W'],['B','W','B','B','W','W'],['W','B','W','W','B','B']]

    # SHOULD RETURN 0 (WRONG)
    # board = [['B','W','W','B'],['B','W','B','B'],['W','B','B','W'],['W','B','W','W']]
    #board = [['B','W','B','W','W','B'],['W','B','W','B','W','B'],['W','B','B','W','B','W'],['B','B','W','B','W','W'],['B','W','W','B','B','W'],['W','W','B','W','B','B']]
    checkerboard(board, len(board))

