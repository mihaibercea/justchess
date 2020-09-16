
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

def find_current_piece(move, current_board, board_coord):

    coord = piece_from_coord(move, board_coord)

    i = coord[0]
    j = coord[1]

    current_piece = current_board[i][j].split("_")[1]

    return current_piece

def is_your_piece(move, turn, current_board, board_coord):

    current_piece = find_current_piece(move, current_board, board_coord)
    
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

        if is_your_piece(move, turn, current_board, board_coord) == True:
            
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

    return final_move 


def input_move_black(player_black,  board_coord, turn, current_board):

    print("\n")
    print("Black moves:")
        
    #RECURENTA!    
     
    print("What is your move, " + player_black + "?" +" (example: 'e2 e4')")
       
    move = input()
        
    move = str(move)  

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

    return final_move 
    

#     return True

# def is_your_piece(move):

