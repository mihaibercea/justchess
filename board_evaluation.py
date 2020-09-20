import move_check

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

def get_black_king_coord(current_board):

    black_king_coord = []

    for i in range(len(current_board)):

        for j in range(len(current_board[i])):
                    
            piece = current_board[i][j].split("_")[1]
           
            if piece == "bk":

                black_king_coord = [i, j]

    return black_king_coord

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
                check == True

    return check

def queen_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "q":
                check == True

    return check

def rook_on_board(current_board):

    check = False

    for line in current_board:
        for cell in line:
            piece = cell.split("_")
            if piece[1][1] == "r":
                check == True

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