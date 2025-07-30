# rock_paper_scissors.games.basic_rps_game

from rock_paper_scissors.games.template_rps_game import TemplateRPSGame
from rock_paper_scissors.moves.move_set import MoveSet
from rock_paper_scissors.players.iplayer import IPlayer


from typing import cast

class BasicRPSGame(TemplateRPSGame):
    def __init__(self, player1: IPlayer, player2: IPlayer, ruleset: dict):
        # inherits:
        # self.round
        # self.score
        # self.player1 
        # self.player2 
        super().__init__(player1, player2)
        # adds:
        # validate:
        self.validate_ruleset(ruleset, self.player1.move_set)
        self.validate_ruleset(ruleset, self.player2.move_set)
        self.ruleset = ruleset

    def get_player1_move(self) -> MoveSet:
        return cast(type[MoveSet], self.player1.make_move())
    
    def get_player2_move(self) -> MoveSet:
        return cast(type[MoveSet], self.player2.make_move())
    
    def resolve_round(self, move1: MoveSet, move2: MoveSet) -> str:
        # Use the basic ruleset lookup table
        result = self.ruleset[move1][move2]
        if result == "draw":
            print("Players draw")
        else:
            print(f"{result} wins the round")
        return result
    
    def display_winner(self) -> None:
        print("\nFinal scores: ")
        for player in self.score.keys():
            print(f"{player}: {self.score[player]}")
        # identify winner:
        if self.score["player1"] == self.score["player2"]:
            print("It was a draw")
        elif self.score["player1"] > self.score["player2"]:
            print("Player1 wins")
        else:
            print("Player2 wins")
    
    def validate_ruleset(self, ruleset: dict, move_set: type[MoveSet]) -> None:
        expected_moves = set(move_set)

        # check top-level keys
        if set(ruleset.keys()) != expected_moves:
            raise ValueError("Top-level keys in ruleset do not motach move set")
        
        # check nested keys
        for outer_move, outcomes in ruleset.items():
            if set(outcomes.keys()) != expected_moves:
                raise ValueError(f"Inner dict for {outer_move} does not match move set")
    
