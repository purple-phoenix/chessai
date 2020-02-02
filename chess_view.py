import tkinter as tk

from chess_models import *

sticky = tk.N+tk.S+tk.E+tk.W


class ChessView(tk.Frame):
    board: Board

    def __init__(self, master=None):
        super().__init__(master)

        self.board = init_board()

        self.master = master
        self.show_board()

    def show_board(self):
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W, column=0, row=7, columnspan=2)
        tk.Grid.rowconfigure(self, 7, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        is_white_square = False
        for x in range(8):
            is_white_square = not is_white_square
            for y in range(8):
                if is_white_square:
                    bg = "white"
                else:
                    bg = "black"
                maybe_has_piece = self.board.has_piece(y, x)
                if maybe_has_piece is None:
                    text = ""
                else:
                    piece, is_white = maybe_has_piece
                    if is_white:
                        text = "White "
                    else:
                        text = "Black "
                    text += str(piece)
                btn = tk.Button(self, text=text, bg=bg)
                btn.grid(column=8-x, row=8-y)
                is_white_square = not is_white_square

        for x in range(8):
            tk.Grid.columnconfigure(self, x, weight=1)

        for y in range(8):
            tk.Grid.rowconfigure(self, y, weight=1)


def init_display():
    root = tk.Tk()
    root.geometry("1000x400")
    frame = tk.Frame(root)
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
    frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    chess_view = ChessView(master=root)
    chess_view.mainloop()
