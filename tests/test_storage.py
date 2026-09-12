import pytest
from app.persistence.json_storage import JSONStorage

def test_save_and_load_game(tmp_path):
    file_path = tmp_path / "game.json"
    storage = JSONStorage(str(file_path))

    game_data = {
        "board": [["X", "O"], ["O", "X"]],
        "players": ["Masuud", "Ali"],
        "current_turn": "Masuud",
        "scores": {"Masuud": 2, "Ali": 1}
    }

    storage.save_game(game_data)
    loaded = storage.load_game()

    assert loaded == game_data

def test_load_missing_file(tmp_path):
    file_path = tmp_path / "missing.json"
    storage = JSONStorage(str(file_path))
    loaded = storage.load_game()
    assert loaded == {}

def test_load_corrupted_file(tmp_path):
    file_path = tmp_path / "bad.json"
    with open(file_path, "w") as f:
        f.write("{not valid json}")

    storage = JSONStorage(str(file_path))
    loaded = storage.load_game()
    assert loaded == {}
