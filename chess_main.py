
# Chess game project

# Board

import random
import string
import math
import numpy
import win_condition
import move_check
import pieces
import board_evaluation
import board_operations

   
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

board_coord_assigned = {
    
    "a8" : board[0][0], "b8" : board[0][1], "c8" : board[0][2], "d8" : board[0][3], "e8" : board[0][4], "f8" : board[0][5], "g8" : board[0][6], "h8" : board[0][7],
    "a7" : board[1][0], "b7" : board[1][1], "c7" : board[1][2], "d7" : board[1][3], "e7" : board[1][4], "f7" : board[1][5], "g7" : board[1][6], "h7" : board[1][7],
    "a6" : board[2][0], "b6" : board[2][1], "c6" : board[2][2], "d6" : board[2][3], "e6" : board[2][4], "f6" : board[2][5], "g6" : board[2][6], "h6" : board[2][7],
    "a5" : board[3][0], "b5" : board[3][1], "c5" : board[3][2], "d5" : board[3][3], "e5" : board[3][4], "f5" : board[3][5], "g5" : board[3][6], "h5" : board[3][7],
    "a4" : board[4][0], "b4" : board[4][1], "c4" : board[4][2], "d4" : board[4][3], "e4" : board[4][4], "f4" : board[4][5], "g4" : board[4][6], "h4" : board[4][7],
    "a3" : board[5][0], "b3" : board[5][1], "c3" : board[5][2], "d3" : board[5][3], "e3" : board[5][4], "f3" : board[5][5], "g3" : board[5][6], "h3" : board[5][7],
    "a2" : board[6][0], "b2" : board[6][1], "c2" : board[6][2], "d2" : board[6][3], "e2" : board[6][4], "f2" : board[6][5], "g2" : board[6][6], "h2" : board[6][7],
    "a1" : board[7][0], "b1" : board[7][1], "c1" : board[7][2], "d1" : board[7][3], "e1" : board[7][4], "f1" : board[7][5], "g1" : board[7][6], "h1" : board[7][7],

    }


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


def standardGame():

    current_board = board_operations.test_board()

    print("The game has begun!\n")

    player_white = ""
    player_black = ""

    print("Who plays white\n?")

    player_white = input()

    player_white = str(player_white)
    
    print("Who plays black?\n?")

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

    # def check_turn(turn):
        
    #     if turn == "white":
    #         turn == "black"
        
    #     elif turn == "black":
    #         turn == "white"
        
    #     return turn
    
    # while win_check_white() != 0 and win_check_black() != 0:


    count = 0 

    #while win condition not completed
    
    while count<200:
                
        if turn == "white":

            move = move_check.input_move_white(player_white, board_coord, turn, current_board)

            current_board = board_operations.make_move(move, current_board)

            black_king_coord = board_evaluation.get_black_king_coord(current_board)

            all_white_attacks = board_evaluation.get_all_white_attacks(current_board)
            
            if (black_king_coord in all_white_attacks):

                if board_evaluation.opponent_has_no_legal_moves(turn, current_board):

                    print(player_white + " wins!")
                    break                
            
            else:
                if win_condition.is_draw(turn, current_board): 
                    print("Draw!")
                    break


            turn = "black"

        elif turn == "black":

            move = move_check.input_move_black(player_black, board_coord, turn, current_board)

            current_board = board_operations.make_move(move, current_board)

            white_king_coord = board_evaluation.get_white_king_coord(current_board)

            all_black_attacks = board_evaluation.get_all_black_attacks(current_board)
            
            if (white_king_coord in all_black_attacks):

                if board_evaluation.opponent_has_no_legal_moves(turn, current_board):

                    print(player_black + " wins!")
                    break                
            
            else:
                if win_condition.is_draw(turn, current_board): 
                    print("Draw!")
                    break

            turn = "white"    
        
        count += 1

        show_board_status(current_board)    

standardGame() 