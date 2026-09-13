import pytest

from app.game.game import Game


class TestGame:

    def test_game_starts_with_no_players(self):
        game = Game()

        assert game.players == []
        assert game.current_player_index == 0
        assert game.passes == 0
        assert game.game_over is False

    def test_add_two_players(self):
        game = Game()

        game.add_player("Mohamed", "black")
        game.add_player("Masud", "white")

        assert len(game.players) == 2
        assert game.players[0].name == "Mohamed"
        assert game.players[0].color == "black"
        assert game.players[1].name == "Masud"
        assert game.players[1].color == "white"

    def test_cannot_add_more_than_two_players(self):
        game = Game()

        game.add_player("Player1", "black")
        game.add_player("Player2", "white")

        with pytest.raises(ValueError):
            game.add_player("Extra Player", "black")

    def test_current_player_starts_as_first_player(self):
        game = Game()

        game.add_player("Player1", "black")
        game.add_player("Player2", "white")

        current_player = game.get_current_player()

        assert current_player.name == "Player1"
        assert current_player.color == "black"

    def test_turn_switches_after_move(self):
        game = Game()

        game.add_player("Player1", "black")
        game.add_player("Player2", "white")

        game.play_move(3, 3)

        current_player = game.get_current_player()

        assert current_player.name == "Player2"
        assert current_player.color == "white"

        game.play_move(4, 4)

        current_player = game.get_current_player()

        assert current_player.name == "Player1"
        assert current_player.color == "black"

    def test_invalid_move_raises_error(self):
        game = Game()

        game.add_player("Player1", "black")
        game.add_player("Player2", "white")

        game.play_move(3, 3)

        with pytest.raises(ValueError):
            game.play_move(3, 3)

    def test_first_pass_switches_turn(self):
        game = Game()

        game.add_player("Player1", "black")
        game.add_player("Player2", "white")

        game.pass_turn()

        current_player = game.get_current_player()

        assert current_player.name == "Player2"
        assert current_player.color == "white"
        assert game.is_game_over() is False

    def test_two_consecutive_passes_end_game(self):
        game = Game()

        game.add_player("Player 1", "black")
        game.add_player("Player 2", "white")

        game.pass_turn()
        game.pass_turn()

        assert game.passes == 2
        assert game.is_game_over() is True

    def test_cannot_play_after_game_ends(self):
        game = Game()

        game.add_player("Player 1", "black")
        game.add_player("Player 2", "white")

        game.pass_turn()
        game.pass_turn()

        with pytest.raises(ValueError):
            game.play_move(3, 3)

    def test_play_move_captures_stone_and_updates_score(self):
        game = Game(board_size=5)

        game.add_player("Player1", "black")
        game.add_player("Player2", "white")

        game.play_move(0, 1)  # Black B1
        game.play_move(1, 1)  # White B2
        game.play_move(1, 0)  # Black A2
        game.play_move(4, 4)  # White E5
        game.play_move(2, 1)  # Black B3
        game.play_move(3, 4)  # White E4
        game.play_move(0, 0)  # Black A1
        game.play_move(2, 4)  # White E3
        game.play_move(1, 2)  # Black C2

        assert game.board.get(1, 1) is None
        assert game.captured_stones["black"] == 1
        assert game.captured_stones["white"] == 0