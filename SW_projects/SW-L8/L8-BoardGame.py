import tkinter as tk


class Game:
    def __init__(self, player1, player2, board, domain):
        self.player1 = player1
        self.player2 = player2
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

            self.turn.get_input()
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
    def __init__(self):
        self.board = [] # list of buttons
        self.state = ""
        self.domain = []

    def config_init_state(self):
        pass

    def update_state(self):
        pass


class Player:

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.type = "human"

    def get_input(self):
        pass    # good luck with this one
