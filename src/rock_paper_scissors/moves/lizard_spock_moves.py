# rock_paper_scissors.moves.lizard_spock_moves

from enum import Enum, auto
from rock_paper_scissors.moves.move_set import MoveSet

class LizardSpockMove(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    LIZARD = "lizard"
    SPOCK = "spock"

    @classmethod 
    def from_string(cls, s: str) -> "LizardSpockMove":
        for move in cls:
            if move.value == s.lower():
                return move
        raise ValueError(f"Invalid move: {s}")

    @classmethod
    def list_moves(cls) -> list[str]:
        return [move.value for move in cls]
    
    @classmethod
    def to_string(cls, move: "LizardSpockMove") -> str:
        return move.value