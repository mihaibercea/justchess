
# board = [
#     ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
#     ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
#     ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
#     ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],   
#     ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
#     ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
#     ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
#     ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
# ]   

# board_coord = [
#     ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
#     ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
#     ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
#     ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
#     ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
#     ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
#     ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
#     ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
# ]

# move = ["a8", "b8"]


# def find_move_coord(move):

#     coord = []

#     for i in range(len(board_coord)):

#         for j in range(len(board_coord[i])):

#             if move[1] == board_coord[i][j]:

#                 coord = [i, j]

#     return coord

# # print(find_move_coord(move))

# mylist = ["a", "b", "a", "c", "c"]
# mylist = dict.fromkeys(mylist)
# print(mylist)


# # Python 3 code to demonstrate 
# # removing duplicated from list 
# # using naive methods 

# # initializing list 
# test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
# print ("The original list is : " + str(test_list)) 

# # using naive method 
# # to remove duplicated 
# # from list 
# res = [] 
# for i in test_list: 
# 	if i not in res: 
# 		res.append(i) 

# # printing list after removal 
# print ("The list after removing duplicates : " + str(res)) 

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
Dict[1] = Dict[1] + " for geeks"

print(Dict)

print("Pick your promoted piece. Please type one of the following:\n 'p' for pawn; 'r' for rook, 'h' for horse, 'b' for bishop or 'q' for queen:\n")

promoted_piece = input()
promoted_piece = str(promoted_piece)
valid_pieces = "prhbq"

length_check = 0
piece_check = 0
    
if len(promoted_piece) == 1:
    length_check = 1
    
    if promoted_piece in valid_pieces:

            piece_check = 1
    
    else:
        piece_check = 0

else:
    length_check == 0
                
if length_check == 1 and piece_check == 1:

    print(promoted_piece)
