# rock_paper_scissors.players.random_computer_player

from rock_paper_scissors.players.iplayer import IPlayer
from rock_paper_scissors.moves.move_set import MoveSet
import random
from enum import Enum

# inherits from IPlayer
class RandomComputerPlayer(IPlayer):
    def __init__(self, move_set: type[MoveSet]):
        """Computer player that returns a random choice from a given MoveSet.

        Args:
            move_set (type[Enum]): an Enum class that also implements the MoveSet interface.
        """
        self.move_set = move_set

    def make_move(self) -> MoveSet:
        # select random choice
        return random.choice(list(self.move_set))