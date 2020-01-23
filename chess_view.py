import tkinter as tk

from chess_models import *


class ChessView(tk.Frame):
    board: Board

    def __init__(self, master=None):
        super().__init__(master)

        self.board = init_board()

        self.master = master
        self.pack()
        self.show_board()

    def show_board(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = lambda: print("hi there!")
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)


def init_display():
    root = tk.Tk()
    chess_view = ChessView(master=root)
    chess_view.mainloop()
