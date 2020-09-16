
import move_check

class piece:

    color = "color"
    shape = "shape"

    def __init__(self, color, shape): 
        self.color = color
        self.shape = shape

    def get_avatar(self):

        avatar = self.color[0] + self.shape[0]

        return avatar

# White Pieces
#====================

white = "white"
black = "black"

pawn = "pawn"
rook = "rook"
horse = "horse"
bishop = "bishop"
queen = "queen"
king = "king"

# class white_pawn():
    
#     def get_available_moves(self, move, current_board, board_coord):
        
#         available_moves = []

#         available_move1 = []
#         available_move2 = []

#         current_position = move_check.piece_from_coord(move, board_coord)

#         if current_position[0] == 6:
            
#             avaialbe_move1[0] = current_position[0]
#             avaialbe_move1[1] = current_position[1]

#             avaialbe_moves = avaialble.moves.append(current_position[][])

#         return available_moves

#     def get_available_attacks():



class white_rook():

    color = "white"
    shape = "rook"

class white_horse():

    color = "white"
    shape = "rook"

class white_bishop():

    color = "white"
    shape = "bishop"

class white_queen():

    color = "white"
    shape = "queen"

class white_king():

    color = "white"
    shape = "king"


# White Pieces
#====================


class black_pawn():

    color = "black"
    shape = "pawn"

class black_rook():

    color = "black"
    shape = "rook"

class blacke_horse():

    color = "black"
    shape = "rook"

class black_bishop():

    color = "black"
    shape = "bishop"

class black_queen():

    color = "black"
    shape = "queen"

class black_king():

    color = "black"
    shape = "king"

def get_avaialbe_moves(move, current_board, board_coord):

    available_moves = []

    current_piece = move_check.find_current_piece(move, current_board, board_coord)

    if current_piece == "wp":

        avaialble_moves = white_pawn().get_available_moves(move, current_board, board_coord)
    
    return available_moves