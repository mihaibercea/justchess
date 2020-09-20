
import move_check
import board_evaluation

class piece:

    color = "color"
    shape = "shape"

    def __init__(self, color, shape): 
        self.color = color
        self.shape = shape

    def get_avatar(self):

        avatar = self.color[0] + self.shape[0]

        return avatar

white = "white"
black = "black"

pawn = "pawn"
rook = "rook"
horse = "horse"
bishop = "bishop"
queen = "queen"
king = "king"

# White Pieces
#====================

class white_pawn():
    
    color = white
    shape = pawn
    
    def get_available_moves(self, current_position, current_board):
        
        available_moves = []

        available_move = []

        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves              
        
        #print(current_position)

        if current_position[0] == 6:

            available_move.append(5)
            available_move.append(current_position[1])

            available_moves.append(available_move)
                    
            available_move = []

            available_move.append(4)
            available_move.append(current_position[1])

            available_moves.append(available_move)

        else:

            available_move.append(current_position[0]-1)
            available_move.append(current_position[1])

            available_moves.append(available_move)                                 

        available_moves = check_if_offboard(available_moves)

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)
       
        available_moves_1 = [i for i in available_moves if i not in all_white_coords]
        available_moves_final = [i for i in available_moves_1 if i not in all_black_coords]
      
      #  print(available_moves_final)

        return available_moves_final


    def get_available_attacks(self, current_position, current_board):
        
        def check_if_offboard(available_attacks):

            for each_move in available_attacks:

                if each_move[0] > 7 or each_move[1] > 7 or each_move[0] < 0 or each_move[1] < 0:

                    available_attacks.remove(each_move)                         

            return available_attacks
       
        i = current_position[0]
        j = current_position[1]

        available_attacks = []

        available_attacks.append([i-1, j-1])
        available_attacks.append([i-1, j+1])
        
        available_attacks = check_if_offboard(available_attacks)
        all_white_coords = board_evaluation.get_all_white_coords(current_board)
  
        available_attacks_final = [i for i in available_attacks if i not in all_white_coords]
        
      #  print(available_attacks_final)

        return available_attacks_final

class white_rook():

    color = white
    shape = rook

    def get_available_moves(self, current_position, current_board):
        
        available_moves = []
        available_move = []

        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves
        
        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        #print(all_white_coords)
        #print(all_black_coords)

        x = i
        y = j+1

        while (y < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y+1

        x = i
        y = j-1

        while (y >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y-1

        x = i+1
        y = j

        while (x < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                
        
        x = i-1
        y = j

        while (x >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1

        # for y in range(len(current_board[j])):

        #     available_move = [i, y]
          
        #     available_moves.append(available_move)

        #     for m in range(len(available_moves)):
                
        #         if available_moves[m] == current_position:

        #             available_moves.pop(m)
            
        available_moves = check_if_offboard(available_moves)


        return available_moves
            
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks
       

class white_bishop():

    color = white
    shape = bishop


    def get_available_moves(self, current_position, current_board):
        
        available_moves = []

        available_move = []
        
        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        x = i+1
        y = j+1

        while (x < 8 and y < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y+1

        x = i-1
        y = j+1

        while (x >= 0 and y < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y+1

        x = i-1
        y = j-1

        while (x >= 0 and y >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y-1

        x = i+1
        y = j-1

        while (x < 8 and y >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y-1

        available_moves = check_if_offboard(available_moves)

        return available_moves
                    
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks

class white_horse():

    color = white
    shape = horse

    def get_available_moves(self, current_position, current_board):
                
        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        # all_black_coords = board_evaluation.get_all_black_coords(current_board)

        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        available_moves_dict = {
        
            "available_move0" : [i+2, j+1],
            "available_move1" : [i+2, j-1],
            "available_move2" : [i-2, j-1],
            "available_move3" : [i-2, j+1],
            "available_move4" : [i+1, j+2],
            "available_move5" : [i+1, j-2],
            "available_move6" : [i-1, j-2],
            "available_move7" : [i-1, j+2]

        }

        available_moves = list(available_moves_dict.values())
               
        available_moves = check_if_offboard(available_moves)
        
        available_moves_final = [i for i in available_moves if i not in all_white_coords]
             
        return available_moves_final
                    
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks

class white_queen():

    color = white
    shape = queen

    def get_available_moves(self, current_position, current_board):
        
        available_moves = []

        available_move = []
        
        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

       
        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        x = i+1
        y = j+1

        while (x < 8 and y < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y+1

        x = i-1
        y = j+1

        while (x >= 0 and y < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y+1

        x = i-1
        y = j-1

        while (x >= 0 and y >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y-1

        x = i+1
        y = j-1

        while (x < 8 and y >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y-1
                
       
        i = current_position[0]
        j = current_position[1]

        x = i
        y = j+1

        while (y < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y+1

        x = i
        y = j-1

        while (y >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y-1

        x = i+1
        y = j

        while (x < 8):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                
        
        x = i-1
        y = j

        while (x >= 0):

            available_move = [x, y]

            if available_move in all_white_coords:

                break
            
            elif available_move in all_black_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1

        available_moves = check_if_offboard(available_moves)

        return available_moves
                    
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks

class white_king():

    color = white
    shape = king

    def get_available_moves(self, current_position, current_board):
        
        available_moves = []
        #available_move = []

        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

        #print(current_position)

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        
        #all_black_attacks = board_evaluation.get_all_black_attacks(current_board)
        
        i = current_position[0]
        j = current_position[1]

        available_moves_dict = {
        
            "available_move0" : [i+1, j+1],
            "available_move1" : [i+1, j-1],
            "available_move2" : [i+1, j],
            "available_move3" : [i-1, j+1],
            "available_move4" : [i-1, j-1],
            "available_move5" : [i-1, j],
            "available_move6" : [i, j+1],
            "available_move7" : [i, j-1]

        }

        available_moves = list(available_moves_dict.values())

                
        available_moves = check_if_offboard(available_moves)
        
        available_moves_1 = [i for i in available_moves if i not in all_white_coords]

        #available_moves_final = [i for i in available_moves_1 if i not in all_black_attacks]

        print("White king can move to: " + str(available_moves_1))

        return available_moves_1              
            
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks



# Black Pieces
#====================


class black_pawn():
    
    color = black
    shape = pawn
    
    def get_available_moves(self, current_position, current_board):
        
        available_moves = []

        available_move = []

        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves              
        
        #print(current_position)

        if current_position[0] == 1:

            available_move.append(2)
            available_move.append(current_position[1])

            available_moves.append(available_move)
                    
            available_move = []

            available_move.append(3)
            available_move.append(current_position[1])

            available_moves.append(available_move)

        else:

            available_move.append(current_position[0]+1)
            available_move.append(current_position[1])

            available_moves.append(available_move)                                 

        available_moves = check_if_offboard(available_moves)

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)
       
        available_moves_1 = [i for i in available_moves if i not in all_white_coords]
        available_moves_final = [i for i in available_moves_1 if i not in all_black_coords]
      
      #  print(available_moves_final)

        return available_moves_final


    def get_available_attacks(self, current_position, current_board):
        
        def check_if_offboard(available_attacks):

            for each_move in available_attacks:

                if each_move[0] > 7 or each_move[1] > 7 or each_move[0] < 0 or each_move[1] < 0:

                    available_attacks.remove(each_move)                         

            return available_attacks
       
        i = current_position[0]
        j = current_position[1]

        available_attacks = []

        available_attacks.append([i+1, j-1])
        available_attacks.append([i+1, j+1])
        
        available_attacks = check_if_offboard(available_attacks)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)
  
        available_attacks_final = [i for i in available_attacks if i not in all_black_coords]
        
      #  print(available_attacks_final)

        return available_attacks_final

class black_rook():

    color = black
    shape = rook

    def get_available_moves(self, current_position, current_board):
        
        available_moves = []
        available_move = []

        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves
        
        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        #print(all_white_coords)
        #print(all_black_coords)

        x = i
        y = j+1

        while (y < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y+1

        x = i
        y = j-1

        while (y >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y-1

        x = i+1
        y = j

        while (x < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                
        
        x = i-1
        y = j

        while (x >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1

        # for y in range(len(current_board[j])):

        #     available_move = [i, y]
          
        #     available_moves.append(available_move)

        #     for m in range(len(available_moves)):
                
        #         if available_moves[m] == current_position:

        #             available_moves.pop(m)
            
        available_moves = check_if_offboard(available_moves)


        return available_moves
            
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks
       

class black_bishop():

    color = black
    shape = bishop


    def get_available_moves(self, current_position, current_board):
        
        available_moves = []

        available_move = []
        
        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        x = i+1
        y = j+1

        while (x < 8 and y < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y+1

        x = i-1
        y = j+1

        while (x >= 0 and y < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y+1

        x = i-1
        y = j-1

        while (x >= 0 and y >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y-1

        x = i+1
        y = j-1

        while (x < 8 and y >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y-1

        available_moves = check_if_offboard(available_moves)

        return available_moves
                    
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks

class black_horse():

    color = black
    shape = horse

    def get_available_moves(self, current_position, current_board):
                
        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

        #all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        available_moves_dict = {
        
            "available_move0" : [i+2, j+1],
            "available_move1" : [i+2, j-1],
            "available_move2" : [i-2, j-1],
            "available_move3" : [i-2, j+1],
            "available_move4" : [i+1, j+2],
            "available_move5" : [i+1, j-2],
            "available_move6" : [i-1, j-2],
            "available_move7" : [i-1, j+2]

        }

        available_moves = list(available_moves_dict.values())
               
        available_moves = check_if_offboard(available_moves)
        
        available_moves_final = [i for i in available_moves if i not in all_black_coords]
             
        return available_moves_final
                    
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks

class black_queen():

    color = black
    shape = queen

    def get_available_moves(self, current_position, current_board):
        
        available_moves = []

        available_move = []
        
        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

       
        #print(current_position)

        i = current_position[0]
        j = current_position[1]

        all_white_coords = board_evaluation.get_all_white_coords(current_board)
        all_black_coords = board_evaluation.get_all_black_coords(current_board)

        x = i+1
        y = j+1

        while (x < 8 and y < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y+1

        x = i-1
        y = j+1

        while (x >= 0 and y < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y+1

        x = i-1
        y = j-1

        while (x >= 0 and y >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1
                y = y-1

        x = i+1
        y = j-1

        while (x < 8 and y >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                y = y-1
                
       
        i = current_position[0]
        j = current_position[1]

        x = i
        y = j+1

        while (y < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y+1

        x = i
        y = j-1

        while (y >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                y = y-1

        x = i+1
        y = j

        while (x < 8):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x+1
                
        
        x = i-1
        y = j

        while (x >= 0):

            available_move = [x, y]

            if available_move in all_black_coords:

                break
            
            elif available_move in all_white_coords:

                available_moves.append(available_move)
                
                break

            else:
                
                available_moves.append(available_move)

                x = x-1

        available_moves = check_if_offboard(available_moves)

        return available_moves
                    
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks

class black_king():

    color = black
    shape = king

    def get_available_moves(self, current_position, current_board):
        
        available_moves = []
        #available_move = []

        def check_if_offboard(avaialbe_moves):
            
            good_moves = []

            for each_move in avaialbe_moves:

                if each_move[0] < 8 and each_move[1] < 8 and each_move[0] > -1 and each_move[1] > -1:

                   good_moves.append(each_move)                                                

            return good_moves

        #print(current_position)

        all_black_coords = board_evaluation.get_all_black_coords(current_board)
        
        #all_white_attacks = board_evaluation.get_all_white_attacks(current_board)
        
        i = current_position[0]
        j = current_position[1]

        available_moves_dict = {
        
            "available_move0" : [i+1, j+1],
            "available_move1" : [i+1, j-1],
            "available_move2" : [i+1, j],
            "available_move3" : [i-1, j+1],
            "available_move4" : [i-1, j-1],
            "available_move5" : [i-1, j],
            "available_move6" : [i, j+1],
            "available_move7" : [i, j-1]

        }

        available_moves = list(available_moves_dict.values())

                
        available_moves = check_if_offboard(available_moves)
        
        available_moves_1 = [i for i in available_moves if i not in all_black_coords]

        #available_moves_final = [i for i in available_moves_1 if i not in all_white_attacks]

        print("Black king can move to: " + str(available_moves_1))

        return available_moves_1              
            
    def get_available_attacks(self, current_position, current_board):
        
        available_attacks = self.get_available_moves(current_position, current_board)
        
        return available_attacks
    

# def get_avaialbe_moves(move, current_board, board_coord):

#     available_moves = []

#     current_piece = move_check.find_current_piece(move, current_board, board_coord)

#     if current_piece == "wp":

#         avaialble_moves = white_pawn().get_available_moves(move, current_board, board_coord)
    
#     return available_moves