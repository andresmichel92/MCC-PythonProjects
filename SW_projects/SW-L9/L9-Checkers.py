import L9_BoardGame as L9


class Token:
    def __init__(self, color, pos_x, pos_y):
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


class CheckersPlayer(L9.Board):

    def __init__(self, name, domain):
        super(CheckersPlayer, self).__init__(name, domain)
        # Create tokens


def main():

    checkers_board = CheckersBoard()
    checkers_board.print_board()


if __name__ == '__main__':
    main()







