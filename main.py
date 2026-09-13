from app.game.game import Game
from app.ui.display import render_board, display_message
from app.ui.validators import parse_input


def show_game(game):
    print(
        render_board(
            game.board.grid,
            game.captured_stones["black"],
            game.captured_stones["white"],
        )
    )

    if not game.game_over:
        current_player = game.get_current_player()
        print(f"\n{current_player.name}'s turn ({current_player.color})")


def show_help():
    print(
        """
Commands:
    <coordinate>   Play a move, e.g. D4
    pass            Pass your turn
    resign          Resign from the game
    help            Show this help message
    quit            Quit the game
"""
    )


def setup_game():
    print("=== Go CLI Game ===\n")

    while True:
        try:
            board_size_input = input("Enter board size (default 9): ").strip()

            if not board_size_input:
                board_size = 9
            else:
                board_size = int(board_size_input)

            if board_size < 1:
                raise ValueError

            break

        except ValueError:
            display_message("Board size must be a positive number.", is_error=True)

    black_name = input("Enter Black player's name: ").strip()
    while not black_name:
        display_message("Player name cannot be empty.", is_error=True)
        black_name = input("Enter Black player's name: ").strip()

    white_name = input("Enter White player's name: ").strip()
    while not white_name:
        display_message("Player name cannot be empty.", is_error=True)
        white_name = input("Enter White player's name: ").strip()

    game = Game(board_size=board_size)

    game.add_player(black_name, "black")
    game.add_player(white_name, "white")

    return game


def main():
    game = setup_game()

    display_message("Game started!")
    show_help()
    show_game(game)

    while not game.game_over:
        try:
            raw_input = input("\nEnter command: ")
            command, coordinates = parse_input(
                raw_input,
                board_size=game.board.size,
            )

            if command == "help":
                show_help()

            elif command == "quit":
                display_message("Game ended.")
                return

            elif command == "resign":
                current_player = game.get_current_player()
                display_message(
                    f"{current_player.name} resigned. "
                    "The other player wins."
                )
                return

            elif command == "pass":
                game_ended = game.pass_turn()

                if game_ended:
                    show_game(game)
                    display_message("Both players passed. Game over.")
                    return

                display_message("Player passed.")
                show_game(game)

            elif command == "play":
                row, col = coordinates
                game.play_move(row, col)
                show_game(game)

        except ValueError as error:
            display_message(str(error), is_error=True)

        except KeyboardInterrupt:
            print("\n\nGame interrupted.")
            return

        except EOFError:
            print("\n\nGame ended.")
            return


if __name__ == "__main__":
    main()