# rock_paper_scissors.moves.basic_moves

from enum import Enum, auto
from rock_paper_scissors.moves.move_set import MoveSet

class BasicMove(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @classmethod 
    def from_string(cls, s: str) -> "BasicMove":
        for move in cls:
            if move.value == s.lower():
                return move
        raise ValueError(f"Invalid move: {s}")

    @classmethod
    def list_moves(cls) -> list[str]:
        return [move.value for move in cls]
    
    @classmethod
    def to_string(cls, move: "BasicMove") -> str:
        return move.value

