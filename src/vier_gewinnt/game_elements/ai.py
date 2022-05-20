from player import Player
import random


class Ai(Player):
    def __init__(self, num):
        super().__init__(num)

    def player_move(self, game_mode):
        return random.randint(0, 4)
