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

        expected_white_bishops = [Bishop(0, 2), Bishop(0, 5)]
        expected_black_bishops = [Bishop(7, 2), Bishop(7, 5)]

        for wb in expected_white_bishops:
            assert wb in white_pieces

        for bb in expected_black_bishops:
            assert bb in black_pieces

        # Check Rooks

        expected_white_rooks = [Rook(0, 0), Rook(0, 7)]
        expected_black_rooks = [Rook(7, 0), Rook(7, 7)]

        for wr in expected_white_rooks:
            assert wr in white_pieces

        for br in expected_black_rooks:
            assert br in black_pieces

        # Check Kings

        assert King(0, 4) in white_pieces
        assert King(7, 4) in black_pieces

        # Check Queens

        assert Queen(0, 3) in white_pieces
        assert Queen(7, 3) in black_pieces

    def test_has_piece(self):
        board = init_board()
        knight_row = 0
        knight_col = 1
        is_white = True
        self.assertEqual((Knight(knight_row, knight_col), is_white), board.has_piece(knight_row, knight_col))

        pawn_row = 6
        pawn_col = 7
        is_white = False
        self.assertEqual((Pawn(pawn_row, pawn_col), is_white), board.has_piece(pawn_row, pawn_col))

        empty_row = 4
        empty_col = 4
        self.assertEqual(None, board.has_piece(empty_row, empty_col))


if __name__ == '__main__':
    unittest.main()
