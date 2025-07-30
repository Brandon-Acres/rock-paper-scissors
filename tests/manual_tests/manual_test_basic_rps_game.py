"""Manually test functionaly of BasicRPSGame"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from rock_paper_scissors.games.basic_rps_game import BasicRPSGame
from rock_paper_scissors.players.random_computer_player import RandomComputerPlayer
from rock_paper_scissors.players.user_player import UserPlayer
from rock_paper_scissors.moves.basic_moves import BasicMove
from rock_paper_scissors.moves.move_set import MoveSet
from rock_paper_scissors.rules.basic_rules import BASIC_RULES

from typing import cast

# set up players
user_player = UserPlayer(cast(type[MoveSet], BasicMove))
computer_player = RandomComputerPlayer(cast(type[MoveSet], BasicMove))

# set up basicRPSGame
basic_game = BasicRPSGame(user_player, computer_player, BASIC_RULES)

# play 3 rounds:
basic_game.play(3)
