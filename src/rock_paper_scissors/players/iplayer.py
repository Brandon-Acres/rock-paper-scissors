# rock_paper_scissors.players.iplayer

from abc import ABC, abstractmethod
from rock_paper_scissors.moves.basic_moves import BasicMove

class IPlayer(ABC):
    @abstractmethod
    def make_move(self) -> BasicMove:
        pass