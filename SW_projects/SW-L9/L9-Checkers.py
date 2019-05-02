import L9_BoardGame as L9


class Token:
    def __init__(self, color, pos_x=0, pos_y=0):
        self.color = color  # array [peasant symbol, King symbol ] or [O, Ô]
        self.status = "peasant"  # array [ alive / dead, king / peasant]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.symbol = color[0]

    def get_moves(self):
        if self.status[1] == "peasant":
            return [[self.pos_x - 1, self.pos_y + 1], [self.pos_x + 1, self.pos_y + 1]]

        elif self.status[0] == "king":
            return [[self.pos_x - 1, self.pos_y + 1], [self.pos_x + 1, self.pos_y + 1],
                    [self.pos_x - 1, self.pos_y - 1],
                    [self.pos_x + 1, self.pos_y - 1]]

    def move(self, new_x, new_y):
        if new_y == 8 and self.status == "peasant":
            self.symbol = self.color[1]
            self.status = "king"

        self.pos_x = new_x
        self.pos_y = new_y

    def __str__(self):
        return self.color

class CheckersBoard(L9.Board):
    def __init__(self):
        super(CheckersBoard, self).__init__()
        # self.board = [[" "]*8]*8
        self.board = [[" "]*8 for _ in range(8)]
        self.state = "play"

    def print_board(self):
        super(CheckersBoard, self).print_board()
        print("    || A   B   C   D   E   F   G   E ||")
        print("    ===================================")

    def config_init_state(self, player1, player2):
        Black_init_pos = [[[0, 0], [0, 2], [0, 4], [0, 6]], [[1, 1], [1, 3], [1, 5], [1, 7]], [[2, 0], [2, 2], [2, 4], [2, 6]]]
        Red_init_pos = [[[5, 1], [5, 3], [5, 5], [5, 7]], [[6, 0], [6, 2], [6, 4], [6, 6]], [[7, 1], [7, 3], [7, 5], [7, 7]]]

        j = 0
        i = 0

        for token in player1.tokens:
            token.pos_x = Black_init_pos[j][i][1]
            # print(str(i)+'-'+str(j))
            token.pos_y = Black_init_pos[j][i][0]
            self.board[token.pos_y][token.pos_x] = token
            i = i + 1
            if i > 3:
                i = 0
                j = j +1

        j = 0
        i = 0

        for token in player2.tokens:
            token.pos_x = Red_init_pos[j][i][1]
            # print(str(i)+'-'+str(j))
            token.pos_y = Red_init_pos[j][i][0]
            self.board[token.pos_y][token.pos_x] = token
            i = i + 1
            if i > 3:
                i = 0
                j = j +1


class CheckersPlayer(L9.Player):
    def __init__(self, name, domain):
        super(CheckersPlayer, self).__init__(name, domain)
        self.tokens = None

    def create_tokens(self):
        i = 0
        self.tokens = []

        while i < 12:
            newToken = Token(self.domain[0])
            self.tokens.append(newToken)
            i = i + 1

    def get_player_input(self):
        print("Your tokens:")
        # print list of tokens
        # ask user to select a move
        # validate in game class
        # ask for input, again, if needed


def main():

    checkers_board = CheckersBoard()
    checkers_board.print_board()

    player1 = CheckersPlayer("red", ['U', 'Û'])
    player1.create_tokens()
    player2 = CheckersPlayer("black", ['O', 'Ô'])
    player2.create_tokens()
    checkers_board.config_init_state(player1, player2)
    checkers_board.print_board()


if __name__ == '__main__':
    main()







