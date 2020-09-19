
# Chess game project

# Board

import random
import string
import math
import numpy
import win_condition
import move_check
import pieces

# Add a class for pieces
# Add a class for each 

   
board = [
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],   
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
]   

board_coord = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
]

# board_coord_assigned IS NOT USED!

# board_coord_assigned = {
    
#     "a8" : board[0][0], "b8" : board[0][1], "c8" : board[0][2], "d8" : board[0][3], "e8" : board[0][4], "f8" : board[0][5], "g8" : board[0][6], "h8" : board[0][7],
#     "a7" : board[1][0], "b7" : board[1][1], "c7" : board[1][2], "d7" : board[1][3], "e7" : board[1][4], "f7" : board[1][5], "g7" : board[1][6], "h7" : board[1][7],
#     "a6" : board[2][0], "b6" : board[2][1], "c6" : board[2][2], "d6" : board[2][3], "e6" : board[2][4], "f6" : board[2][5], "g6" : board[2][6], "h6" : board[2][7],
#     "a5" : board[3][0], "b5" : board[3][1], "c5" : board[3][2], "d5" : board[3][3], "e5" : board[3][4], "f5" : board[3][5], "g5" : board[3][6], "h5" : board[3][7],
#     "a4" : board[4][0], "b4" : board[4][1], "c4" : board[4][2], "d4" : board[4][3], "e4" : board[4][4], "f4" : board[4][5], "g4" : board[4][6], "h4" : board[4][7],
#     "a3" : board[5][0], "b3" : board[5][1], "c3" : board[5][2], "d3" : board[5][3], "e3" : board[5][4], "f3" : board[5][5], "g3" : board[5][6], "h3" : board[5][7],
#     "a2" : board[6][0], "b2" : board[6][1], "c2" : board[6][2], "d2" : board[6][3], "e2" : board[6][4], "f2" : board[6][5], "g2" : board[6][6], "h2" : board[6][7],
#     "a1" : board[7][0], "b1" : board[7][1], "c1" : board[7][2], "d1" : board[7][3], "e1" : board[7][4], "f1" : board[7][5], "g1" : board[7][6], "h1" : board[7][7],

#     }

# class piece:

#     color = "color"
#     shape = "shape"

#     def __init__(self, color, shape): 
#         self.color = color
#         self.shape = shape

#     def get_avatar(self):

#         avatar = self.color[0] + self.shape[0]

#         return avatar

white_pawn = pieces.piece("white", "pawn")
white_horse = pieces.piece("white", "horse")
white_bishop = pieces.piece("white", "bishop")
white_rook = pieces.piece("white", "rook")
white_queen = pieces.piece("white", "queen")
white_king = pieces.piece("white", "king")

black_pawn = pieces.piece("black", "pawn")
black_horse = pieces.piece("black", "horse")
black_bishop = pieces.piece("black", "bishop")
black_rook = pieces.piece("black", "rook")
black_queen = pieces.piece("black", "queen")
black_king = pieces.piece("black", "king")


def purge_cell(cell):
    
    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + "00"

    return current_cell

# testing purge:

# #print(board)

# board[0][0] = purge_cell(board[0][0])

# #print(board)

def fill_cell(cell, current_piece):

    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + current_piece

    return current_cell

def find_move_coord(indice):

    coord = []

    for i in range(len(board_coord)):

        for j in range(len(board_coord[i])):

            if indice == board_coord[i][j]:

                coord = [i, j]

    return coord

def find_current_piece(move, current_board):

    i = find_move_coord(move[0])[0]
    j = find_move_coord(move[0])[1]

    current_piece = current_board[i][j].split("_")[1]

    return current_piece

def is_your_piece(move, turn, current_board):

    current_piece = find_current_piece(move, current_board)
    
    if turn == "white":
        if current_piece[0] == "w":
            return True
        else:
            return False

    if turn == "black":
        if current_piece[0] == "b":
            return True
        else:
            return False

#board[0][0] = fill_cell(board[0][0], "zz")

#print(board[0][0])

insufficient_material = 0

# def win_check_white():

#     win = 0
    
#     if black_king.legal_move == 0:

#         win = 1

#     return win

# def win_check_black():

#     win = 0
    
#     if white_king.legal_move == 0:

#         win = 1

#     return win 

# def check_material(current_board):

#     if insufficient_material:

#         return True
    
#     else:

#         return False

# def draw_check(current_board):
    
#     draw = 0

#     if check_material(current_board):

#         draw = 1

#     return draw

def standardGame():

    def init_board_standard():

        start_board = board

        for i in range(2, 7):
            for j in range(len(start_board[i])):
                start_board[i][j] = "White_00"

        start_board[0][0] = fill_cell(start_board[0][0], black_rook.get_avatar())
        start_board[0][1] = fill_cell(start_board[0][1], black_horse.get_avatar())
        start_board[0][2] = fill_cell(start_board[0][2], black_bishop.get_avatar())
        start_board[0][3] = fill_cell(start_board[0][3], black_queen.get_avatar())
        start_board[0][4] = fill_cell(start_board[0][4], black_king.get_avatar())
        start_board[0][5] = fill_cell(start_board[0][5], black_bishop.get_avatar())
        start_board[0][6] = fill_cell(start_board[0][6], black_horse.get_avatar())
        start_board[0][7] = fill_cell(start_board[0][7], black_rook.get_avatar())

        start_board[1][0] = fill_cell(start_board[1][0], black_pawn.get_avatar())
        start_board[1][1] = fill_cell(start_board[1][1], black_pawn.get_avatar())
        start_board[1][2] = fill_cell(start_board[1][2], black_pawn.get_avatar())
        start_board[1][3] = fill_cell(start_board[1][3], black_pawn.get_avatar())
        start_board[1][4] = fill_cell(start_board[1][4], black_pawn.get_avatar())
        start_board[1][5] = fill_cell(start_board[1][5], black_pawn.get_avatar())
        start_board[1][6] = fill_cell(start_board[1][6], black_pawn.get_avatar())
        start_board[1][7] = fill_cell(start_board[1][7], black_pawn.get_avatar())

        start_board[6][0] = fill_cell(start_board[1][0], white_pawn.get_avatar())
        start_board[6][1] = fill_cell(start_board[1][1], white_pawn.get_avatar())
        start_board[6][2] = fill_cell(start_board[1][2], white_pawn.get_avatar())
        start_board[6][3] = fill_cell(start_board[1][3], white_pawn.get_avatar())
        start_board[6][4] = fill_cell(start_board[1][4], white_pawn.get_avatar())
        start_board[6][5] = fill_cell(start_board[1][5], white_pawn.get_avatar())
        start_board[6][6] = fill_cell(start_board[1][6], white_pawn.get_avatar())
        start_board[6][7] = fill_cell(start_board[1][7], white_pawn.get_avatar())

        start_board[7][0] = fill_cell(start_board[0][0], white_rook.get_avatar())
        start_board[7][1] = fill_cell(start_board[0][1], white_horse.get_avatar())
        start_board[7][2] = fill_cell(start_board[0][2], white_bishop.get_avatar())
        start_board[7][3] = fill_cell(start_board[0][3], white_queen.get_avatar())
        start_board[7][4] = fill_cell(start_board[0][4], white_king.get_avatar())
        start_board[7][5] = fill_cell(start_board[0][5], white_bishop.get_avatar())
        start_board[7][6] = fill_cell(start_board[0][6], white_horse.get_avatar())
        start_board[7][7] = fill_cell(start_board[0][7], white_rook.get_avatar())
        
        return start_board

    current_board = init_board_standard()

    print("The game has begun!\n")

    player_white = ""
    player_black = ""

    print("Who plays white\n?")

    player_white = input()

    player_white = str(player_white)
    
    print("who plays black?\n?")

    player_black = input()

    player_black = str(player_black)

    def show_board_status(current_board):

        print("In the black corner: " + player_black)
        print("\n")

        for i in range(len(current_board)):

            print(current_board[i])
            print("\n")
        
        print("In the white corner: " + player_white)
        print("\n")

    show_board_status(current_board)

    turn = "white"

    def check_turn(turn):
        
        if turn == "white":
            turn == "black"
        
        elif turn == "black":
            turn == "white"
        
        return turn
    
    # while win_check_white() != 0 and win_check_black() != 0:

    count = 0 

    #while win condition not completed

   #not_draw = win_condition.is_not_draw()

    while win_condition.is_not_draw():
                
        if turn == "white":

            move = move_check.input_move_white(player_white, board_coord, turn, current_board)
        
            # to implement move_check.make_move() instead

            move = move.split(" ")
          
            i = find_move_coord(move[0])[0]
            j = find_move_coord(move[0])[1]

            current_piece = current_board[i][j].split("_")[1]

            current_board[i][j] = move_check.purge_cell(current_board[i][j])

            x = find_move_coord(move[1])[0]
            y = find_move_coord(move[1])[1]

            current_board[x][y] = move_check.fill_cell(current_board[x][y], current_piece)

            not_draw = win_condition.is_not_draw()

            if win_condition.is_black_king_mated():
                
                show_board_status(current_board)

                print(player_white + " wins!")

                break

            turn = "black"
                                   
        elif turn == "black":

            move = move_check.input_move_black(player_black, board_coord, turn, current_board)

            # to implement move_check.make_move() instead

            move = move.split(" ")
          
            i = find_move_coord(move[0])[0]
            j = find_move_coord(move[0])[1]

            current_piece = current_board[i][j].split("_")[1]

            current_board[i][j] = move_check.purge_cell(current_board[i][j])

            x = find_move_coord(move[1])[0]
            y = find_move_coord(move[1])[1]                      

            current_board[x][y] = move_check.fill_cell(current_board[x][y], current_piece)

            not_draw = win_condition.is_not_draw()

            if win_condition.is_black_king_mated():
                
                show_board_status(current_board)

                print(player_white + " wins!")

                break

            turn = "white"           
            
        show_board_status(current_board)

        if not_draw == False:           

            print("It's a Draw")

    return True


standardGame() 