import chess_main
import pieces

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

    start_board[0][0] = chess_main.fill_cell(start_board[0][0], black_rook.get_avatar())
    start_board[0][1] = chess_main.fill_cell(start_board[0][1], black_horse.get_avatar())
    start_board[0][2] = chess_main.fill_cell(start_board[0][2], black_bishop.get_avatar())
    start_board[0][3] = chess_main.fill_cell(start_board[0][3], black_queen.get_avatar())
    start_board[0][4] = chess_main.fill_cell(start_board[0][4], black_king.get_avatar())
    start_board[0][5] = chess_main.fill_cell(start_board[0][5], black_bishop.get_avatar())
    start_board[0][6] = chess_main.fill_cell(start_board[0][6], black_horse.get_avatar())
    start_board[0][7] = chess_main.fill_cell(start_board[0][7], black_rook.get_avatar())

    start_board[1][0] = chess_main.fill_cell(start_board[1][0], black_pawn.get_avatar())
    start_board[1][1] = chess_main.fill_cell(start_board[1][1], black_pawn.get_avatar())
    start_board[1][2] = chess_main.fill_cell(start_board[1][2], black_pawn.get_avatar())
    start_board[1][3] = chess_main.fill_cell(start_board[1][3], black_pawn.get_avatar())
    start_board[1][4] = chess_main.fill_cell(start_board[1][4], black_pawn.get_avatar())
    start_board[1][5] = chess_main.fill_cell(start_board[1][5], black_pawn.get_avatar())
    start_board[1][6] = chess_main.fill_cell(start_board[1][6], black_pawn.get_avatar())
    start_board[1][7] = chess_main.fill_cell(start_board[1][7], black_pawn.get_avatar())

    start_board[6][0] = chess_main.fill_cell(start_board[1][0], white_pawn.get_avatar())
    start_board[6][1] = chess_main.fill_cell(start_board[1][1], white_pawn.get_avatar())
    start_board[6][2] = chess_main.fill_cell(start_board[1][2], white_pawn.get_avatar())
    start_board[6][3] = chess_main.fill_cell(start_board[1][3], white_pawn.get_avatar())
    start_board[6][4] = chess_main.fill_cell(start_board[1][4], white_pawn.get_avatar())
    start_board[6][5] = chess_main.fill_cell(start_board[1][5], white_pawn.get_avatar())
    start_board[6][6] = chess_main.fill_cell(start_board[1][6], white_pawn.get_avatar())
    start_board[6][7] = chess_main.fill_cell(start_board[1][7], white_pawn.get_avatar())

    start_board[7][0] = chess_main.fill_cell(start_board[0][0], white_rook.get_avatar())
    start_board[7][1] = chess_main.fill_cell(start_board[0][1], white_horse.get_avatar())
    start_board[7][2] = chess_main.fill_cell(start_board[0][2], white_bishop.get_avatar())
    start_board[7][3] = chess_main.fill_cell(start_board[0][3], white_queen.get_avatar())
    start_board[7][4] = chess_main.fill_cell(start_board[0][4], white_king.get_avatar())
    start_board[7][5] = chess_main.fill_cell(start_board[0][5], white_bishop.get_avatar())
    start_board[7][6] = chess_main.fill_cell(start_board[0][6], white_horse.get_avatar())
    start_board[7][7] = chess_main.fill_cell(start_board[0][7], white_rook.get_avatar())
        
    return start_board