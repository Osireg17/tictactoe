

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    
    
    Xcount = 0
    Ocount = 0
    
    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)
        
    if Xcount <= Ocount:
        return X
    else:
        return O
    
    


def actions(board):
    
    
    possible_actions = set()
    
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((row_index, col_index))
    
    return possible_actions
    


def result(board, action):
    
    player_turn = player(board)
    
    new_board = deepcopy(board)
    i,j = action
    
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    else:
        new_board[i][j] = player_turn
    
    return new_board
    
    


def winner(board):

    for player in (X, O):
        for row in board:
            if row == [player] * 3:
                return player
            
        for col in range(3):
            column = [board[x][col] for x in range(3)]
            if column == [player] * 3:
                return player
            
        if[board[col][col] for col in range(3)] == [player] * 3:
            return player
        elif [board[col][~col] for col in range(3)] == [player] * 3:
            return player
    
    return None


def terminal(board):

    if winner(board) != None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            val = -5
            for action in actions(board):
                new_val= min_value(result(board, action))[0]
                if new_val > val:
                    val = new_val
                    optimal_move = action
            return val, optimal_move
        
    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            val = 5
            for action in actions(board):
                new_val = max_value(result(board, action))[0]
                if new_val < val:
                    val = new_val
                    optimal_move = action
            return val, optimal_move
    
    current_player = player(board)
    
    if terminal(board):
        return None
    
    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
