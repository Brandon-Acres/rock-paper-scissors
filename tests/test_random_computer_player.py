import unittest

from rock_paper_scissors.players.random_computer_player import RandomComputerPlayer
from rock_paper_scissors.moves.basic_moves import BasicMove

class TestUserPlayer(unittest.TestCase):
    def setUp(self):
        self.player = RandomComputerPlayer(BasicMove)

    def test_random_move_is_always_valid(self):
        for _ in range(100):
            move = self.player.make_move()      
            self.assertIn(move, list(BasicMove))


if __name__ == "__main__":
    unittest.main()