import unittest

from chess_models import *


class TestModels(unittest.TestCase):

    def test_init_board(self):
        board = init_board()
        white_pieces = board.get_white_pieces()
        black_pieces = board.get_black_pieces()
        # Check pawns
        for col in range(0, 8):
            white_pawn_row = 1
            black_pawn_row = 6
            expected_white_pawn = Pawn(white_pawn_row, col)
            expected_black_pawn = Pawn(black_pawn_row, col)
            assert expected_white_pawn in white_pieces
            assert expected_black_pawn in black_pieces

        # Check knights
        expected_white_knights = [Knight(0, 1), Knight(0, 6)]
        for expected_white_knight in expected_white_knights:
            assert expected_white_knight in white_pieces

        expected_black_knights = [Knight(7, 1), Knight(7, 6)]
        for expected_black_knight in expected_black_knights:
            assert expected_black_knight in black_pieces
        # Check bishops

        # Check Rooks

        # Check Kings

        # Check Queens


if __name__ == '__main__':
    unittest.main()
