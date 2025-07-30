# rock_paper_scissors.rules.basic_rules
"""Basic rock paper scissors rules as a nested dictionary."""

from rock_paper_scissors.moves.lizard_spock_moves import LizardSpockMove

LIZARD_SPOCK_RULES = {
    LizardSpockMove.ROCK: {
        LizardSpockMove.ROCK: "draw",
        LizardSpockMove.PAPER: "player2",
        LizardSpockMove.SCISSORS: "player1",
        LizardSpockMove.LIZARD: "player1",
        LizardSpockMove.SPOCK: "player2"
    },
    LizardSpockMove.PAPER: {
        LizardSpockMove.ROCK: "player1",
        LizardSpockMove.PAPER: "draw",
        LizardSpockMove.SCISSORS: "player2",
        LizardSpockMove.LIZARD: "player2",
        LizardSpockMove.SPOCK: "player1"
    },
    LizardSpockMove.SCISSORS: {
        LizardSpockMove.ROCK: "player2",
        LizardSpockMove.PAPER: "player1",
        LizardSpockMove.SCISSORS: "draw",
        LizardSpockMove.LIZARD: "player1",
        LizardSpockMove.SPOCK: "player2"
    },
    LizardSpockMove.LIZARD: {
        LizardSpockMove.ROCK: "player2",
        LizardSpockMove.PAPER: "player1",
        LizardSpockMove.SCISSORS: "player2",
        LizardSpockMove.LIZARD: "draw",
        LizardSpockMove.SPOCK: "player1"
    },
    LizardSpockMove.SPOCK: {
        LizardSpockMove.ROCK: "player1",
        LizardSpockMove.PAPER: "player2",
        LizardSpockMove.SCISSORS: "player1",
        LizardSpockMove.LIZARD: "player2",
        LizardSpockMove.SPOCK: "draw"
    }
}