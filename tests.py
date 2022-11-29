import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    
    def test_make_empty_board(self):
        board = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
         ]
        self.assertEqual(logic.make_empty_board(),board)

    def test_other_player(self):
        player="X"
        self.assertEqual(logic.other_player(player),"O")
    
    def test_isfull(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', None],
            ['O', 'X', None],
        ]
        #self.assertTrue(logic.isfull(board))
        self.assertFalse(logic.isfull(board))

    def test_check_move(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'X'],
        ]
        row=1
        col=1
        self.assertTrue(logic.check_move(board,row,col))
    
    def test_make_move(self):
        board = [
            ['X', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        player1="X"
        player2="O"
        now=1
        row=0
        col=0
        self.assertEqual(logic.make_move(board,player1,player2,now,row,col),board)

    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()
