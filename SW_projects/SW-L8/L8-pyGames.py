import tkinter as Tk
turn = 0

class Tile:
    def __init__(self, pos_x, pos_y, board, root):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.board = board
        self.btn= Tk.Button(root, text=self.board.board[pos_x][pos_y], fg="Black",width=3,height=1,font=('Helvetica','20'), command=self.board.on_click(pos_x, pos_y))
        self.btn.grid(column=pos_x, row=pos_y)

# model
class Board:

    def __init__(self, n_tiles, name):
        self.n_tiles = n_tiles
        self.name = name
        self.board = [[" "] * self.n_tiles]*self.n_tiles
        self.the_tiles=[]

    def get_board(self, root):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                newTile = Tile(i,j,self,root)
                self.the_tiles.append(newTile)

    def on_click(self, i, j):
        global turn
        if turn%2==0:
            self.board[i][j]= "X"
        elif turn>0:
            self.board[i][j]="O"
        turn = turn + 1

# View
class Screen:
    def __init__(self, root, board, turn):
        self.frame = Tk.Frame(root)
        self.board = board
        self.lbl = Tk.Label(root,text="turn: " + turn, font=('Helvetica', 10))
        self.lbl.grid(row=1,column=5)
        root.geometry("300x200")


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.board = Board(3, "Tic Tac Toe game")
        self.Screen = Screen(self.root, self.board, turn=" ")

    def run(self):
        self.root.title(self.board.name)
        self.board.get_board(self.root)
        # self.root.deiconify()
        self.root.mainloop()


def main():
    c = Controller()
    c.run()


if __name__ == '__main__':
    main()