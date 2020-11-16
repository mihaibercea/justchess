import move_check
import pieces
import board_operations

# def get_pgn_game(turn, turn_count):

#     all_moves = []

#     return all_moves

def get_all_white_coords(current_board):

    white_coords = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):

            current_piece = current_board[i][j].split("_")[1]

            if current_piece[0] == "w":
                
                coord = [i, j]

                white_coords.append(coord)
    
    res = [] 

    for i in white_coords: 
        if i not in res: 
            res.append(i) 
    
    return res

def get_all_black_coords(current_board):

    black_coords = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):

            current_piece = current_board[i][j].split("_")[1]

            if current_piece[0] == "b":
                
                coord = [i, j]

                black_coords.append(coord)
    
    res = [] 

    for i in black_coords: 
        if i not in res: 
            res.append(i) 

    return res

def get_all_white_moves(current_board):
    
    all_moves = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece_type = current_board[i][j].split("_")[1]

            current_possition =[i, j]

            if piece_type[0] == "w":
                
                piece_moves = move_check.get_current_piece_moves(current_possition, current_board)
               
                for pos in piece_moves:

                    all_moves.append(pos)

             # To purge this list of duplicates!

    res = [] 
    for i in all_moves: 
	    if i not in res: 
		    res.append(i)  
    

    return res

def get_all_black_moves(current_board):
    
    all_moves = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece_type = current_board[i][j].split("_")[1]

            current_possition =[i, j]

            if piece_type[0] == "b":
                
                piece_moves = move_check.get_current_piece_moves(current_possition, current_board)
               
                for pos in piece_moves:

                    all_moves.append(pos)

             # To purge this list of duplicates!

    res = [] 
    for i in all_moves: 
	    if i not in res: 
		    res.append(i)  
    

    return res

def get_all_white_attacks(current_board):

    all_attacks = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece_type = current_board[i][j].split("_")[1]

            current_possition =[i, j]

            if piece_type[0] == "w":
                
                piece_attacks = move_check.get_current_piece_attacks(current_possition, current_board)
               
                for pos in piece_attacks:

                    all_attacks.append(pos)

             # To purge this list of duplicates!

    res = [] 
    for i in all_attacks: 
	    if i not in res: 
		    res.append(i)  
    

    return res

def get_all_black_attacks(current_board):

    all_attacks = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece_type = current_board[i][j].split("_")[1]

            current_possition =[i, j]

            if piece_type[0] == "b":
                
                piece_attacks = move_check.get_current_piece_attacks(current_possition, current_board)

                for pos in piece_attacks:

                    all_attacks.append(pos)

    res = [] 
    for i in all_attacks: 
	    if i not in res: 
		    res.append(i)  

             # To purge this list of duplicates!

    return res

def get_white_king_coord(current_board):

    white_king_coord = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece = current_board[i][j].split("_")[1]
           
            if piece == "wk":

                white_king_coord = [i, j]

    return white_king_coord

def get_white_king_attacks(current_board):

    current_position = get_white_king_coord(current_board)
    
    piece = pieces.white_king()
    white_king_attacks = piece.get_available_attacks(current_position, current_board)

    return white_king_attacks


def get_black_king_coord(current_board):

    black_king_coord = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece = current_board[i][j].split("_")[1]
           
            if piece == "bk":

                black_king_coord = [i, j]

    return black_king_coord

def get_black_king_attacks(current_board):

    current_position = get_black_king_coord(current_board)
    
    piece = pieces.black_king()
    black_king_attacks = piece.get_available_attacks(current_position, current_board)

    return black_king_attacks

def is_white_king_attacked(current_board):

    white_king_coord = get_white_king_coord(current_board)

    all_black_attacks = get_all_black_attacks(current_board)

    for pos in range(all_black_attacks):

        if pos == white_king_coord:
            
            return True
        
        else:

            return False

def is_black_king_attacked(current_board):

    black_king_coord = get_black_king_coord(current_board)

    all_white_attacks = get_all_white_attacks(current_board)

    for pos in range(all_white_attacks):

        if pos == black_king_coord:
            
            return True
        
        else:

            return False


# for win condition:

#### for draw

def pawn_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "p":
                check = True

    return check

def queen_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "q":
                check = True

    return check

def rook_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "r":
                check = True

    return check

def bishop_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "b":
                check = True
                
    return check

def horse_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "h":
                check = True
                
    return check

def white_horses(current_board):

    check = 0

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1] == "wh":
                check =+1
                
    return check

def black_horses(current_board):

    check = 0

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1] == "bh":
                check =+1
                
    return check

def white_bishops(current_board):

    check = 0

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1] == "wb":
                check =+1
                
    return check

def black_bishops(current_board):

    check = 0

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1] == "bb":
                check =+1
                
    return check

def is_sufficient_material(current_board):

    sufficient_material = True
    
    if (not pawn_on_board(current_board)) and (not queen_on_board(current_board)) and (not rook_on_board(current_board)): 
        
        if (not bishop_on_board(current_board)) and not (horse_on_board(current_board)):  
                
            sufficient_material = False
        
        elif (not bishop_on_board(current_board)) and (white_horses(current_board) <= 2) and (black_horses(current_board) == 0):
            
            sufficient_material = False
        
        elif (not bishop_on_board(current_board)) and (white_horses(current_board) == 0) and (black_horses(current_board) <= 2):
            
            sufficient_material = False
        
        elif (not (horse_on_board(current_board)) and (black_bishops(current_board) == 1) and white_bishops(current_board) == 0):
            
            sufficient_material = False

        elif (not (horse_on_board(current_board)) and (black_bishops(current_board) == 0) and white_bishops(current_board) == 1):
            
            sufficient_material = False

    else:

        sufficient_material = True

    return sufficient_material

def get_all_white_pawn_attacks(current_board):

    all_attacks = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece_type = current_board[i][j].split("_")[1]

            current_possition =[i, j]

            if piece_type == "wp":
                
                piece_attacks = move_check.get_current_piece_attacks(current_possition, current_board)
               
                for pos in piece_attacks:

                    all_attacks.append(pos)

             # To purge this list of duplicates!

    res = [] 
    for i in all_attacks: 
	    if i not in res: 
		    res.append(i)  
    

    return res

def get_all_black_pawn_attacks(current_board):

    all_attacks = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece_type = current_board[i][j].split("_")[1]

            current_possition =[i, j]

            if piece_type == "bp":
                
                piece_attacks = move_check.get_current_piece_attacks(current_possition, current_board)
               
                for pos in piece_attacks:

                    all_attacks.append(pos)

             # To purge this list of duplicates!

    res = [] 
    for i in all_attacks: 
	    if i not in res: 
		    res.append(i)  
    

    return res


def find_current_piece(current_position, current_board):

    i = current_position[0]
    j = current_position[1]

    current_piece = current_board[i][j].split("_")[1]

    return current_piece

def test_move(pos, attack, new_board):
        
    i = pos[0]
    j = pos[1]

    current_piece = new_board[i][j].split("_")[1]

    new_board[i][j] = board_operations.purge_cell(new_board[i][j])

    x = attack[0]
    y = attack[1]

    #to implement a way to refill the previous cell with it's piece.

    new_board[x][y] = board_operations.fill_cell(new_board[x][y], current_piece)

    return new_board

def rev_test_move(pos, attack, new_board, attacked_piece):

    i = attack[0]
    j = attack[1]

    new_current_piece = new_board[i][j].split("_")[1]

    new_board[i][j] = board_operations.fill_cell(new_board[i][j], attacked_piece)

    x = pos[0]
    y = pos[1]

    new_board[x][y] = board_operations.fill_cell(new_board[x][y], new_current_piece)

    return new_board

def opponent_has_no_legal_moves(turn, current_board):
       
    all_white_coords = get_all_white_coords(current_board)

    all_black_coords = get_all_black_coords(current_board)

    # all_white_moves = get_all_white_moves(current_board)

    # all_black_moves = get_all_black_moves(current_board)

    # all_black_attacks = get_all_black_attacks(current_board)

    # all_white_attacks = get_all_white_attacks(current_board)

    # white_king_coord = get_white_king_coord(current_board)

    # black_king_coord = get_black_king_coord(current_board)

    black_king_attacks = get_black_king_attacks(current_board)

    white_king_attacks = get_white_king_attacks(current_board)

    # all_black_pawn_attacks = get_all_black_pawn_attacks(current_board)

    # all_white_pawn_attacks = get_all_white_pawn_attacks(current_board)
    
    # all_white_pieces_attacked_by_black_pawns = [pos for pos in all_white_coords if pos in all_black_pawn_attacks] 

    # all_black_pieces_attacked_by_white_pawns = [pos for pos in all_black_coords if pos in all_white_pawn_attacks]
  
    
    # black_king_moves = black_king_attacks

    # for pos in black_king_attacks:
    #     if pos in white_king_attacks:
    #         black_king_moves.pop(pos)

    # white_king_moves = white_king_attacks

    # for pos in white_king_attacks:
    #     if pos in black_king_attacks:
    #         white_king_moves.pop(pos)
        
    if turn == "white":  

        check = 0

        # Test all available black moves. If any move is legal, the function returns false.
   
        for pos in all_black_coords:

            this_current_piece = move_check.find_current_piece(pos, current_board)
            piece_moves = move_check.get_current_piece_moves(pos, current_board)
                       
            if this_current_piece != "bp":

                for attack in piece_moves:               
                
                    new_board = current_board
                # bug happens here
                    
                    attacked_piece = find_current_piece(attack, current_board)

                    new_board = test_move(pos, attack, new_board)

                    new_all_black_attacks = get_all_black_attacks(new_board)

                    new_all_white_attacks = get_all_white_attacks(new_board)

                    new_white_king_coord = get_white_king_coord(new_board)

                    new_black_king_coord = get_black_king_coord(new_board)

                    new_board = rev_test_move(pos, attack, new_board, attacked_piece)
                    
                    if (new_black_king_coord not in new_all_white_attacks):

                        check = 1               
            
            elif this_current_piece == "bp":
                
                pawn_attacks = move_check.get_current_piece_attacks(pos, current_board)

                valid_attacks = [pos for pos in all_white_coords if pos in pawn_attacks]

                for attack in valid_attacks:               
            
                    new_board = current_board
                    
                    attacked_piece = find_current_piece(attack, current_board)

                    new_board = test_move(pos, attack, new_board)

                    new_all_black_attacks = get_all_black_attacks(new_board)

                    new_all_white_attacks = get_all_white_attacks(new_board)

                    new_white_king_coord = get_white_king_coord(new_board)

                    new_black_king_coord = get_black_king_coord(new_board)

                    new_board = rev_test_move(pos, attack, new_board, attacked_piece)
                    
                    if (new_black_king_coord not in new_all_white_attacks):

                        check = 1   
        
        print(check)

        if check == 1 :

            return False

        elif check == 0 :

            return  True

    if turn == "black":

        check = 0

        # Test all available white moves. If any move is legal, the function returns false.
   
        for pos in all_white_coords:

            this_current_piece = move_check.find_current_piece(pos, current_board)
            piece_moves = move_check.get_current_piece_moves(pos, current_board)
                       
            if this_current_piece != "wp":

                for attack in piece_moves:               
                
                    new_board = current_board
                    
                    attacked_piece = find_current_piece(attack, current_board)

                    new_board = test_move(pos, attack, new_board)

                    new_all_black_attacks = get_all_black_attacks(new_board)

                    new_all_white_attacks = get_all_white_attacks(new_board)

                    new_white_king_coord = get_white_king_coord(new_board)

                    new_black_king_coord = get_black_king_coord(new_board)

                    new_board = rev_test_move(pos, attack, new_board, attacked_piece)
                    
                    if (new_white_king_coord not in new_all_black_attacks):

                        check = 1               
            
            elif this_current_piece == "wp":
                
                pawn_attacks = move_check.get_current_piece_attacks(pos, current_board)

                valid_attacks = [pos for pos in all_black_coords if pos in pawn_attacks]

                for attack in valid_attacks:               
            
                    new_board = current_board
                    
                    attacked_piece = find_current_piece(attack, current_board)

                    new_board = test_move(pos, attack, new_board)

                    new_all_black_attacks = get_all_black_attacks(new_board)

                    new_all_white_attacks = get_all_white_attacks(new_board)

                    new_white_king_coord = get_white_king_coord(new_board)

                    new_black_king_coord = get_black_king_coord(new_board)

                    new_board = rev_test_move(pos, attack, new_board, attacked_piece)
                    
                    if (new_white_king_coord not in new_all_black_attacks):

                        check = 1   

        print(check)

        if check == 1 :

            return False

        elif check == 0 :

            return  True


                        # there is at least one legal move
            
            




            

