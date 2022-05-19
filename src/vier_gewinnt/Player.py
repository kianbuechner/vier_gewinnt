import random


class Player:
    def __init__(self, num):
        self.num = num

    def player_move(self, game_mode):
        # Wenn der Spielmodus gegen den Computer ausgewählt wurde, wird der Spielstein in eine zufällige Spalte gesetzt.
        if game_mode == 2 and self.num == 2:
            column = random.randint(1, 5)

        else:
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




