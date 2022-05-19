import GamePiece as Gp


class GameTable:
    def __init__(self, scale):
        self.game_table = []
        for row in range(0, scale):
            row_list = []
            for column in range(0, scale):
                row_list.append(Gp.GamePiece(row, column))
            self.game_table.append(row_list)

    # Funktion die immer das aktuelle Spielfeld visuell ausgibt.
    def print_game_table(self):
        table_string = "|1|2|3|4|5|\n-----------\n"
        for row in self.game_table:
            for column in row:
                if column.value == 1:
                    table_string += "|" + "x"
                elif column.value == 2:
                    table_string += "|" + "o"
                else:
                    table_string += "| "
            table_string += "|\n"
        print(table_string)

    # Überprüft ob das Spiel von einem Spieler gewonnen wurde, also ob 4 gleiche Spielsteine horizontal,
    # vertikal oder diagonal nebeneinander sind. Ausführliche Erklärung in der beigelegten Dokumentation.
    def is_game_won(self, row, column):
        player = self.game_table[row][column]
        is_game_won = None

        # Horizontal
        row_numbers = [j for j, x in enumerate(self.game_table[row]) if x.value == player]
        if len(row_numbers) > 3:
            if row_numbers == list(range(min(row_numbers), max(row_numbers) + 1)):
                return True
            else:
                is_game_won = False
        else:
            is_game_won = False

        # Vertikal
        game_table_column = []
        for i in self.game_table:
            game_table_column.append(i[column])
        column_numbers = [j for j, x in enumerate(game_table_column) if x.value == player]
        if len(column_numbers) > 3:
            if column_numbers == list(range(min(column_numbers), max(column_numbers) + 1)):
                return True
            else:
                is_game_won = False
        else:
            is_game_won = False

        # Diagonal
        # links-unten nach rechts-oben
        game_table_diagonal_bot = []
        if row + column >= 5:
            start_field_row = 4
            start_field_column = row + column - 4
            counter = start_field_row
            for a in range(0, 5 - start_field_column):
                game_table_diagonal_bot.append(self.game_table[counter][a + start_field_column])
                counter -= 1
            diagonal_numbers = [j for j, x in enumerate(game_table_diagonal_bot) if x.value == player]
            if len(diagonal_numbers) > 3:
                if diagonal_numbers == list(range(min(diagonal_numbers), max(diagonal_numbers) + 1)):
                    is_game_won = True
                else:
                    is_game_won = False
            else:
                is_game_won = False
        else:
            start_field_row = row + column
            start_field_column = 0
            counter = start_field_row
            for a in range(0, start_field_row + 1):
                game_table_diagonal_bot.append(self.game_table[counter][a])
                counter -= 1
            diagonal_numbers = [j for j, x in enumerate(game_table_diagonal_bot) if x == player]
            if len(diagonal_numbers) > 3:
                if diagonal_numbers == list(range(min(diagonal_numbers), max(diagonal_numbers) + 1)):
                    is_game_won = True
                else:
                    is_game_won = False
            else:
                is_game_won = False

        # links-oben nach rechts-unten
        game_table_diagonal_top = []
        if row < column:
            start_field_row = 0
            start_field_column = column - row
            counter = 0
            for a in range(0, 5 - start_field_column):
                game_table_diagonal_top.append(self.game_table[a][start_field_column + counter])
                counter += 1
            diagonal_numbers = [j for j, x in enumerate(game_table_diagonal_top) if x == player]
            if len(diagonal_numbers) > 3:
                if diagonal_numbers == list(range(min(diagonal_numbers), max(diagonal_numbers) + 1)):
                    return True
                else:
                    is_game_won = False
            else:
                is_game_won = False
        else:
            start_field_row = row - column
            start_field_column = 0
            counter = 0
            for a in range(0, 5 - start_field_row):
                game_table_diagonal_top.append(self.game_table[a + start_field_row][counter])
                counter += 1
            diagonal_numbers = [j for j, x in enumerate(game_table_diagonal_top) if x == player]
            if len(diagonal_numbers) > 3:
                if diagonal_numbers == list(range(min(diagonal_numbers), max(diagonal_numbers) + 1)):
                    return True
                else:
                    is_game_won = False
            else:
                is_game_won = False

        return is_game_won

    def is_game_table_full(self):
        for row in self.game_table:
            for game_piece in row:
                if game_piece.value == 0:
                    return False
        return True

    # Gibt einen Boolean zurück der angibt ob das Spiel vorbei ist.
    def find_and_exchange_lowest(self, column, player, game_mode):
        # In der for-Schleife wird durch die fokussierte Spalte, die der Funktion durch column mitgegeben wurde,
        # durch iteriert. Dies geschieht Rückwärts von 4 bis 0, da die Spalte angefangen von unten nach freien Plätzen
        # überprüft werden soll.
        for row in range(4, -1, -1):

            # Der Wert des fokussierten Elements wird hier schon in einer Variable gespeichert, da er später eventuell
            # überschrieben wird.
            element = self.game_table[row][column]

            # Wenn das fokussierte Feld leer ist:
            if element.value == 0:
                self.game_table[row][column].value = player.num
                self.print_game_table()

                # Wenn das Spiel gewonnen wurde:
                if self.is_game_won(row, column):
                    if game_mode == 2 and player.num == 2:
                        print("Der Computer hat gewonnen!")
                    else:
                        print("Spieler ", player.num, " hat gewonnen! Herzlichen Glückwunsch!")
                    return True

                # Wenn das gesamte Spielfeld voll ist:
                elif self.is_game_table_full():
                    print("Das Spiel ist unentschieden ausgegangen!")
                    return True
                else:
                    return False

            # Wenn das fokussierte Feld ganz oben und nicht leer ist, also die Spalte schon voll ist:
            elif row == 0 and element.value != 0:
                if not (game_mode == 2 and player.num == 2):
                    print("Spalte ist schon voll! Versuchs nochmal in einer freien Spalte.")
                player.player_move(game_mode)
