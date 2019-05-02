
class Game:
    def __init__(self, player1, player2, domain, board, root=None):
        self.player1 = player1
        self.player2 = player2
        self.root = root                 #UI
        self.board = board
        self.domain = domain
        self.turn = None

    def play(self):
        self.board.config_init_state()

        while self.board.state == "play":
            if self.turn is None or self.turn == self.player2:
                self.turn = self.player1
            elif self.turn == self.player2:
                self.turn = self.player1

            self.board.get_input(self.turn)
            self.board.update_state(self.player1, self.player2)

        self.end_game()

    def end_game(self):
        msg = ""
        if self.board.state == "tie":
            msg = "tie"
        elif self.board.state == "winner":
            msg = "winner: " + self.turn.name
        return msg


class Board:
    def __init__(self, domain =None, root=None):
       # self.board = None  # list of buttons
        self.board = [[" "]*3]*3
        self.state = ""
        self.domain = domain
        self.root = root #used for UI

    def config_init_state(self):
        pass

    def update_state(self, player1 = None, player2 = None):
        pass

    def get_input(self, player):
        player.get_player_input()

    def print_board(self):
        print("    ==" + "===" * len(self.board[0]) + "="* int(len(self.board[0])-1) + "==")
        x = "    ||" + "---" * len(self.board[0]) + "-"* int(len(self.board[0])-1) + "||"
        for i in range(len(self.board)):
            print(x)
            print(" {}  ||".format(i+1), end = '')
            for j in range(len(self.board[i])):
                print(" " + str(self.board[i][j]) + " |", end = '')
                if j+1 == len(self.board[i]):
                    print("|")
        print("    ==" + "===" * len(self.board[0]) + "=" * int(len(self.board[0]) - 1) + "==")


class Player:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.type = "human"

    def get_player_input(self):
        pass


