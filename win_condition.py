
import board_evaluation
import move_check
import pieces



def is_draw(turn, current_board):

    no_legal_moves_for_opponent = board_evaluation.opponent_has_no_legal_moves(turn, current_board)    
    is_sufficient_material = board_evaluation.is_sufficient_material(current_board)

    if no_legal_moves_for_opponent or (not is_sufficient_material):
    
        return True
    else:

        return False