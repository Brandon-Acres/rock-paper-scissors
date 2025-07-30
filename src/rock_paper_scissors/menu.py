# rock_paper_scissors.menu

from enum import Enum

class MenuOption(Enum):
    PLAY_BASIC_RPS = "1"
    QUIT = "q"

def show_main_menu() -> MenuOption:
    print("\nWelcome to Rock Paper Scissors!")
    print("Select an option below by entering the value in (parentheses)")
    print(f"({MenuOption.PLAY_BASIC_RPS.value}) Play Basic Rock Paper Scissors against a random Computer")
    print(f"({MenuOption.QUIT.value}) Quit game")

    while True:
        try:
            choice = input("Enter your choice: ")
            return MenuOption(choice)
        except (ValueError, KeyError):
            print("Invalid selection. Please try again.")
