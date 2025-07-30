# rock_paper_scissors.rules.basic_rules
"""Basic rock paper scissors rules as a nested dictionary."""

from rock_paper_scissors.moves.basic_moves import BasicMove

BASIC_RULES = {
    BasicMove.ROCK: {
        BasicMove.ROCK: "draw",
        BasicMove.PAPER: "player2",
        BasicMove.SCISSORS: "player1"
    },
    BasicMove.PAPER: {
        BasicMove.ROCK: "player1",
        BasicMove.PAPER: "draw",
        BasicMove.SCISSORS: "player2"
    },
    BasicMove.SCISSORS: {
        BasicMove.ROCK: "player2",
        BasicMove.PAPER: "player1",
        BasicMove.SCISSORS: "draw"
    }
}