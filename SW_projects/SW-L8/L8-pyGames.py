import os

class Player:
    def __init__(self, symbol):
        self.symbol=symbol

    def play(self):
        #method to get player input
        ask_input()
        return input


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.player_turn = player1

    def turn(self):
        if self.player_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn= self.player1


class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.board_scheme = "tiles by tiles matrix"

    def create_board(self):
        board = [" "] * self.tiles

class TTTBoard(Board):

    def show_board(self):
        #nice method to show board

