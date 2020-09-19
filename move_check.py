import pieces
import chess_main
import board_evaluation

def piece_from_coord(move, board_coord):

    move = move.split(" ")

    coord = []

    for i in range(len(board_coord)):

        for j in range(len(board_coord[i])):

            if move[0] == board_coord[i][j]:

                coord = [i, j]

    return coord

def piece_to_coord(move, board_coord):

    move = move.split(" ")

    coord = []

    for i in range(len(board_coord)):

        for j in range(len(board_coord[i])):

            if move[1] == board_coord[i][j]:

                coord = [i, j]

    return coord

def find_current_piece(current_position, current_board):

    i = current_position[0]
    j = current_position[1]

    current_piece = current_board[i][j].split("_")[1]

    return current_piece

def purge_cell(cell):
    
    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + "00"

    return current_cell

def fill_cell(cell, current_piece):

    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + current_piece

    return current_cell

# def find_move_coord(indice):

#     coord = []

#     for i in range(len(board_coord)):

#         for j in range(len(board_coord[i])):

#             if indice == board_coord[i][j]:

#                 coord = [i, j]

#     return coord

def make_move(move, current_board, board_coord):
 
    move = move.split(" ")
    
    i = piece_from_coord(move, board_coord)[0]
    j = piece_from_coord(move, board_coord)[1]

    current_piece = current_board[i][j].split("_")[1]

    current_board[i][j] = purge_cell(current_board[i][j])

    x = piece_to_coord(move, board_coord)[0]
    y = piece_to_coord(move, board_coord)[1]

    current_board[x][y] = fill_cell(current_board[x][y], current_piece)

    return current_board

def get_current_piece_moves(current_position, current_board):

    piece_moves = []
   
    current_piece = find_current_piece(current_position, current_board)
   
    if current_piece == "wp":
        
        piece = pieces.white_pawn()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "wr":
        
        piece = pieces.white_rook()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "wh":
        
        piece = pieces.white_horse()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "wb":
        
        piece = pieces.white_bishop()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "wq":

        piece = pieces.white_queen()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "wk":
        
        piece = pieces.white_king()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "bp":
        
        piece = pieces.black_pawn()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "br":
        
        piece = pieces.black_rook()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "bh":
        
        piece = pieces.black_horse()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "bb":
        
        piece = pieces.black_bishop()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "bq":
        
        piece = pieces.black_queen()
        piece_moves = piece.get_available_moves(current_position, current_board)

    elif current_piece == "bk":
        
        piece = pieces.black_king()
        piece_moves = piece.get_available_moves(current_position, current_board)

    return piece_moves

def get_current_piece_attacks(current_position, current_board):

    piece_attacks = []     

    current_piece = find_current_piece(current_position, current_board)
    
    if current_piece == "wp":
        
        piece = pieces.white_pawn()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "wr":
        
        piece = pieces.white_rook()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "wh":
        
        piece = pieces.white_horse()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "wb":
        
        piece = pieces.white_bishop()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "wq":
        
        piece = pieces.white_queen()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "wk":
        
        piece = pieces.white_king()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "bp":
        
        piece = pieces.black_pawn()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "br":
        
        piece = pieces.black_rook()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "bh":
        
        piece = pieces.black_horse()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "bb":
        
        piece = pieces.black_bishop()
        piece_attacks = piece.get_available_attacks(current_position, current_board)
    
    elif current_piece == "bq":
        
        piece = pieces.black_queen()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    elif current_piece == "wk":
        
        piece = pieces.black_king()
        piece_attacks = piece.get_available_attacks(current_position, current_board)

    return piece_attacks


def is_your_piece(current_position, turn, current_board):

    current_piece = find_current_piece(current_position, current_board)
    
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

def target_not_your_piece(next_position, turn, current_board):

    current_piece = find_current_piece(next_position, current_board)
    
    if turn == "white":
        if current_piece[0] == "w":
            return False
        else:
            return True

    if turn == "black":
        if current_piece[0] == "b":
            return False
        else:
            return True

def is_move_valid(move, board_coord, turn, current_board):

    len_check = 0
    space_check = 0
    first_check = 0
    second_check = 0
    
    if len(move) == 5:
        len_check = 1

        if move[2] == " ":
        
            space_check = 1

            move_start = str(move[0] + move[1])

            move_end = str(move[3] + move[4])

            for i in range(len(board_coord)):

                for j in range(len(board_coord[i])):
                    
                    if move_start == board_coord[i][j]:
                        first_check = 1
                        
            for i in range(len(board_coord)):

                for j in range(len(board_coord[i])):
                    
                    if move_end == board_coord[i][j]:
                        second_check = 1 
        
        else:
            space_check == 0

    else:
        len_check = 0          

    if len_check == 0 or space_check == 0:

        return 0
          
    elif first_check == 0:

        return 1
    
    elif second_check == 0:

        return 2
    
    if len_check == 1 and space_check == 1 and first_check == 1 and  second_check == 1:

        current_position = piece_from_coord(move, board_coord)

        next_position = piece_to_coord(move, board_coord)

        if is_your_piece(current_position, turn, current_board):
                        
            piece_moves = get_current_piece_moves(current_position, current_board)

            piece_attacks = get_current_piece_attacks(current_position, current_board)
           

            print(piece_moves)
            print(piece_attacks)

            new_board = make_move(move, current_board, board_coord)

            all_black_attacks = board_evaluation.get_all_black_attacks(new_board)

            all_white_attacks = board_evaluation.get_all_white_attacks(new_board)

            white_king_coord = board_evaluation.get_white_king_coord(new_board)

            black_king_coord = board_evaluation.get_black_king_coord(new_board)
            
            if turn == "white" and (white_king_coord in all_black_attacks) :

                return 5

            elif turn == "black" and (black_king_coord in all_white_attacks):

                return 6

            elif (next_position not in piece_attacks) or (next_position not in piece_attacks):

                return 7

            elif (next_position in piece_attacks) and target_not_your_piece(next_position, turn, current_board):

                return 8

            else:

                return 3

        else:
            
            return 4          

def input_move_white(player_white, board_coord, turn, current_board):

    print("\n")
    print("White moves:")
        
    #RECURENTA!    
     
    print("What is your move, " + player_white + "?" +" (example: 'e2 e4')")
       
    move = input()
        
    move = str(move) 

    move = move.lower()   

    check_move = is_move_valid(move, board_coord, turn, current_board)

    if check_move == 0:
            
        print("Completely wrong input, please try again\n")
        
        final_move = input_move_white(player_white, board_coord, turn, current_board)

    elif check_move == 1:
            
        print("The square you want to move from is not a valid squre, please try again\n")

        final_move = input_move_white(player_white, board_coord, turn, current_board)

    elif check_move == 2:

        print("The square you want to move to is not a valid squre, please try again\n")
        
        final_move = input_move_white(player_white, board_coord, turn, current_board)

    elif check_move == 4:

        print("You did not select your piece, please try again\n")
        
        final_move = input_move_white(player_white, board_coord, turn, current_board)

    elif check_move == 3:
        
        final_move = move
    
    else:

        print("Illegal move, please try again\n")
        
        final_move = input_move_white(player_white, board_coord, turn, current_board)


    return final_move 


def input_move_black(player_black,  board_coord, turn, current_board):

    print("\n")
    print("Black moves:")
        
    #RECURENTA!    
     
    print("What is your move, " + player_black + "?" +" (example: 'e2 e4')")
       
    move = input()
        
    move = str(move)

    move = move.lower()
        
    check_move = is_move_valid(move, board_coord, turn, current_board)

    if check_move == 0:
            
        print("Completely wrong input, please try again\n")
        
        final_move = input_move_black(player_black,  board_coord, turn, current_board)

    elif check_move == 1:
            
        print("The square you want to move from is not a valid squre, please try again\n")

        final_move = input_move_black(player_black,  board_coord, turn, current_board)

    elif check_move == 2:

        print("The square you want to move to is not a valid squre, please try again\n")
        
        final_move = input_move_black(player_black,  board_coord, turn, current_board)

    elif check_move == 4:

        print("You did not select your piece, please try again\n")
        
        final_move = input_move_black(player_black,  board_coord, turn, current_board)

    elif check_move == 3:
        
        final_move = move

    else:

        print("Illegal move, please try again\n")
        
        final_move = input_move_black(player_black, board_coord, turn, current_board)


    return final_move 
    

#     return True

# def is_your_piece(move):

