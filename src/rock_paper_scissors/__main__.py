# rock_paper_scissors.__main__

from rock_paper_scissors.menu import show_main_menu, MenuOption
from rock_paper_scissors.games.basic_rps_game import BasicRPSGame
from rock_paper_scissors.players.user_player import UserPlayer
from rock_paper_scissors.players.random_computer_player import RandomComputerPlayer
from rock_paper_scissors.moves.basic_moves import BasicMove
from rock_paper_scissors.moves.move_set import MoveSet
from rock_paper_scissors.moves.lizard_spock_moves import LizardSpockMove
from rock_paper_scissors.rules.basic_rules import BASIC_RULES
from rock_paper_scissors.rules.lizard_spock_rules import LIZARD_SPOCK_RULES
from typing import cast

def main():
    while True:
        choice = show_main_menu()

        match choice:
            case MenuOption.PLAY_BASIC_RPS:
                game = create_basic_rps_game(cast(type[MoveSet], BasicMove), BASIC_RULES)
                rounds = get_rounds_from_user()
                game.play(rounds)

            case MenuOption.PLAY_LIZARD_SPOCK_BASIC_RPS:
                game = create_basic_rps_game(cast(type[MoveSet], LizardSpockMove), LIZARD_SPOCK_RULES)
                rounds = get_rounds_from_user()
                game.play(rounds)
                
            case MenuOption.QUIT:
                print("Thanks for playing!")
                break

def get_rounds_from_user() -> int:
    while True:
        try:
            rounds = int(input("Enter number of rounds you would like to play: "))
            return rounds
        except ValueError:
            print("Invalid input - enter an integer number of rounds")

def create_basic_rps_game(move_set: type[MoveSet], rules: dict) -> BasicRPSGame:
    user = UserPlayer(move_set)
    computer = RandomComputerPlayer(move_set)
    game = BasicRPSGame(user, computer, rules)
    return game



if __name__ == "__main__":
    main()
