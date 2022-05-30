"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    x_count = 0
    o_count = 0
    for row in board:
        for sqr in row:
            if sqr == X:
                x_count += 1
            elif sqr == O:
                o_count += 1
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(3):
        for col in range(3):
            square = board[row][col]
            if square == EMPTY:
                actions.append((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_cp = copy.deepcopy(board)
    if board_cp[action[0]][action[1]] == EMPTY:
        board_cp[action[0]][action[1]] = player(board)
        return (board_cp)
    else:
        raise ValueError("Wrong action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    count = 0

    # Check rows for winner
    for row in range(3):
        for col in range(3):
            if count == 3:
                return winner
            if ((board[row][col] != EMPTY and count == 0) or
                    (count > 0 and board[row][col] == winner)):
                winner = board[row][col]
                count += 1
            else:
                count = 0
                winner = None
                break

    # Check colomns for winner
    for col in range(3):
        for row in range(3):
            if count == 3:
                return winner
            if ((board[row][col] != EMPTY and count == 0) or
                    (count > 0 and board[row][col] == winner)):
                winner = board[row][col]
                count += 1
            else:
                count = 0
                winner = None
                break

    # Check diagonal
    col = -1
    step = 1
    for side in range(2):
        for row in range(3):
            if count == 3:
                return winner
            if ((board[row][col + step] != EMPTY and count == 0) or
                    (count > 0 and board[row][col + step] == winner)):
                winner = board[row][col + step]
                count += 1
                col += step
            else:
                count = 0
                winner = None
                col = 3
                step = -1
                break
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
   


def max_value(board):
    """
    Recursively check all possible outcomes and returns max score
    """

    


def min_value(board):
    """
    Recursively check all possible outcomes and returns min score
    """
   


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
   