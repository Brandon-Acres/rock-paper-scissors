# rock_paper_scissors.games.template_rps_game
"""Template creating abstract structure of a rock, paper, scissors game.
"""

from abc import ABC, abstractmethod
from rock_paper_scissors.moves.move_set import MoveSet
from rock_paper_scissors.players.iplayer import IPlayer

class TemplateRPSGame(ABC):
    def __init__(self, player1: IPlayer, player2: IPlayer,):
        self.round = 0
        self.score = {"player1": 0, "player2": 0}
        self.player1 = player1
        self.player2 = player2

    def play(self, round_limit: int) -> None:
        """Runs the rock paper scissors game loop."""
        while self.round < round_limit:
            print(f"\nRound {self.round + 1}")
            move1 = self.get_player1_move()
            move2 = self.get_player2_move()
            print(f"Player 1 chose {self.player1.move_set.to_string(move1)}, Player 2 chose {self.player1.move_set.to_string(move2)}")
            result = self.resolve_round(move1, move2)
            self.update_score(result)
            self.round += 1

        self.display_winner()
    
    @abstractmethod
    def get_player1_move(self) -> MoveSet:
        ...
    
    @abstractmethod
    def get_player2_move(self) -> MoveSet:
        ...

    @abstractmethod
    def resolve_round(self, move1: MoveSet, move2: MoveSet) -> str:
        """Return 'player1', 'player2', or 'draw'."""
        ...

    @abstractmethod
    def display_winner(self) -> None:
        ...

    def update_score(self, result: str) -> None:
        if result in self.score:
            self.score[result] += 1
        print(f"Score: {self.score}")

    def reset_round(self) -> None:
        self.round = 0

    def reset_score(self) -> None:
        self.score = {"player1": 0, "player2": 0}


