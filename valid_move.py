

def input_move_white(player_white):

    print("\n")
    print("Muta Albul:")

    print("Ce vrei sa muti, " + player_white + "?" +" (exemplu: 'e2 e4')")
    
    move = input()
    move = str(move)  

    return move

def input_move_black(player_black):

    print("\n")
    print("Muta Negrul:")

    print("Ce vrei sa muti, " + player_black + "?" +" (exemplu: 'e2 e4')")
    
    move = input()
    move = str(move)  

    return move

# def is_move_valid(move):

#     if len(move) != 5:
        
#         print("Esti spart. Ai scris prostii.\n")
#         print("Scrie, in pizda ma-tii, o mutare valida.\n")



#     elif 

#     return True

# def is_your_piece(move):

