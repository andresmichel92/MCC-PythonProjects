import L9_BoardGame as L9


class Token:
    def __init__(self, color, pos_x =0, pos_y=0):
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


class CheckersBoard(L9.Board):
    def __init__(self):
        self.board = [[" "]*8]*8
        self.state = "play"


class CheckersPlayer(L9.Player):
    def __init__(self, name, domain):
        super(CheckersPlayer, self).__init__(name, domain)
        self.tokens = None

    def create_tokens(self):
        i = 0
        self.tokens = []
        while i < 12:
            newToken = Token(self.domain)
            self.tokens.append(newToken)


    def get_player_input(self):
        print("Your tokens:")
        # print list of tokens
        # ask user to select a move
        # validate in game class
        # ask for input, again, if needed


def main():

    checkers_board = CheckersBoard()
    checkers_board.print_board()


if __name__ == '__main__':
    main()







