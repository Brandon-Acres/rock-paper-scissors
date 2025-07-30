# rock_paper_scissors.moves.move_set

from typing import Protocol, TypeVar, Iterator

T = TypeVar("T", bound="MoveSet") 

class MoveSet(Protocol):
    @classmethod
    def from_string(cls: type[T], s: str) -> T:
        """Parses a string and returns a Move enum."""
        ...

    @classmethod
    def to_string(cls: type[T], move: T) -> str:
        """Takes a MoveSet value and returns its string representation"""
        ...

    @classmethod
    def list_moves(cls: type[T]) -> list[str]:
        """Returns list of valid move strings (for help/UI)."""
        ...

    @classmethod
    def __iter__(cls: type[T]) -> Iterator[T]: ...