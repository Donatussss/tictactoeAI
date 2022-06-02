"""
Tic Tac Toe Player
"""
import copy
import math
# import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counts = get_count(board)

    if is_initial_state(board) or counts[0] == counts[1]:
        return X

    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        default_action_set = {0, 0}
        return default_action_set

    finalset = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                finalset.add((i, j))

    return finalset


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    the_player = player(result_board)

    if result_board[action[0]][action[1]] is None:
        result_board[action[0]][action[1]] = the_player
    else:
        raise Exception("Sorry, that is not a valid move")

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    col1 = [board[0][0], board[1][0], board[2][0]]
    col2 = [board[0][1], board[1][1], board[2][1]]
    col3 = [board[0][2], board[1][2], board[2][2]]
    row1 = copy.deepcopy(board[0])
    row2 = copy.deepcopy(board[1])
    row3 = copy.deepcopy(board[2])
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[0][2], board[1][1], board[2][0]]

    checklists = [col1, col2, col3, row1, row2, row3, diagonal1, diagonal2]
    winilistx = [X, X, X]
    winilistO = [O, O, O]

    for i in checklists:
        if i == winilistx:
            return X
        elif i == winilistO:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or is_full(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # X is the maximizer
    # O is the minimizer

    if is_initial_state(board):
        all_actions = list(actions(board))
        return random.choice(all_actions)

    # if is_initial_state(board):
    #     all_actions = list(actions(board))
    #     return all_actions[0]

    if len(actions(board)) == 0:
        return None

    the_player = player(board)
    the_actions = []
    utility_vals = []

    for action in actions(board):
        the_result = result(board, action)
        utility_vals.append(minimax_calc(the_result))
        the_actions.append(action)

    if the_player == X:
        max_val = max(utility_vals)
        max_val_index = utility_vals.index(max_val)
        the_action = the_actions[max_val_index]
        return the_action

    elif the_player == O:
        min_val = min(utility_vals)
        min_val_index = utility_vals.index(min_val)
        the_action = the_actions[min_val_index]
        return the_action


def minimax_calc(board):

    if terminal(board):
        return utility(board) * get_empty(board)
        # return utility(board)

    utility_vals = []

    # Get player
    the_player = player(board)
    the_actions = []

    for action in actions(board):
        the_result = result(board, action)
        utility_vals.append(minimax_calc(the_result))
        the_actions.append(action)

    if the_player == X:
        max_val = max(utility_vals)
        max_val_index = utility_vals.index(max_val)
        the_action = the_actions[max_val_index]
        return max_val

    elif the_player == O:
        min_val = min(utility_vals)
        min_val_index = utility_vals.index(min_val)
        the_action = the_actions[min_val_index]
        return min_val


def is_initial_state(board):
    condition = True

    for i in board:
        for j in i:
            if j is not None:
                return False

    return condition


def get_count(board):
    x_count = 0
    o_count = 0

    for i in board:
        for j in i:
            if j == "X":
                x_count += 1

            elif j == "O":
                o_count += 1

    return [x_count, o_count]


def is_full(board):
    condition = True

    for i in board:
        for j in i:
            if j is None:
                return False

    return condition


def get_empty(board):
    empty_count = 1

    for i in board:
        for j in i:
            if j is None:
                empty_count += 1

    return empty_count
