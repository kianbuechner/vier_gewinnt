import Player as P
import GameTable as Gt

# das Spielfeld ist ein 2 dimensionales Array.
game_table = Gt.GameTable(5)
game_piece = ["", "x", "o"]
player_one = P.Player(1)
player_two = P.Player(2)


def play_game():
    # Zu Beginn des Spiels kann der Spielmodus ausgewählt werden.
    game_mode = int(input(
        "Wähle einen Spielmodus 1 oder 2:\n 1 für PVP - Player Versus Player\n 2 für PVC - Player Versus Computer\n"))
    if game_mode == 1:
        print("Du hast den PVP-Modus gewählt. Viel Spaß euch beiden!")
    elif game_mode == 2:
        print("Du hast den PVC-Modus gewählt. Viel Spaß gegen den Computer!")

    # Die Variable is_game_over enthält ein Boolean der angibt, ob das Spiel vorbei ist.
    is_game_over = False
    game_table.print_game_table()

    # Solange is_game_over == False ist, wird die while-Schleife und somit das Spiel ausgeführt.
    while not is_game_over:
        is_game_over = game_table.find_and_exchange_lowest(player_one.player_move(game_mode), player_one, game_mode)
        if is_game_over:
            break
        is_game_over = game_table.find_and_exchange_lowest(player_two.player_move(game_mode), player_two, game_mode)


if __name__ == '__main__':
    play_game()
