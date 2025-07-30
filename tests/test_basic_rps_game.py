# tests/test_basic_rps_game.py

import unittest
from unittest.mock import patch
from rock_paper_scissors.players.user_player import UserPlayer
from rock_paper_scissors.players.random_computer_player import RandomComputerPlayer
from rock_paper_scissors.moves.basic_moves import BasicMove
from rock_paper_scissors.moves.move_set import MoveSet
from typing import cast
from rock_paper_scissors.games.basic_rps_game import BasicRPSGame
from rock_paper_scissors.rules.basic_rules import BASIC_RULES

class TestBasicRPSGame(unittest.TestCase):
    @patch("builtins.input")
    def test_play_game_with_user_input(self, mock_input):
        # Simulate three user moves: rock, paper, scissors

        user = UserPlayer(cast(type[MoveSet], BasicMove))
        computer = RandomComputerPlayer(cast(type[MoveSet], BasicMove))
        game = BasicRPSGame(user, computer, BASIC_RULES)

        rounds = [3, 5, 7, 100, 1000]
        for r in rounds:
            mock_input.side_effect = ["rock", "paper", "scissors"]* (r // 3 + 1)
            game.play(r)

            # Check right number of rounds played
            self.assertEqual(game.round, r)
            self.assertLessEqual(sum(game.score.values()), r)


from rock_paper_scissors.players.iplayer import IPlayer

class TestDeterministicGame(unittest.TestCase):
    def test_deterministic_game(self):
        # predefined moves: user wins 2, computer wins 1, 1 draw
        user_moves = [BasicMove.ROCK, BasicMove.PAPER, BasicMove.SCISSORS, BasicMove.ROCK]
        comp_moves = [BasicMove.SCISSORS, BasicMove.ROCK, BasicMove.ROCK, BasicMove.ROCK]

        class MockPlayer(IPlayer):
            def __init__(self, moves, move_set: type[MoveSet]):
                self.moves = moves
                self.index = 0
                self.move_set = move_set

            def make_move(self):
                move = self.moves[self.index]
                self.index += 1
                return move
        
        user = MockPlayer(user_moves, cast(type[MoveSet], BasicMove))
        computer = MockPlayer(comp_moves, cast(type[MoveSet], BasicMove))
        game = BasicRPSGame(user, computer, BASIC_RULES)

        game.play(len(user_moves))

        self.assertEqual(game.score['player1'], 2)
        self.assertEqual(game.score['player2'], 1)
        self.assertEqual(game.round, 4)

if __name__ == "__main__":
    unittest.main()