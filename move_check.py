import pieces
import board_evaluation
# import chess_main
import json

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

# testing purge:

#print(board)

#board[0][0] = purge_cell(board[0][0])

#print(board)

def fill_cell(cell, current_piece):

    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + current_piece

    return current_cell

# def find_move_coord(move):

#     coord = []

#     for i in range(len(board_coord)):

#         for j in range(len(board_coord[i])):

#             if move == board_coord[i][j]:

#                 coord = [i, j]

#     return coord


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

    elif current_piece == "bk":
        
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

def is_opponent_piece(current_position, turn, current_board):

    current_piece = find_current_piece(current_position, current_board)
    
    if turn == "white":
        if current_piece[0] == "b":
            return True
        else:
            return False

    if turn == "black":
        if current_piece[0] == "w":
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

def make_test_move(move, new_board, board_coord):
        
    i = piece_from_coord(move, board_coord)[0]
    j = piece_from_coord(move, board_coord)[1]

    current_piece = new_board[i][j].split("_")[1]

    new_board[i][j] = purge_cell(new_board[i][j])

    x = piece_to_coord(move, board_coord)[0]
    y = piece_to_coord(move, board_coord)[1]

    new_board[x][y] = fill_cell(new_board[x][y], current_piece)

    return new_board

def revert_test_move(move, new_board, board_coord, next_piece):

    i = piece_to_coord(move, board_coord)[0]
    j = piece_to_coord(move, board_coord)[1]

    current_piece = new_board[i][j].split("_")[1]

    new_board[i][j] = fill_cell(new_board[i][j], next_piece)

    x = piece_from_coord(move, board_coord)[0]
    y = piece_from_coord(move, board_coord)[1]

    new_board[x][y] = fill_cell(new_board[x][y], current_piece)

    return new_board

def add_en_passant_moves(test_pgn_game, current_position, current_piece, next_position):

    if current_piece == "wp":

        en_passant_flag = []

        if ((current_position[0] == 6) and next_position[0] == 4):

            en_passant_flag.append(5)
            en_passant_flag.append(current_position[1])

            test_pgn_game['en_passant_flag'] = en_passant_flag

            with open("./game_database/game_flags.json", "w") as outfile:  
                json.dump(test_pgn_game, outfile) 

    elif current_piece == "bp":

        en_passant_flag = []

        if ((current_position[0] == 1) and next_position[0] == 3):

            en_passant_flag.append(2)
            en_passant_flag.append(current_position[1])

            test_pgn_game['en_passant_flag'] = en_passant_flag

            with open("./game_database/game_flags.json", "w") as outfile:  
                json.dump(test_pgn_game, outfile) 

    else:

        test_pgn_game['en_passant_flag'] = []

def promote(current_piece):

    promoted_piece = current_piece

    print("Pick your promoted piece. Please type one of the following:\n 'p' for pawn; 'r' for rook, 'h' for horse, 'b' for bishop or 'q' for queen:\n")

    p_piece = input()
    p_piece = str(p_piece)
    valid_pieces = "prhbq"

    length_check = 0
    piece_check = 0
        
    if len(p_piece) == 1:
        length_check = 1
        
        if p_piece in valid_pieces:

             piece_check = 1
        
        else:
            piece_check = 0

    else:
        length_check == 0

    if length_check == 0 or piece_check == 0:

        print("Wrong input. Please try again")
        p_piece = promote(current_piece) 

    if length_check == 1 and piece_check == 1:

        promoted_piece = promoted_piece.strip("p")
        promoted_piece = promoted_piece + p_piece

        return promoted_piece
    
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

        current_piece = find_current_piece(current_position, current_board)

        next_piece = find_current_piece(next_position, current_board)

        print("next pos" + str(next_position))

        if is_your_piece(current_position, turn, current_board):
                        
            piece_moves = get_current_piece_moves(current_position, current_board)

            piece_attacks = get_current_piece_attacks(current_position, current_board)

            attacks_on_opp_pieces = []

            promoted_piece = current_piece

            promoted = 0
           
            all_black_attacks = board_evaluation.get_all_black_attacks(current_board)

            all_white_attacks = board_evaluation.get_all_white_attacks(current_board)

            white_king_coord = board_evaluation.get_white_king_coord(current_board)

            black_king_coord = board_evaluation.get_black_king_coord(current_board)

            all_white_coords = board_evaluation.get_all_white_coords(current_board)

            all_black_coords = board_evaluation.get_all_black_coords(current_board)

            print("Current piece moves: " + str(piece_moves))
            print("Current piece attacks: " + str(piece_attacks))

            if turn == "white":
            
                if current_piece == "wp" and next_position[0] == 0 and next_piece == "00":
                    
                    promoted_piece = promote(current_piece)

                    promoted = 1

            if turn == "black":
            
                if current_piece == "bp" and next_position[0] == 7 and next_piece == "00":
                    
                    promoted_piece = promote(current_piece)

                    promoted = 1

            new_board = current_board

            new_board = make_test_move(move, new_board, board_coord)

            if promoted == 1:
                
                i = piece_to_coord(move, board_coord)[0]
                j = piece_to_coord(move, board_coord)[1]
                
                new_board[i][j] = fill_cell(new_board[i][j], promoted_piece)

            # for i in range(len(new_board)):

            #     print(new_board[i])
            #     print("\n")
            

            test_all_black_attacks = board_evaluation.get_all_black_attacks(current_board)

            test_all_white_attacks = board_evaluation.get_all_white_attacks(current_board)

            test_white_king_coord = board_evaluation.get_white_king_coord(current_board)

            test_black_king_coord = board_evaluation.get_black_king_coord(current_board)

            test_all_white_coords = board_evaluation.get_all_white_coords(current_board)

            test_all_black_coords = board_evaluation.get_all_black_coords(current_board)

            new_board = revert_test_move(move, new_board, board_coord, next_piece)
            
            with open('./game_database/game_flags.json', 'r') as flags:
                data=flags.read()

            game_flags = json.loads(data)

            en_passant_flag = game_flags['en_passant_flag']
            
            if turn == "white":

                attacks_on_opp_pieces = [i for i in piece_attacks if i in all_black_coords]

                if current_piece == "wp":

                    if en_passant_flag in piece_attacks:

                        attacks_on_opp_pieces.append(en_passant_flag)
               
            if turn == "black":

                attacks_on_opp_pieces = [i for i in piece_attacks if i in all_white_coords]
                
                if current_piece == "bp":

                    if en_passant_flag in piece_attacks:

                        attacks_on_opp_pieces.append(en_passant_flag)

            print("All white attacks:  " + str(test_all_white_attacks))
            print("All white coords:  " + str(test_all_white_coords))
            
            print("All black attacks:  " + str(test_all_black_attacks))
            print("All black coords:  " + str(test_all_black_coords))

            print("White king coord  " + str(test_white_king_coord))
            print("Black king coord  " + str(test_black_king_coord))

            # for i in range(len(current_board)):

            #     print(current_board[i])
            #     print("\n")
            
            if (turn == "white" and (test_white_king_coord in test_all_black_attacks)) :

                return 5

            elif (turn == "black" and (test_black_king_coord in test_all_white_attacks)):

                return 6

            elif ((next_position not in piece_moves) and (next_position not in attacks_on_opp_pieces)):

                return 7

            # elif ((next_position in piece_attacks) and is_your_piece(next_position, turn, current_board)):
                 
            #     return 8                        

            # elif (current_piece == "wp") and next_position[0] = 7

            else:

                add_en_passant_moves(game_flags, current_position, current_piece, next_position)
                
                with open("./game_database/game_flags.json", "w") as outfile:  
                    json.dump(game_flags, outfile) 

                return 3                
                          
        else:
            
            return 4           


