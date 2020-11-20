import pieces
import move_check
import json

white_pawn = pieces.piece("white", "pawn")
white_horse = pieces.piece("white", "horse")
white_bishop = pieces.piece("white", "bishop")
white_rook = pieces.piece("white", "rook")
white_queen = pieces.piece("white", "queen")
white_king = pieces.piece("white", "king")

black_pawn = pieces.piece("black", "pawn")
black_horse = pieces.piece("black", "horse")
black_bishop = pieces.piece("black", "bishop")
black_rook = pieces.piece("black", "rook")
black_queen = pieces.piece("black", "queen")
black_king = pieces.piece("black", "king")

board = [
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],   
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
]   

board_coord = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
]


def classic_board():

    start_board = board

    for i in range(2, 7):
        for j in range(len(start_board[i])):
            start_board[i][j] = "White_00"

    start_board[0][0] = fill_cell(start_board[0][0], black_rook.get_avatar())
    start_board[0][1] = fill_cell(start_board[0][1], black_horse.get_avatar())
    start_board[0][2] = fill_cell(start_board[0][2], black_bishop.get_avatar())
    start_board[0][3] = fill_cell(start_board[0][3], black_queen.get_avatar())
    start_board[0][4] = fill_cell(start_board[0][4], black_king.get_avatar())
    start_board[0][5] = fill_cell(start_board[0][5], black_bishop.get_avatar())
    start_board[0][6] = fill_cell(start_board[0][6], black_horse.get_avatar())
    start_board[0][7] = fill_cell(start_board[0][7], black_rook.get_avatar())

    start_board[1][0] = fill_cell(start_board[1][0], black_pawn.get_avatar())
    start_board[1][1] = fill_cell(start_board[1][1], black_pawn.get_avatar())
    start_board[1][2] = fill_cell(start_board[1][2], black_pawn.get_avatar())
    start_board[1][3] = fill_cell(start_board[1][3], black_pawn.get_avatar())
    start_board[1][4] = fill_cell(start_board[1][4], black_pawn.get_avatar())
    start_board[1][5] = fill_cell(start_board[1][5], black_pawn.get_avatar())
    start_board[1][6] = fill_cell(start_board[1][6], black_pawn.get_avatar())
    start_board[1][7] = fill_cell(start_board[1][7], black_pawn.get_avatar())

    start_board[6][0] = fill_cell(start_board[1][0], white_pawn.get_avatar())
    start_board[6][1] = fill_cell(start_board[1][1], white_pawn.get_avatar())
    start_board[6][2] = fill_cell(start_board[1][2], white_pawn.get_avatar())
    start_board[6][3] = fill_cell(start_board[1][3], white_pawn.get_avatar())
    start_board[6][4] = fill_cell(start_board[1][4], white_pawn.get_avatar())
    start_board[6][5] = fill_cell(start_board[1][5], white_pawn.get_avatar())
    start_board[6][6] = fill_cell(start_board[1][6], white_pawn.get_avatar())
    start_board[6][7] = fill_cell(start_board[1][7], white_pawn.get_avatar())

    start_board[7][0] = fill_cell(start_board[0][0], white_rook.get_avatar())
    start_board[7][1] = fill_cell(start_board[0][1], white_horse.get_avatar())
    start_board[7][2] = fill_cell(start_board[0][3], white_bishop.get_avatar())
    start_board[7][3] = fill_cell(start_board[0][3], white_queen.get_avatar())
    start_board[7][4] = fill_cell(start_board[0][4], white_king.get_avatar())
    start_board[7][5] = fill_cell(start_board[0][5], white_bishop.get_avatar())
    start_board[7][6] = fill_cell(start_board[0][6], white_horse.get_avatar())
    start_board[7][7] = fill_cell(start_board[0][7], white_rook.get_avatar())
        
    return start_board


def purge_cell(cell):
    
    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + "00"

    return current_cell

def fill_cell(cell, current_piece):

    current_cell = cell.split("_")

    current_cell = str(current_cell[0]) + "_" + current_piece

    return current_cell

def find_move_coord(move):

    coord = []

    for i in range(len(board_coord)):

        for j in range(len(board_coord[i])):

            if move == board_coord[i][j]:

                coord = [i, j]

    return coord

def find_current_piece(move, current_board):

    i = find_move_coord(move[0])[0]
    j = find_move_coord(move[0])[1]

    current_piece = current_board[i][j].split("_")[1]

    return current_piece


def make_move(move, current_board):


    move = move.split(" ")
        
    i = find_move_coord(move[0])[0]
    j = find_move_coord(move[0])[1]

    current_piece = current_board[i][j].split("_")[1]

    with open('./game_database/game_flags.json', 'r') as flags:
        data=flags.read()

    game_flags = json.loads(data)
    
    castling = game_flags['castling']
    en_passant_flag = game_flags['en_passant_flag']
    en_passant_flagged = game_flags['en_passant_flagged']

    if castling == "wshort":
        current_board[7][4] = purge_cell(current_board[7][4])
        current_board[7][7] = purge_cell(current_board[7][7])
        current_board[7][6] = fill_cell(current_board[7][6], 'wk')
        current_board[7][5] = fill_cell(current_board[7][6], 'wr')

    elif castling == "wlong":
        current_board[7][4] = purge_cell(current_board[7][4])
        current_board[7][0] = purge_cell(current_board[7][0])
        current_board[7][2] = fill_cell(current_board[7][2], 'wk')
        current_board[7][3] = fill_cell(current_board[7][3], 'wr')

    elif castling == "bshort":
        current_board[0][4] = purge_cell(current_board[0][4])
        current_board[0][7] = purge_cell(current_board[0][7])
        current_board[0][6] = fill_cell(current_board[0][6], 'bk')
        current_board[0][5] = fill_cell(current_board[0][6], 'br')

    elif castling == "blong":
        current_board[0][4] = purge_cell(current_board[0][4])
        current_board[0][0] = purge_cell(current_board[0][0])
        current_board[0][2] = fill_cell(current_board[0][2], 'bk')
        current_board[0][3] = fill_cell(current_board[0][3], 'br')

    else:

        current_board[i][j] = purge_cell(current_board[i][j])

        x = find_move_coord(move[1])[0]
        y = find_move_coord(move[1])[1]

        if len(en_passant_flag) == 2:

            if en_passant_flag[0] == x and en_passant_flag[1] == y:
                pawn_x = en_passant_flagged[0]
                pawn_y = en_passant_flagged[1]

                current_board[pawn_x][pawn_x] = purge_cell(current_board[pawn_x][pawn_y])

        current_board[x][y] = fill_cell(current_board[x][y], current_piece)

    return current_board


board_test = [
    ["white_br", "black_bh", "white_bb", "black_bq", "white_bk", "black_00", "white_00", "black_br"],
    ["black_bp", "white_bp", "black_bp", "white_bp", "black_00", "white_bp", "black_bp", "white_bp"],
    ["white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_bp", "white_00", "black_00", "white_00"],   
    ["white_00", "black_00", "white_00", "black_00", "white_wp", "black_00", "white_00", "black_00"],
    ["black_00", "white_00", "black_00", "white_00", "black_00", "white_00", "black_00", "white_00"],
    ["white_wp", "black_wp", "white_wp", "black_00", "white_00", "black_wp", "white_wp", "black_wp"],
    ["black_wr", "white_wh", "black_wb", "white_wq", "black_wk", "white_00", "black_00", "white_wr"],
]   

def test_board():

    start_board = board_test
           
    return start_board
