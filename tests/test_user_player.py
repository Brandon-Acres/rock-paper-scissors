import unittest
from unittest.mock import patch # for testing user input

from rock_paper_scissors.players.user_player import UserPlayer
from rock_paper_scissors.moves.basic_moves import BasicMove
from typing import cast
from rock_paper_scissors.moves.move_set import MoveSet

class TestUserPlayer(unittest.TestCase):
    def setUp(self):
        self.player = UserPlayer(cast(type[MoveSet], BasicMove))

    @patch("builtins.input", return_value="rock")
    def test_make_move_valid_input(self, mock_input):
        move = self.player.make_move()
        self.assertEqual(move, BasicMove.ROCK)

    @patch("builtins.input", side_effect=["banana", "scissors"])
    def test_make_move_invalid_then_valid(self, mock_input):
        # simulates looping until valid input given
        move = self.player.make_move()
        self.assertEqual(move, BasicMove.SCISSORS)

if __name__ == "__main__":
    unittest.main()