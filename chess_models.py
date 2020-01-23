from typing import List, Tuple, Union


class AbsPiece:

    def __init__(self, row: int, col: int):
        self.row = row  # Row piece is located on board from white perspective. Bottommost is 0 topmost is 7
        self.col = col  # Col piece is located on board from white perspective. Leftmost is 0 right most is 7


class Pawn(AbsPiece):

    def __init__(self, row: int, col: int):
        super().__init__(row, col)

    def __eq__(self, other):
        return isinstance(other, Pawn) and self.col == other.col and self.row == other.row


class Knight(AbsPiece):

    def __init__(self, row: int, col: int):
        super().__init__(row, col)

    def __eq__(self, other):
        return isinstance(other, Knight) and self.col == other.col and self.row == other.row


class Bishop(AbsPiece):
    def __init__(self, row: int, col: int):
        super().__init__(row, col)

    def __eq__(self, other):
        return isinstance(other, Bishop) and self.col == other.col and self.row == other.row


class Rook(AbsPiece):
    def __init__(self, row: int, col: int):
        super().__init__(row, col)

    def __eq__(self, other):
        return isinstance(other, Rook) and self.col == other.col and self.row == other.row


Piece = Union[Pawn, Knight, Bishop]


class Board:
    white_pieces: List[Piece]
    black_pieces: List[Piece]

    def __init__(self, wp: [Piece], bp: List[Piece]):
        self.white_pieces = wp
        self.black_pieces = bp

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces


def init_board() -> Board:
    white_pieces = []
    black_pieces = []
    white_pawn_row = 1
    black_pawn_row = 6
    for col in range(0, 8):
        white_pieces.append(Pawn(white_pawn_row, col))
        black_pieces.append(Pawn(black_pawn_row, col))

    white_main_piece_row = 0
    black_main_piece_row = 7

    knight_cols = [1, 6]
    for col in knight_cols:
        white_pieces.append(Knight(white_main_piece_row, col))
        black_pieces.append(Knight(black_main_piece_row, col))

    bishops_cols = [2, 5]
    for col in bishops_cols:
        white_pieces.append(Bishop(white_main_piece_row, col))
        black_pieces.append(Bishop(black_main_piece_row, col))

    rook_cols = [0, 7]
    for col in rook_cols:
        white_pieces.append(Rook(white_main_piece_row, col))
        black_pieces.append(Rook(black_main_piece_row, col))

    return Board(white_pieces, black_pieces)






























