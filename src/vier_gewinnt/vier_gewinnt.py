import random
import module as m

# das Spielfeld ist ein 2 dimensionales Array.
game_table = m.GameTable


# Funktion die immer das aktuelle Spielfeld visuell ausgibt.
def print_game_table():
    table_string = "|1|2|3|4|5|\n-----------\n"
    for i in game_table:
        for j in i:
            if j == 1:
                table_string += "|" + game_pieces[1]
            elif j == 2:
                table_string += "|" + game_pieces[2]
            else:
                table_string += "| "
        table_string += "|\n"
    print(table_string)


def start_game():
    # Zu Beginn des Spiels kann der Spielmodus ausgewählt werden.
    game_mode = int(input("Wähle einen Spielmodus 1 oder 2:\n 1 für PVP - Player Versus Player\n 2 für PVC - Player Versus Computer\n"))
    if game_mode == 1:
        print("Du hast den PVP-Modus gewählt. Viel Spaß euch beiden!")
    elif game_mode == 2:
        print("Du hast den PVC-Modus gewählt. Viel Spaß gegen den Computer!")
    
    # Die Variable is_game_over enthält ein Boolean der angibt ob das Spiel vorbei ist.
    is_game_over = False
    print_game_table()
    
    # Solange is_game_over == False ist, wird die while-Schleife ausgeführt. 
    while not is_game_over:
        is_game_over = player_move(1, game_mode)
        if is_game_over:
            break
        is_game_over = player_move(2, game_mode)


# Gibt den Boolean, der angibt ob das Spiel vorbei ist, von der Funktion find_and_exchange_lowest() mit zurück.
def player_move(player, game_mode):
    
    # Wenn der Spielmodus gegen den Computer ausgewählt wurde, wird der Spielstein in eine zufällige Spalte gesetzt.
    if game_mode == 2 and player == 2:
        column = random.randint(1, 5)
        
    else:
        is_valid_input = False
        while not is_valid_input:

            # Mit einem try-catch wird der Fall, dass der Benutzer keinen Input eingibt, abgedeckt.
            try: 
                column = int(input("Gib die Nummer 1-5 der Spalte an, in die du deinen Spielstein setzen möchtest: "))
                if column in range(1, 6):
                    is_valid_input = True
                else:
                    print("Deine Eingabe ist kein Zahl zwischen 1 und 5, versuche es nochmal!")
            except ValueError:
                print("Deine Eingabe ist ungültig, versuche es nochmal!")
            
    return find_and_exchange_lowest(column - 1, player, game_mode)


# Gibt einen Boolean zurück der angibt ob das Spiel vorbei ist.
def find_and_exchange_lowest(column, player, game_mode):
    
    # In der for-Schleife wird durch die fokussierte Spalte, die der Funktion durch column mitgegeben wurde, durch iteriert.
    # Dies geschieht Rückwärts von 4 bis 0, da die Spalte angefangen von unten nach freien Plätzen überprüft werden soll.
    for i in range(4, -1, -1):
        
        # Der Wert des fokussierten Elements wird hier schon in einer Variable gespeichert, da er später eventuell überschrieben wird.
        element = game_table[i][column]
        
        # Wenn das fokussierte Feld leer ist:
        if element == 0:
            game_table[i][column] = player
            print_game_table()
            
            # Eine Liste mit Booleans zu jeder Reihe des Tables, die angibts, ob diese keine 0 enthält, um zu prüfen ob das Spielfeld voll ist.
            is_game_table_full = [False if 0 in i else True for i in game_table]        
            
            # Wenn das Spiel gewonnen wurde:
            if is_game_won(i, column):
                if game_mode == 2 and player == 2:
                    print("Der Computer hat gewonnen!")
                else:
                    print("Spieler ", game_pieces[player], " hat gewonnen! Herzlichen Glückwunsch!")
                return True

            # Wenn das gesamte Spielfeld voll ist:
            elif [False if False in is_game_table_full else True] == True:
                print("Das Spiel ist unentschieden ausgegangen!")
                return True
            return False
        
        # Wenn das fokussierte Feld ganz oben und nicht leer ist, also die Spalte schon voll ist:
        elif i == 0 and element != 0:
            if not (game_mode == 2 and player == 2):
                print("Spalte ist schon voll! Versuchs nochmal in einer freien Spalte.")
            player_move(player, game_mode)


# Überprüft ob das Spiel von einem Spieler gewonnen wurde, also ob 4 gleiche Spielsteine horizontal, vertikal oder diagonal nebeneinander sind.
# Ausführliche Erklärung in der beigelegten Dokumentation.
def is_game_won(row, column):
    player = game_table[row][column]
    is_game_won = None
                
    # Horizontal
    row_numbers = [j for j, x in enumerate(game_table[row]) if x == player]
    if len(row_numbers) > 3:
        if row_numbers == list(range(min(row_numbers), max(row_numbers) + 1)):
            return True
        else:
            is_game_won = False
    else:
        is_game_won = False
    
    # Vertikal
    game_table_column = []
    for i in game_table.game_table:
        game_table_column.append(i[column])
    column_numbers = [j for j, x in enumerate(game_table_column) if x == player]
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
            game_table_diagonal_bot.append(game_table[counter][a + start_field_column])
            counter -= 1
        diagonal_numbers = [j for j, x in enumerate(game_table_diagonal_bot) if x == player]
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
            game_table_diagonal_bot.append(game_table[counter][a])
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
            game_table_diagonal_top.append(game_table[a][start_field_column + counter])
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
            game_table_diagonal_top.append(game_table[a + start_field_row][counter])
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


if __name__ == '__main__':
    start_game()
