
import board_evaluation

def is_white_king_mated():

    # for every atack or every defence of white pieces, the king should not be attacked anymore.

    return False

def is_black_king_mated():

    return False

def is__not_draw(current_board):

    # after your move: 
    #??
    # 1. Noone has any more moves or attacks for all pieces except the king.
    #
    #
    #       to take care of king moves here.
    #
    #       for turn = black
    #
    #           if black_king_moves not in all_white attacks
    #
    #       if black_king_moves not in all_white attacks
    #           
    #           if black_king_moves not in all_white attacks
    #
    #       
    # and
    #
    # 2. Your opponent has no more pawn attacks where an opposite piece is.
    #
    # or
    #??
    #



    # 3. Insufficient material: just kings, just one bishop, just 2 or less horses.
    # under move_check 
    #   def is_sufficient_material():
    #       if pawn_on_board:
    #           sufficient_material
    #       elif queen_on_board:
    #           sufficient_material
    #       elif rook_onboard:
    #           sufficient_material
    #       elif bishop and horse:
    #           sufficient_material
    #       elif two bishops:   
    #            sufficient_material
    #       else:
    #           insufficient material
    
    is_sufficient_material = board_evaluation.is_sufficient_material(current_board)

    return False