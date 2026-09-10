import pytest

from app.game.board import Board
from app.game.stone import Stone

def test_board_starts_empty():
    board = Board(9)
    for row in range(9):
        for col in range(9):
            assert board.get(row, col) is None


def test_board_places_stone():
    board = Board(9)
    stone = Stone("black")
    board.place_stone(3, 3, stone)
    assert board.get(3, 3) == stone


def test_cannot_place_stone_on_occupied_position():
    board = Board(9)
    stone1 = Stone("black")
    stone2 = Stone("white")
    board.place_stone(3, 3, stone1)
    with pytest.raises(ValueError):
        board.place_stone(3, 3, stone2)


def test_cannot_place_stone_off_board():
    board = Board(9)
    stone = Stone("black")
    with pytest.raises(ValueError):
        board.place_stone(-1, 0, stone)
    with pytest.raises(ValueError):
        board.place_stone(0, -1, stone)
    with pytest.raises(ValueError):
        board.place_stone(9, 0, stone)
    with pytest.raises(ValueError):
        board.place_stone(0, 9, stone)


def test_get_neighbours():
    board = Board(9)
    neighbors = board.get_neighbors(3, 3)

    assert set(neighbors) == {(2, 3), (4, 3), (3, 2), (3, 4)}


def test_corner_has_two_neighbours():
    board = Board(9)
    neighbors = board.get_neighbors(0, 0)

    assert set(neighbors) == {(1, 0), (0, 1)}