# tests/test_app_flow.py
"""Basic integration test to verify that app, menu, and basic game interact correctly"""

import unittest
from unittest.mock import patch

from rock_paper_scissors.__main__ import main

class TestAppIntegration(unittest.TestCase):
    @patch('builtins.input')
    def test_full_game_flow(self, mock_input):
        # simulate user inputs:
        # 1. select basic RPS from menu
        # 2. play a short game (3 rounds) with moves: rock, paper, scissors
        # 3. Quit the app after the game

        mock_input.side_effect = [
            '1',        # choose basic RPS game
            '3',        # number of rounds
            'rock',     # round 1 user move
            'paper',    # round 2 user move
            'scissors', # round 3 user move
            'q'         # quit after game ends
        ]

        # run app via main function - goes through entire flow
        main()

        # Checking that no exceptions are raised and flow ends

if __name__ == '__main__':
    unittest.main()