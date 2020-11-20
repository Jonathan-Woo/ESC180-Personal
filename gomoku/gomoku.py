"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

from typing import Sequence

def is_empty(board):
    if make_empty_board(len(board)) == board:
        return True
    return False

def within_board(y, x):
    '''Helper function to check if a given y and x is within the board
    '''
    return (y <= 7 and y >= 0 and x <= 7 and x >= 0)
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    colour = board[y_end][x_end]
    bounds = 0
    #Test each side of sequence
    #Since y_end and x_end represent the end of the sequence, 
    #and d_y and d_x are the directions, we can assume that you always
    #add the pattern.
    #first check if the next position is within the board or not
    if not within_board(y_end + d_y, x_end + d_x):
        bounds += 1
    #if that side is within the board, check if the next spot is open
    elif board[y_end + d_y][x_end + d_x] != " ":
        bounds += 1
    #now check the other side of the sequence for the same results
    #remember that you are checking the spot following the pattern
    #after the exisitng end.
    if not within_board(y_end - (d_y * length), x_end - (d_x * length)):
        bounds += 1
    elif board[y_end - (d_y * length)][x_end - (d_y * length)] != " ":
        bounds += 1
    
    #now that we have checked both sides of the pattern and determined the bounds.
    #the pattern condition is based on how many bounds there are
    if bounds == 2:
        return "CLOSED"
    elif bounds == 1:
        return "SEMIOPEN"
    return "OPEN"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''Analyzes a row starting from (y_start, x_start) and goes in the direction (d_y, d_x).
    Returns a tuple whose first element is the number of open sequences of colour col
    of length length in the row R, and whose second element is the number of semi-open sequences.
    '''
    #finds the length of the row to first determine how many items to go through based on the
    #direction 
    if d_y == 1 and d_x == -1:
        row_length = min(x_start + 1, 8 - y_start)
    elif d_y == 1 and d_x == 1:
        row_length = min(8 - x_start, 8 - y_start)
    else:
        row_length = 8
    #Iterates through the board starting from y_start and x_start following d_y and d_x.
    #Finds every sequence where the next colour does not match the previous colour.
    #In this case, that sequence must also match the colour col.
    pre_colour = board[y_start][x_start]
    cur_colour = board[y_start][x_start]
    sequences = []
    seq_length = 0
    for i in range(row_length):
        cur_colour = board[y_start + (d_y * i)][x_start + (d_x * i)]
        #this if statement is quite restricting and complicated because there are
        #several things that must be true in order for us to analyze that sequence's
        #bounds. It must be of colour col, of length length and be the end of a sequence.
        if pre_colour != cur_colour and pre_colour == col and seq_length == length:
            #once we know that this is an endpoint in the row, we append the position of the previous 
            #index because the current index is already the index of a different colour
            sequences.append([y_start + (d_y * (i - 1)), x_start + (d_x * (i - 1))])
            seq_length = 0
        #if it has reaches the end of the row, it should be marked an endpoint
        #instead of checking for the previous colour, we check the current colour becuase 
        #there is no more indices to check. It must be the same colour as the previous index
        #because if the previous index were different, it would be caught in the first if statement. 
        elif i == (row_length - 1) and cur_colour == col and seq_length == (length - 1):
            #if we are at the end of the row, we need the position of the index intstead of the previous
            #one because the sequence terminiated because of row length, not a different colour.
            sequences.append([y_start + (d_y * i), x_start + (d_x * i)])
        elif pre_colour != cur_colour:
            seq_length = 0
        pre_colour = cur_colour
        seq_length += 1
    
    #after getting the colour and endpoints, we can use the is_bounded function to check
    #each endpoint since we already know direction as d_y and d_x.
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(sequences)):
        if is_bounded(board, sequences[i][0], sequences[i][1], length, d_y, d_x) == "OPEN":
            open_seq_count += 1
        elif is_bounded(board, sequences[i][0], sequences[i][1], length, d_y, d_x) == "SEMIOPEN":
            semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    '''Checks all rows, columns and diagonals in the board to check for all number of semi open
    and open sequences of colour col and length length. 
    Always starts at an edge.
    '''
    seq_data = []
    #Using detect_row for all rows moving left to right
    for row in range(len(board)):
        seq_data.append(detect_row(board, col, row, 0, length, 0, 1))

    #Using detect_row for all columns 
    for column in range(len(board[0])):
        seq_data.append(detect_row(board, col, 0, column, length, 1, 0))

    #Using detect_row for all diagonals except for the longest diagonal (to avoid double counting)
    #I anticipate that length >= 2 so I don't check corners where length = 1
    for row_column in range(1, len(board) - 1):
        #top right to bottom left
        seq_data.append(detect_row(board, col, 0, row_column, length, 1, -1))
        seq_data.append(detect_row(board, col, row_column, 7, length, 1, -1))

        #top left to bottom right
        seq_data.append(detect_row(board, col, 0, row_column, length, 1, 1))
        seq_data.append(detect_row(board, col, row_column, 0, length, 1, 1))

    #Using detect_row for the longest diagonals
    seq_data.append(detect_row(board, col, 0, 0, length, 1, 1))
    seq_data.append(detect_row(board, col, 0, 7, length, 1, -1))
    
    #now analyze the data from seq_data which containts tuples of all open sequences and semi open
    #sequences.
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(seq_data)):
        open_seq_count += seq_data[i][0]
        semi_open_seq_count += seq_data[i][1]
    
    return open_seq_count, semi_open_seq_count

def search_max(board):
    '''
    '''
    #now loop through rows and columns of the temporary board while inputting "b" for 
    #all empty positions one at a time. Test the score and save the position if it's the highest. 
    #then remove the temporary move and repeat.
    prev_score = float("-inf")
    move_y, move_x = None, None
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == " ":
                board[row][column] = "b"
                if score(board) > prev_score:
                    prev_score = score(board)
                    move_y = row
                    move_x = column
                board[row][column] = " "
    return move_y, move_x

def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_full(board):
    '''Helper function that returns True if the board is full.
    '''
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == " ":
                return False
    return True

def check_sequence(board, length, col):
    '''Checks if a sequence of length length exists on the board board.
    '''
    #There are 4 possible directions
    #We must test each element in board on whether they follow the direction
    #for length length
    
    #Goes through the entire board at each position and checks if 
    #a sequence of length length is in the board.
    
    for i in range(4):
        if i == 0:
            d_y = 1
            d_x = 0
        elif i == 1:
            d_y = 0
            d_x = 1
        elif i == 2:
            d_y = 1
            d_x = -1
        else:
            d_y = 1
            d_x = 1
    
        #initialize pre_col and cur_col
        pre_col = col
        cur_col = col
    
        for row in range(len(board)):
            for column in range(len(board[0])):
                for seq_length in range(length):
                    cur_col = board[row + (d_y * seq_length)][column + (d_x * seq_length)]
                    if cur_col != pre_col:
                        break
                    if cur_col == pre_col and seq_length == length - 1:
                        return True
                    pre_col = cur_col
    
    return False

def is_win(board):
    '''determines the current status of the game
    returns one of:
    "White won" "Black won" "Draw" "Continue playing"
    Draw is only returned if the board is full
    '''
    #Checks if the board is full.
    if is_full(board):
        return "Draw"

    #Uses helper function check_sequence() to test if a sequence of 
    #length 5 exists in the board for both b and w
    if check_sequence(board, 5, "b"):
        return "Black won"
    elif check_sequence(board, 5, "w"):
        return "White won"
    
    #if the board isn't full and neither player has won, returns
    #"Continue playing"
    return "Continue playing"

def print_board(board):
    '''Prints out the Gomoku board.
    '''
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board):
    '''Prints the number of open and semi-open rows for white and black.
    '''
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
    
def play_gomoku(board_size):
    '''Allows user to play against a computer on a square board size
    board_size x board_size.
    '''
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
                
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    '''Adds the sequence of stones of colour col of length length to board starting
    from location (y,x) and moving in the direction (d_y, d_x).
    '''
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 0, 1, 1, 5, "b")
    print(is_win(board))
    