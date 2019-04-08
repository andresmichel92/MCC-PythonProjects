import L8-BoardGame as L8
from tkinter import *
from tkinter import messagebox

class TTTGame(L8.Game):


class TTTboard(L8.Board):
    def __init__(self):


def show_game(a_board):

    window = Tk()
    window.title(a_board.name)
    lbl = Label(window, text=a_board.name)
    window.mainloop()


def show_win(win_message):
    messagebox.showinfo("WIN!!!!", win_message)