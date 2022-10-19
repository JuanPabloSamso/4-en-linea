import unittest
from game import InLine

class TestInLine(unittest.TestCase):
    def test_board(self):
        game = InLine()
        self.assertEqual(len(game.board), 6)
        self.assertEqual(len(game.board[0]), 7)

    def test_players(self):
        game = InLine()
        self.assertEqual(game.player1,'X')
        self.assertEqual(game.player2,'Y')

    def test_available(self):
        game = InLine()
        game.available(1)
        self.assertEqual(game.available(0),5)

    def test_throw_coin(self):
        game = InLine()
        game.throw_coin(0)
        self.assertEqual(game.board[5][0],'X')

    def test_turn1(self):
        game = InLine()
        game.turn()
        self.assertEqual(game.player,2)

    def test_turn2(self):
        game = InLine()
        game.player =2
        game.turn()
        self.assertEqual(game.player,1)

    def test_turn_after_play(self):
        game = InLine()
        game.throw_coin(0)
        self.assertEqual(game.player,2)

    def test_check_col_empty(self):
        game = InLine()
        game.check_col()
        game.board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']] 
        self.assertEqual(game.check_col(),None)

    def test_check_col_win(self):
        game = InLine()
        game.check_col()
        game.board = [['X',' ',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_col(),True)

    def test_check_row_empty(self):
        game = InLine()
        game.check_row()
        game.board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_row(),None)

    def test_check_row_win(self):
        game = InLine()
        game.check_row()
        game.board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ','X','X','X','X']]
        self.assertEqual(game.check_row(),True)

    def test_check_diag_up_empty(self):
        game = InLine()
        game.check_diag_up()
        game.board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_diag_up(),None)
        
    def test_check_diag_up_win(self):
        game = InLine()
        game.check_diag_up()
        game.board = [[' ',' ',' ',' ',' ',' ','X'],[' ',' ',' ',' ',' ','X',' '],[' ',' ',' ',' ','X',' ',' '],[' ',' ',' ','X',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_diag_up(),True)

    def test_check_diag_down_empty(self):
        game = InLine()
        game.check_diag_down()
        game.board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_diag_down(),None)
        
    def test_check_diag_down_win(self):
        game = InLine()
        game.check_diag_down()
        game.board = [['X',' ',' ',' ',' ',' ',' '],[' ','X',' ',' ',' ',' ',' '],[' ',' ','X',' ',' ',' ',' '],[' ',' ',' ','X',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_diag_down(),True)

    def test_check_winner_1(self):
        game = InLine()
        game.check_winner()
        game.board = [['X',' ',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_winner(),True)

    def test_check_winner_2(self):
        game = InLine()
        game.check_winner()
        game.board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
        self.assertEqual(game.check_winner(),None)


if __name__ == '__main__':
    unittest.main() 
