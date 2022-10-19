import unittest
from unittest.mock import patch
from main import main

@patch('builtins.print')
@patch('builtins.input')

class TestMain(unittest.TestCase):

    def test_s(self, patched_input, patched_print, *args):
        patched_input.return_value = 's'
        main()
        self.assertEqual(patched_print.call_count, 7)
        patched_input.assert_called_once()

    def test_player1_win(self, patched_input, patched_print, *args):
        patched_input.side_effect = ['1','2','1','2','1','2','1','n']
        main()
        last_call = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_call - 1][0][0], 'Jugador 1 gana')

    def test_type_error(self, patched_input, patched_print, *args):
        patched_input.side_effect = ['1','1','1','1','1','1','1', 's']
        main()
        self.assertEqual(patched_print.call_args_list[49][0][0], 'Columna completa, ingrese otro número')

    def test_value_error(self, patched_input, patched_print, *args):
        patched_input.side_effect = ['d','s']
        main()
        self.assertEqual(patched_print.call_args_list[7][0][0],'Error, ingrese un número del 0 al 6')

    def test_index_error(self, patched_input, patched_print, *args):
        patched_input.side_effect = ['9', 's']
        main()
        self.assertEqual(patched_print.call_args_list[7][0][0], 'Error, ingrese un número del 0 al 6')



if __name__ == '__main__':
    unittest.main()
