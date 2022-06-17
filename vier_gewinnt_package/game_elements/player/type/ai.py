import random

from vier_gewinnt_package.game_elements.player.player import Player


class Ai(Player):
    def __init__(self):
        super().__init__(2)
        self.name = "Computer"

    def player_move(self):
        return random.randint(0, 4)
