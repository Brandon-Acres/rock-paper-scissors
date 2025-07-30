# tests/test_main_menu.py

from rock_paper_scissors.menu import show_main_menu, MenuOption
import unittest
from unittest.mock import patch

class TestMainMenu(unittest.TestCase):
    @patch('builtins.input')
    def test_menu_requires_valid_menu_option(self, mock_input):
        # simulates entering invalid main menu options until a correct menu option is entered

        inputs = ["not_valid_input_string", 3, 33.4, "5", "p", "1"]

        mock_input.side_effect = inputs
        entered_menu_option = show_main_menu()

        self.assertEqual(entered_menu_option, MenuOption.PLAY_BASIC_RPS)

if __name__ == "__main__":
    unittest.main()