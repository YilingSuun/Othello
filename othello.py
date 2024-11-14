# CSCI 1913, Spring 2023, Project 1
# Student Names:
# Yiling Sun
import random


def match_left_horizontal_lines(board, row, col, color):
    """This function check if the straight lines starting from row,col and
    continuing horizontally, in left direction start with an opponent’s
    token and end with a token matching the color argument.
    """
    current_row, current_col = row, col - 1
    while current_col > 0 and not board[current_row][current_col] == 0:
        if board[current_row][current_col] == 1:
            current_col -= 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_col = 0
        elif board[current_row][current_col] == 2:
            current_col -= 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_col = 0
    return False


def match_right_horizontal_lines(board, row, col, color):
    """This function check if the straight lines starting from row,col and
    continuing horizontally, in right direction start with an opponent’s
    token and end with a token matching the color argument.
    """
    current_row, current_col = row, col + 1
    while (current_col < len(board[0]) - 1 and
           not board[current_row][current_col] == 0):
        if board[current_row][current_col] == 1:
            current_col += 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_col = len(board[0]) - 1
        elif board[current_row][current_col] == 2:
            current_col += 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_col = len(board[0]) - 1
    return False


def match_up_vertical_lines(board, row, col, color):
    """This function check if the straight lines starting from row, col
    and continuing vertically, in up direction start with an opponent’s
    token and end with a token matching the color argument.
    """
    current_row, current_col = row - 1, col
    while current_row > 0 and not board[current_row][current_col] == 0:
        if board[current_row][current_col] == 1:
            current_row -= 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_col = 0
        elif board[current_row][current_col] == 2:
            current_row -= 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_col = 0
    return False


def match_down_vertical_lines(board, row, col, color):
    """This function check if the straight lines starting from row, col
    and continuing vertically, in down direction start with an opponent’s
    token and end with a token matching the color argument.
    """
    current_row, current_col = row + 1, col
    while (current_row < len(board) - 1 and
           not board[current_row][current_col] == 0):
        if board[current_row][current_col] == 1:
            current_row += 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_row = len(board) - 1
        elif board[current_row][current_col] == 2:
            current_row += 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_row = len(board) - 1
    return False


def match_left_up_line(board, row, col, color):
    """This function check if the straight lines starting from row, col
    and continuing diagonally, in left up direction start with an
    opponent’s token and end with a token matching the color argument.
    """
    current_row, current_col = row - 1, col - 1
    while (current_col > 0 and
           current_row > 0 and not
           board[current_row][current_col] == 0):
        if board[current_row][current_col] == 1:
            current_col -= 1
            current_row -= 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_col = 0
        elif board[current_row][current_col] == 2:
            current_col -= 1
            current_row -= 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_col = 0
    return False


def match_right_up_line(board, row, col, color):
    """This function check if the straight lines starting from row, col
    and continuing diagonally, in right up direction start with an
    opponent’s token and end with a token matching the color argument.
    """
    current_row, current_col = row - 1, col + 1
    while (current_row > 0 and
           current_col < len(board[0]) - 1 and not
           board[current_row][current_col] == 0):
        if board[current_row][current_col] == 1:
            current_col += 1
            current_row -= 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_row = 0
        elif board[current_row][current_col] == 2:
            current_col += 1
            current_row -= 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_row = 0
    return False


def match_left_down_line(board, row, col, color):
    """This function check if the straight lines starting from row, col
    and continuing diagonally, in left down direction start with an
    opponent’s token and end with a token matching the color argument.
    """
    current_row, current_col = row + 1, col - 1
    while (current_row < len(board) - 1 and
           current_col > 0 and not
           board[current_row][current_col] == 0):
        if board[current_row][current_col] == 1:
            current_col -= 1
            current_row += 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_col = 0
        elif board[current_row][current_col] == 2:
            current_col -= 1
            current_row += 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_col = 0
    return False


def match_right_down_line(board, row, col, color):
    """This function check if the straight lines starting from row, col
    and continuing diagonally, in right down direction start with an
    opponent’s token and end with a token matching the color argument.
    """
    current_row, current_col = row + 1, col + 1
    while (current_col < len(board[0]) - 1 and
           current_row < len(board) - 1 and not
           board[current_row][current_col] == 0):
        if board[current_row][current_col] == 1:
            current_col += 1
            current_row += 1
            if board[current_row][current_col] == 2:
                if color == "black":
                    return True
                else:
                    current_col = len(board[0]) - 1
        elif board[current_row][current_col] == 2:
            current_col += 1
            current_row += 1
            if board[current_row][current_col] == 1:
                if color == "white":
                    return True
                else:
                    current_col = len(board[0]) - 1
    return False


def is_valid_move(board, row, col, color):
    """The function check if a token in row, col is valid move and
    should return True if the specified row, column is a "valid"
    move for the given color and False in all other cases.
    """
    if not board[row][col] == 0:
        return False
    else:
        if (match_left_horizontal_lines(board, row, col, color) or
                match_right_horizontal_lines(board, row, col, color) or
                match_up_vertical_lines(board, row, col, color) or
                match_down_vertical_lines(board, row, col, color) or
                match_left_down_line(board, row, col, color) or
                match_left_up_line(board, row, col, color) or
                match_right_down_line(board, row, col, color) or
                match_right_up_line(board, row, col, color)):
            return True
        return False


def get_valid_moves(board, color):
    """This function take in a board state and a color and return
    a list of all valid moves, where each move is a tuple of row, column
    values in the list
    """
    valid_moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if is_valid_move(board, i, j, color):
                valid_moves.append((i, j))
    return valid_moves


def select_next_play_random(board, color):
    """This function take in a board state and color and return a
    randomly selected move from the list of valid moves, returned
    as a tuple of row, column index values.
    """
    valid_move = get_valid_moves(board, color)
    rand_num = random.randrange(len(valid_move))
    return valid_move[rand_num]


def select_next_play_ai(board, color):
    """This function take in a board state and a color and return a
    selected move from the list of valid moves, returned as a tuple
    of row, column index values.
    """
    return get_valid_moves(board, color)[0]


def select_next_play_human(board, color):
    """This function take in a board state and a color and return a
    move selected by a player from the list of valid moves, returned
    as a tuple of row, column index values. If the player picks an
    invalid move it must re-prompt them until a valid move is chosen.
    """
    row = int(input("Select a row: "))
    column = int(input("Select a column: "))
    # Check if the input is a valid move.
    while not (row, column) in get_valid_moves(board, color):
        print("Invalid choice")
        row = int(input("Select a row: "))
        column = int(input("Select a column: "))
    return row, column


def get_board_as_string(board):
    """ This function returns the current board state as a string.
    """
    board_str = "  "
    # Print the first line of numbers
    for i in range(len(board[0])):
        if i < 10:
            board_str += " " + str(i)
        # If the indexes of the rows are 10 or larger, print its unit digit.
        else:
            board_str += " " + str(i % 10)
    # Print the middle lines
    for i in range(len(board)):
        board_str += "\n  +"
        for j in range(len(board[0])):
            board_str += "-+"
        # If the indexes of the columns larger than 9, print its unit digit.
        if i < 10:
            board_str += f"\n{i} "
        else:
            board_str += f"\n{i % 10} "
        for j in range(len(board[0])):
            board_str += "| "
            # Print white and black tokens
            if board[i][j] == 1:
                board_str = board_str[:-1]
                board_str += '\u25CB'
            if board[i][j] == 2:
                board_str = board_str[:-1]
                board_str += '\u25CF'
        board_str += "|"
    # Print the last line of "+-"
    board_str += "\n  +"
    for i in range(len(board[0])):
        board_str += "-+"

    return board_str


def set_up_board(width, height):
    """This function takes two integers, width and height, and return a
    list of size height, which contains a sublist of length width filled
    with zeros. The first 4 tokens (2 black and 2 white) are placed in
    the center of the board. As the game plays those zeros should become 1
    if there is a white token there and 2 if there is a black token there.
    """
    size_lst = []
    for i in range(height):
        size_lst.append([])
        for j in range(width):
            size_lst[i].append(0)

    size_lst[height // 2][width // 2] = 1
    size_lst[height // 2 - 1][width // 2 - 1] = 1
    size_lst[height // 2 - 1][width // 2] = 2
    size_lst[height // 2][width // 2 - 1] = 2

    return size_lst


def flip_black(board, row, col):
    """This function determining the lines of opponent tokens"black"
    to "flip" when a move is made and flip the opponent's black tokens
    """
    if match_left_horizontal_lines(board, row, col, "white"):
        current_col = col - 1
        while board[row][current_col] == 2:
            board[row][current_col] = 1
            current_col -= 1
    if match_right_horizontal_lines(board, row, col, "white"):
        current_col = col + 1
        while board[row][current_col] == 2:
            board[row][current_col] = 1
            current_col += 1
    if match_up_vertical_lines(board, row, col, "white"):
        current_row = row - 1
        while board[current_row][col] == 2:
            board[current_row][col] = 1
            current_row -= 1
    if match_down_vertical_lines(board, row, col, "white"):
        current_row = row + 1
        while board[current_row][col] == 2:
            board[current_row][col] = 1
            current_row += 1
    if match_left_up_line(board, row, col, "white"):
        current_row, current_col = row - 1, col - 1
        while board[current_row][current_col] == 2:
            board[current_row][current_col] = 1
            current_row -= 1
            current_col -= 1
    if match_right_up_line(board, row, col, "white"):
        current_row, current_col = row - 1, col + 1
        while board[current_row][current_col] == 2:
            board[current_row][current_col] = 1
            current_row -= 1
            current_col += 1
    if match_left_down_line(board, row, col, "white"):
        current_row, current_col = row + 1, col - 1
        while board[current_row][current_col] == 2:
            board[current_row][current_col] = 1
            current_row += 1
            current_col -= 1
    if match_right_down_line(board, row, col, "white"):
        current_row, current_col = row + 1, col + 1
        while board[current_row][current_col] == 2:
            board[current_row][current_col] = 1
            current_row += 1
            current_col += 1


def flip_white(board, row, col):
    """This function determining the lines of opponent tokens "white"
    to "flip" when a move is made and flip the opponent's white tokens
    """
    if match_left_horizontal_lines(board, row, col, "black"):
        current_col = col - 1
        while board[row][current_col] == 1:
            board[row][current_col] = 2
            current_col -= 1
    if match_right_horizontal_lines(board, row, col, "black"):
        current_col = col + 1
        while board[row][current_col] == 1:
            board[row][current_col] = 2
            current_col += 1
    if match_up_vertical_lines(board, row, col, "black"):
        current_row = row - 1
        while board[current_row][col] == 1:
            board[current_row][col] = 2
            current_row -= 1
    if match_down_vertical_lines(board, row, col, "black"):
        current_row = row + 1
        while board[current_row][col] == 1:
            board[current_row][col] = 2
            current_row += 1
    if match_left_up_line(board, row, col, "black"):
        current_row, current_col = row - 1, col - 1
        while board[current_row][current_col] == 1:
            board[current_row][current_col] = 2
            current_row -= 1
            current_col -= 1
    if match_right_up_line(board, row, col, "black"):
        current_row, current_col = row - 1, col + 1
        while board[current_row][current_col] == 2:
            board[current_row][current_col] = 1
            current_row -= 1
            current_col += 1
    if match_left_down_line(board, row, col, "black"):
        current_row, current_col = row + 1, col - 1
        while board[current_row][current_col] == 1:
            board[current_row][current_col] = 2
            current_row += 1
            current_col -= 1
    if match_right_down_line(board, row, col, "black"):
        current_row, current_col = row + 1, col + 1
        while board[current_row][current_col] == 1:
            board[current_row][current_col] = 2
            current_row += 1
            current_col += 1


def human_vs_random():
    """This function is a game that played by a human and a random until
    a winner is found. It has no input and return 1 if player 1 won and
    2 if player 2 won and 0 if it was a tie.
    """
    board = set_up_board(8, 8)
    # Player 1's turn if it has valid moves
    while not get_valid_moves(board, "white") == []:
        print("Player 1's Turn")
        print(get_board_as_string(board))
        location = select_next_play_human(board, "white")
        row = location[0]
        col = location[1]
        board[row][col] = 1
        flip_black(board, row, col)
        # Player 2's turn if it has valid moves
        if not get_valid_moves(board, "black") == []:
            print("Player 2's Turn")
            print(get_board_as_string(board))
            location = select_next_play_random(board, "black")
            row = location[0]
            col = location[1]
            board[row][col] = 2
            flip_white(board, row, col)
    # When there are no valid move for each player, the game end.
    print("Final Board State")
    print(get_board_as_string(board))
    # Calculate the total tokens each player had won.
    sum_white = 0
    sum_black = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                sum_white += 1
            if board[i][j] == 2:
                sum_black += 1
    # Find the winner who win the most tokens
    if sum_white > sum_black:
        print("Player 1 Wins")
        return 1
    elif sum_black > sum_white:
        print("Player 2 Wins")
        return 2
    else:
        print("It was a tie")
        return 0


def random_vs_random():
    """This function is a game that played by two random condition until
    a winner is found. It has no input and return 1 if player 1 won and
    2 if player 2 won and 0 if it was a tie.
    """
    board = set_up_board(8, 8)
    # Player 1's turn if it has valid moves
    while not get_valid_moves(board, "white") == []:
        print("Player 1's Turn")
        print(get_board_as_string(board))
        location = select_next_play_random(board, "white")
        row = location[0]
        col = location[1]
        board[row][col] = 1
        flip_black(board, row, col)
        # Player 2's turn if it has valid moves
        if not get_valid_moves(board, "black") == []:
            print("Player 2's Turn")
            print(get_board_as_string(board))
            location = select_next_play_random(board, "black")
            row = location[0]
            col = location[1]
            board[row][col] = 2
            flip_white(board, row, col)
    # When there are no valid move for each player, the game end.
    print("Final Board State")
    print(get_board_as_string(board))
    # Calculate the total tokens each player had won.
    sum_white = 0
    sum_black = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                sum_white += 1
            if board[i][j] == 2:
                sum_black += 1
    # Find the winner who win the most tokens
    if sum_white > sum_black:
        print("Player 1 Wins")
        return 1
    elif sum_black > sum_white:
        print("Player 2 Wins")
        return 2
    else:
        print("It was a tie")
        return 0


def ai_vs_random():
    """This function is a game that played by an AI and a random until
    a winner is found. It has no input and return 1 if player 1 won and
    2 if player 2 won and 0 if it was a tie.
    """
    board = set_up_board(8, 8)
    # Player 1's turn if it has valid moves
    while not get_valid_moves(board, "white") == []:
        print("Player 1's Turn")
        print(get_board_as_string(board))
        location = select_next_play_ai(board, "white")
        row = location[0]
        col = location[1]
        board[row][col] = 1
        flip_black(board, row, col)
        # Player 2's turn if it has valid moves
        if not get_valid_moves(board, "black") == []:
            print("Player 2's Turn")
            print(get_board_as_string(board))
            location = select_next_play_random(board, "black")
            row = location[0]
            col = location[1]
            board[row][col] = 2
            flip_white(board, row, col)
    # When there are no valid move for each player the game end
    print("Final Board State")
    print(get_board_as_string(board))
    # Calculate the total tokens each player had won.
    sum_white = 0
    sum_black = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                sum_white += 1
            if board[i][j] == 2:
                sum_black += 1
    # Find the winner who win the most tokens
    if sum_white > sum_black:
        print("Player 1 Wins")
        return 1
    elif sum_black > sum_white:
        print("Player 2 Wins")
        return 2
    else:
        print("It was a tie")
        return 0
