import unittest

from chess_models import *


class TestModels(unittest.TestCase):

    def test_init_board(self):

        board = init_board()
        white_pieces = board.get_white_pieces()
        black_pieces = board.get_black_peices()
        # Check pawns
        for col in range(0, 8):
            white_pawn_row = 1
            black_pawn_row = 6
            expected_white_pawn = Pawn(white_pawn_row, col)
            expected_black_pawn = Pawn(black_pawn_row, col)
            assert expected_white_pawn in white_pieces
            assert expected_black_pawn in black_pieces

        # Check knights

        # Check bishops

        # Check Rooks

        # Check Kings

        # Check Queens


if __name__ == '__main__':
    unittest.main()
