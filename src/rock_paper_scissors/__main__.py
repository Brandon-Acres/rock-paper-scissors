# rock_paper_scissors.__main__

from rock_paper_scissors.menu import show_main_menu, MenuOption
from rock_paper_scissors.games.basic_rps_game import BasicRPSGame
from rock_paper_scissors.players.user_player import UserPlayer
from rock_paper_scissors.players.random_computer_player import RandomComputerPlayer
from rock_paper_scissors.moves.basic_moves import BasicMove
from rock_paper_scissors.moves.move_set import MoveSet
from rock_paper_scissors.rules.basic_rules import BASIC_RULES
from typing import cast

def main():
    while True:
        choice = show_main_menu()

        match choice:
            case MenuOption.PLAY_BASIC_RPS:
                user = UserPlayer(cast(type[MoveSet], BasicMove))
                computer = RandomComputerPlayer(cast(type[MoveSet], BasicMove))
                game = BasicRPSGame(user, computer, BASIC_RULES)

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


if __name__ == "__main__":
    main()
