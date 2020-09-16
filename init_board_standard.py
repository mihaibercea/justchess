def init_board_standard():

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
    start_board[7][2] = fill_cell(start_board[0][2], white_bishop.get_avatar())
    start_board[7][3] = fill_cell(start_board[0][3], white_queen.get_avatar())
    start_board[7][4] = fill_cell(start_board[0][4], white_king.get_avatar())
    start_board[7][5] = fill_cell(start_board[0][5], white_bishop.get_avatar())
    start_board[7][6] = fill_cell(start_board[0][6], white_horse.get_avatar())
    start_board[7][7] = fill_cell(start_board[0][7], white_rook.get_avatar())
        
    return start_board