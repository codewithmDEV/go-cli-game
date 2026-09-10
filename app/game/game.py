from app.game.board import Board
from app.game.player import Player
from app.game.stone import Stone
from app.game.rules import Rules


class Game:
    def __init__(self, board_size=9):
        self.board = Board(board_size)
        self.players = []
        self.current_player_index = 0
        self.passes = 0
        self.game_over = False

        self.captured_stones = {
            "black": 0,
            "white": 0
        }

    def add_player(self, name, color):
        if len(self.players) >= 2:
            raise ValueError("Cannot add more than two players.")

        self.players.append(Player(name, color))

    def get_current_player(self):
        if len(self.players) != 2:
            raise ValueError("The game requires exactly two players.")

        return self.players[self.current_player_index]

    def switch_turn(self):
        self.current_player_index = (
            self.current_player_index + 1
        ) % len(self.players)

    def play_move(self, row, col):
        if self.game_over:
            raise ValueError("The game is already over.")

        if len(self.players) != 2:
            raise ValueError("The game requires exactly two players.")

        current_player = self.get_current_player()
        stone = Stone(current_player.color)

        if not Rules.is_valid_move(
            self.board,
            row,
            col,
            stone
        ):
            raise ValueError("Invalid move.")

        self.board.place_stone(row, col, stone)

        captured_groups = Rules.get_captured_groups(
            self.board,
            row,
            col
        )

        for group in captured_groups:
            self.captured_stones[current_player.color] += len(group)
            Rules.capture_group(self.board, group)

        self.passes = 0
        self.switch_turn()

    def pass_turn(self):
        if self.game_over:
            raise ValueError("The game is already over.")

        if len(self.players) != 2:
            raise ValueError("The game requires exactly two players.")

        self.passes += 1

        if self.passes >= 2:
            self.game_over = True
            return True

        self.switch_turn()
        return False

    def is_game_over(self):
        return self.game_over