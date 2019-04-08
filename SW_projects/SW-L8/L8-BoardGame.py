import tkinter as tk


class Game:
    def __init__(self, player1, player2, domain, root, board):
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
            self.board.update_state()

        self.end_game()

    def end_game(self):
        msg = ""
        if self.board.state == "tie":
            msg = "tie"
        elif self.board.state == "winner":
            msg = "winner: " + self.turn.name
        return msg


class Board:
    def __init__(self, root=None):
        self.board = [] # list of buttons
        self.state = ""
        self.domain = "#"
        self.root = root #used for UI

    def config_init_state(self):
        pass

    def update_state(self):
        pass

    def get_input(self, player):
        # setattr(self, "domain", player.get_player_input())
        self.domain = player.get_player_input()
        print("this is getting print: " + self.domain)

class Player:

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.type = "human"

    def get_player_input(self):
        return self.domain    # good luck with this one


class TTTboard(Board):
    def __init__(self, root):
        super(TTTboard, self).__init__(root)
        self.btn1 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command= lambda: self.clicked(self.btn1))
        self.btn1.grid(column=1, row=1)
        self.btn2 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn2))
        self.btn2.grid(column=2, row=1)
        self.btn3 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn3))
        self.btn3.grid(column=3, row=1)
        self.btn4 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn4))
        self.btn4.grid(column=1, row=2)
        self.btn5 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn5))
        self.btn5.grid(column=2, row=2)
        self.btn6 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn6))
        self.btn6.grid(column=3, row=2)
        self.btn7 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn7))
        self.btn7.grid(column=1, row=3)
        self.btn8 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn8))
        self.btn8.grid(column=2, row=3)
        self.btn9 = tk.Button(self.root, text=" ", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: self.clicked(self.btn9))
        self.btn9.grid(column=3, row=3)

    def config_init_state(self):
        self.board = [self.btn1["text"], self.btn2["text"], self.btn3["text"], self.btn4["text"], self.btn5["text"],
                      self.btn6["text"], self.btn7["text"], self.btn8["text"], self.btn9["text"]]

    def clicked1(self):
        if self.btn1["text"] == " ":  # For getting the text of a button
            self.btn1["text"] = self.domain

    def clicked(self, button):
        print(self.board)
        if button["text"] == " ":
            button["text"] = self.domain

def main():
    # set Domain
    Dmn = ["X", "O"]
    # create Players
    player1 = Player("P1", Dmn[0])
    player2 = Player("P1", Dmn[1])
    print("domains: Player1= "+player1.domain+" Player2= "+player2.domain)
    # create root window
    window = tk.Tk()
    # set board
    the_board = TTTboard(window)
    # set game
    TicTacToe = Game(player1, player2, Dmn, window, the_board)
    TicTacToe.play()
    print(TicTacToe.turn)
    TicTacToe.root.mainloop()


if __name__ == '__main__':
    main()
