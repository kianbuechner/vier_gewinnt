import enum



class Player(enum.Enum):
    player_one = 1
    player_two = 2


class GameTable:
    game_table = []

    def __init__(self):
        self.game_table = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def print_game_table(self):
        clear_output()
        table_string = "|1|2|3|4|5|\n-----------\n"
        for i in self.game_table:
            for j in i:
                if j == 1:
                    table_string += "|" + GamePiece("o").value
                elif j == 2:
                    table_string += "|" + GamePiece("x").value
                else:
                    table_string += "| "
            table_string += "|\n"
        print(table_string)


class GamePiece(enum.Enum):
    player_one = "x"
    player_two = "o"

