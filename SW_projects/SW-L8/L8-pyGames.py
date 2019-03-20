import L8_UI as UI
import os
import tkinter as tk



class Player:
    def __init__(self, symbol):
        self.symbol=symbol

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

    def play_game(self):
        #method to get player input
        UI.show_game(self.board)
        return input

class Board:
    def __init__(self, tiles, name):
        self.tiles = tiles
        self.name = name
        self.board = [" "] * self.tiles

class TTTBoard(Board):

    def show_board(self):
        self.board()

def main():
    ttt_board = Board(3, "Tic Tac Toe")
    play_game = Player
    player1 = Player("X")
    player2 = Player("O")
    TTT_game = Game(ttt_board, player1, player2)
    TTT_game.play_game()


if __name__ == '__main__':
    main()

