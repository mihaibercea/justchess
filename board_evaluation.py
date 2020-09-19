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

                all_attacks = all_attacks.append(piece_attacks)

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

                all_attacks = all_attacks.append(piece_attacks)

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