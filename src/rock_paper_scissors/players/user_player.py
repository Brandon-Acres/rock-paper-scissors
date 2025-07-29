# rock_paper_scissors.players.user_player
from rock_paper_scissors.players.iplayer import IPlayer
from rock_paper_scissors.moves.move_set import MoveSet

# inherits from IPlayer
class UserPlayer(IPlayer):
    def __init__(self, move_set: type[MoveSet]):
        self.move_set = move_set

    def make_move(self) -> MoveSet:
        prompt = f"Enter move ({', '.join(self.move_set.list_moves())}): "
        user_input = input(prompt)
        try:
            return self.move_set.from_string(user_input)
        except ValueError as e:
            print(e)
            return self.make_move()

   