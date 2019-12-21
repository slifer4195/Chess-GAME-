
num_col = 8
num_row = 8

board = [['R','N','B','K','Q','B','N','R'],
         ['P','P','P','P','P','P','P','P'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['p','p','p','p','p','p','p','p'],
         ['r','n','b','q','k','b','n','r']]

player1_piece = ['p' , 'r' , 'n' , 'b' , 'q' , 'k']
player2_piece = ['P' , 'R' , 'N' , 'B' , 'Q' , 'K']

#drawing the  board
def draw_board(board):
    for i in range(num_col):
        for j in range(num_row):
            print(board[i][j] , end= '   \t')
        print(' ', i)
        print('\n')
    print('____________________________________________________________________')
    for i in range(num_row):
        print(i, end = '   \t')
    print('\n')
draw_board(board)

#checks whose turn it is
def player_turn(turn):
    if turn == 0:
        return 'player 1'
    else:
        return 'player 2'


#make sure the user selected a piece
def valid_spot(board,col,row):
    if board[col][row] != '.':
        return True
    else:
        return False

#to know which piece the user selected
def identify_piece(board,col,row):
    if board[col][row] == 'p':
        return 'pawn'
    elif board[col][row] == 'P':
        return 'Pawn'
    elif board[col][row] == 'r':
        return 'rook'
    elif board[col][row] == 'R':
        return 'Rook'
    elif board[col][row] == 'n':
        return 'knight'
    elif board[col][row] == 'N':
        return 'Knight'
    elif board[col][row] == 'b':
        return 'bishop'
    elif board[col][row] == 'B':
        return 'Bishop'

#moving
def move(board, col, row, col_end, row_end):
    board[col_end][row_end] = board[col][row]
    board[col][row] = '.'

def invalid_move():
    global turn
    print('invalid move')
    turn -= 1

def possible_victim(player1_piece, player2_piece, player):
    if player == 'player 1':
        return player2_piece
    elif player == 'player 2':
        return player1_piece

#pawn characterstics
class pawn:
    def __init__(self, column , column_end, row, row_end,sign,player):
        self.col = col
        self.col_end = col_end
        self.row = row
        self.row_end = row_end
        self.sign = sign
        self.player = player

    def if_attack(self, sign):
        if row == 0:
            if row + 1 == row_end and col - (1 * sign) == col_end:
                return True
            else:
                return False
        elif row == 7:
            if row - 1 == row_end and col - (1 * sign) == col_end:
                return True
            else:
                return False
        else:
            if row + 1 == row_end and col - (1 * sign) == col_end:
                return True
            elif row - 1 == row_end and col - (1 * sign) == col_end:
                return True
            else:
                return False

    def if_go_up(self, sign):
        if row == row_end and col - (1 * sign)== col_end or row == row_end and col - (2 * sign) == col_end:
            return True
        else:
            return False

    def no_obstacle(self):
        if board[col_end][row_end] == '.':
            return True
        else:
            return False

    def valid_first_move(self,sign):
        if sign == 1:
            if col == 6:
                return True
            else:
                return False
        elif sign == -1:
            if col == 1:
                return True
            else:
                return False

    # pawn attack validation
    def attack_valid(self,sign , victim):
        # check for case when you are at the edge
        if row < 7:
            if col - (1 * sign) == col_end and row + 1 == row_end or col - (1 * sign) == col_end and row - 1 == row_end:
                if board[col_end][row_end] != '.' and board[col_end][row_end] in victim:
                    return True
                else:
                    return False
            else:
                return False
        elif row == 7:
            if col - (1 * sign) == col_end and row - 1 == row_end:
                if board[col_end][row_end] != '.' and board[col_end][row_end] in victim:
                    return True
                else:
                    return False
            else:
                return False

    #if its player 2, its moving direction changes player 1: 1, player 2: -1
    def sign_change(self):
        if player == 'player 1':
            sign = 1
        elif player == 'player 2':
            sign = -1
        return sign

class rook:

    def __init__(self,col, col_end, row, row_end , player , piece):
        self.col = col
        self.col_end = col_end
        self.row = row
        self.row_end = row_end
        self.player = player
        self.piece = piece

    #cheking if it it is moving vertically or horizontally
    def direction_check(self):
        if col == col_end and row != row_end:
            return 'horizontal'
        if col != col_end and row == row_end:
            return 'vertical'
        else:
            return False

    def up_down_check(self):
        if col > col_end :
            return 'up'
        elif col < col_end :
            return 'down'

    def up(self,  victim):
        counter = 0
        for c in range(col_end, col):
            if board[c][row] != '.':
                counter += 1
        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

    def down(self,  victim):
        counter = 0
        for c in range(col+1, col_end+1):
            if board[c][row] != '.':
                counter += 1
        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

    def right_left_check(self):
        if row > row_end :
            return 'left'
        elif row < row_end:
            return 'right'

    def right(self ,  victim):
        counter = 0
        for r in range(row+1, row_end+1):
            if board[col][r] != '.':
                counter += 1
        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

    def left(self,  victim):
        counter = 0
        for r in range(row_end, row):
            if board[col][r] != '.' :
                counter += 1
        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

class knight:

    def __init__(self, col, col_end , row, row_end):
        self.col = col
        self.col_end = col_end
        self.row = row
        self.row_end = row_end

    def valid_move(self):
        if row + 2 == row_end and col - 1 == col_end:
            return True
        elif row + 2 == row_end and col + 1 == col_end:
            return True
        elif row - 2 == row_end and col - 1 == col_end:
            return True
        elif row - 2 == row_end and col + 1 == col_end:
            return True
        elif row + 1 == row_end and col - 2 == col_end:
            return True
        elif row + 1 == row_end and col + 2 == col_end:
            return True
        elif row - 1 == row_end and col - 2 == col_end:
            return True
        elif row - 1 == row_end and col + 2 == col_end:
            return True
        else:
            return False

    def valid_destination(self, victim , destination):
        if destination == '.' or destination in victim:
            return True
        else:
            return False

class bishop:

    def __init__(self, col, col_end, row, row_end):
        self.col = col
        self.col_end = col_end
        self.row = row
        self.row_end = row_end

    def valid_bishop_move(self):
        col_diff = abs(col_end - col)
        row_diff = abs(row_end - row)
        if col_diff == row_diff:
            return True
        else:
            return False
    def condition_check(self):
        if row_end > row and col_end < col:
            return 1
        elif row_end > row and col_end > col:
            return 2
        elif col_end > col and row_end < row:
            return 3
        elif col_end < col and row_end < row:
            return 4
    def first_condition(self, victim):
        counter = 0
        c = col - 1

        for r in range(row + 1, row_end+1):
            if board[c][r] != '.':
                counter += 1
            c = c - 1

        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

    def second_condition(self, victim):
        counter = 0
        c = col + 1

        for r in range(row + 1, row_end + 1):
            if board[c][r] != '.':
                counter += 1
            c = c + 1

        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

    def third_condition(self, victim):
        counter = 0
        r = row -1

        for c in range(col+1, col_end+1):
            if board[c][r] != '.':
                counter += 1
            r -= 1

        if counter == 0:
            return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

    def forth_condition(self, victim):
        counter = 0
        c = col_end

        for r in range(row_end, row-1):
            if board[c][r] != '.':
                counter += 1
            c = c + 1

        if counter == 0:
              return True
        elif counter == 1:
            if board[col_end][row_end] in victim:
                return True
            else:
                return False
        else:
            return False

run = True
turn = 0

#main loop
while run:
    player = player_turn(turn)
    victim = possible_victim(player1_piece, player2_piece, player)

    col, row = map(int, input(player + ", enter the col(horizontal number) and the row(vertical number) for the selection of the piece: ").split())

    if valid_spot(board,col,row):

        piece = identify_piece(board,col,row)
        col_end, row_end = map(int, input(player + ", enter the col(horizontal number) and the row(vertical number) for the destination of the piece: ").split())

        if piece == 'pawn' and player == 'player 1' or piece == 'Pawn' and player == 'player 2':

            pawn_1 = pawn(col,col_end,row,row_end, 1 , player)
            sign = pawn_1.sign_change()

            if not pawn_1.if_attack(sign) and not pawn_1.if_go_up(sign):
                invalid_move()
            else:

                if pawn_1.if_go_up(sign):

                    if pawn_1.no_obstacle():

                        if col - (2 * sign) == col_end:
                            if pawn_1.valid_first_move(sign):
                                move(board, col, row, col_end, row_end)

                        else:
                            move(board, col, row, col_end, row_end)

                    else:
                        invalid_move()

                elif pawn_1.if_attack(sign):

                    if pawn_1.attack_valid(sign, victim):
                        move(board, col, row, col_end, row_end)
                    else:
                        invalid_move()

        elif piece == 'rook' and player == 'player 1' or piece == 'Rook' and player == 'player 2':

            rook_1 = rook(col, col_end, row, row_end , player, piece)
            if rook_1.direction_check() == 'horizontal' or rook_1.direction_check() == 'vertical':

                if rook_1.direction_check() == 'vertical':

                    if rook_1.up_down_check() == 'up':

                        if rook_1.up(victim):
                            move(board, col, row, col_end, row_end)
                        else:
                            invalid_move()

                    elif rook_1.up_down_check() == 'down':

                        if rook_1.down( victim):
                            move(board, col, row, col_end, row_end)
                        else:
                            invalid_move()

                elif rook_1.direction_check() == 'horizontal': #check for spelling

                    if rook_1.right_left_check()== 'right':
                        if rook_1.right(victim):
                            move(board, col, row, col_end, row_end)
                        else:
                            invalid_move()

                    elif rook_1.right_left_check() == 'left':
                        if rook_1.left( victim):
                            move(board, col, row, col_end, row_end)
                        else:
                            invalid_move()

            else:
                invalid_move()

        elif piece == 'knight' and player == 'player 1' or piece == 'Knight' and player == 'player 2':
            knight_1 = knight(col, col_end ,row, row_end)
            if knight_1.valid_move():
                destination = board[col_end][row_end]
                # print(destination)
                # print(knight_1.valid_destination(victim , destination))
                if knight_1.valid_destination(victim , destination):
                    move(board,col, row, col_end, row_end)
                    print('working')
                else:
                    print('nani')
                    invalid_move()
            else:
                invalid_move()

        elif piece == 'bishop' and player == 'player 1' or piece == 'Bishop' and player == 'player 2':

            bishop_1 = bishop(col, col_end, row, row_end)
            if bishop_1.valid_bishop_move():
                condition = bishop_1.condition_check()
                if condition == 1:
                    if bishop_1.first_condition(victim) == True:
                        move(board,col, row, col_end,row_end)
                    else:
                        invalid_move()
                elif condition == 2:
                    if bishop_1.second_condition(victim) == True:
                        move(board, col, row, col_end, row_end)
                    else:
                        invalid_move()

                elif condition == 3:

                    if bishop_1.third_condition(victim) == True:
                        move(board, col, row, col_end, row_end)
                    else:
                        invalid_move()

                elif condition == 4:
                    if bishop_1.forth_condition(victim) == True:
                        move(board, col, row, col_end, row_end)
                    else:
                        invalid_move()

    else:
        invalid_move()

    turn += 1
    turn = turn % 2
    draw_board(board)

