# rock_paper_scissors.players.iplayer

from abc import ABC, abstractmethod
from rock_paper_scissors.moves.move_set import MoveSet

class IPlayer(ABC):
    move_set: type[MoveSet]

    @abstractmethod
    def make_move(self) -> MoveSet:
        pass