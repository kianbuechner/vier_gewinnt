from player import Player


class Human(Player):
    def __init__(self, num):
        super().__init__(num)

    def player_move(self, game_mode):
        is_valid_input = False
        while not is_valid_input:

            # Mit einem try-catch wird der Fall, dass der Benutzer keinen Input eingibt, abgedeckt.
            try:
                column = int(
                    input("Gib die Nummer 1-5 der Spalte an, in die du deinen Spielstein setzen möchtest: "))
                if column in range(1, 6):
                    is_valid_input = True
                else:
                    print("Deine Eingabe ist kein Zahl zwischen 1 und 5, versuche es nochmal!")
            except ValueError:
                print("Deine Eingabe ist ungültig, versuche es nochmal!")

        return column - 1
