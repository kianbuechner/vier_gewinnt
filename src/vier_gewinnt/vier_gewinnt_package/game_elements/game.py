import yaml

from vier_gewinnt_package.game_elements.game_table import GameTable
from vier_gewinnt_package.game_elements.player.type.ai import Ai
from vier_gewinnt_package.game_elements.player.type.human import Human


def print_leaderboard():
    with open(r"records.yaml") as file:
        records = yaml.full_load(file)

    # Die Datei wird zum ausgeben auf dem Leaderboard, nach den Siegen gegen einen anderen menschlichen Spieler
    # sortiert.
    records = dict(sorted(records.items(), key=lambda x: x[1], reverse=True))

    player = "Spieler".ljust(10)
    vs_human = "vs. Mensch".ljust(10)
    vs_ai = "vs. Computer".ljust(10)

    string = f"\nBestenliste:\n{player} | {vs_human} | {vs_ai}\n-------------------------------------- \n"

    for key in list(records.keys()):
        player = key.ljust(10)
        value_human = str(records[key][0]).ljust(10)
        value_ai = str(records[key][1]).ljust(10)
        string += f"{player} | {value_human} | {value_ai}\n"

    print(string)


class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        self.game_table = GameTable(5)
        self.game_piece = ["", "x", "o"]

    def play_game(self):
        print_leaderboard()
        # Zu Beginn des Spiels kann der Spielmodus ausgewählt werden.
        game_mode = int(input(
            "Wähle einen Spielmodus 1 oder 2:\n 1 für PVP - Player Versus Player\n 2 für PVC - Player Versus Computer\n"
        ))
        if game_mode == 1:
            print("Du hast den PVP-Modus gewählt. Viel Spaß euch beiden!")
            self.player_one = Human(1)
            self.player_two = Human(2)
        elif game_mode == 2:
            print("Du hast den PVC-Modus gewählt. Viel Spaß gegen den Computer!")
            self.player_one = Human(1)
            self.player_two = Ai()

        # Die Variable is_game_over enthält ein Boolean der angibt, ob das Spiel vorbei ist.
        is_game_over = False
        self.game_table.print_game_table()

        # Solange is_game_over == False ist, wird die while-Schleife und somit das Spiel ausgeführt.
        while not is_game_over:
            is_game_over = self.game_table.find_and_exchange_lowest(self.player_one.player_move(),
                                                                    self.player_one, game_mode)
            if is_game_over:
                break
            is_game_over = self.game_table.find_and_exchange_lowest(self.player_two.player_move(),
                                                                    self.player_two, game_mode)
