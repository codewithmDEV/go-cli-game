from app.game.board import Board
from app.game.stone import Stone
from app.game.rules import Rules


def test_get_group_returns_connected_same_color_stones():
    board = Board(9)

    black = Stone("black")

    board.place_stone(3, 3, black)
    board.place_stone(3, 4, black)
    board.place_stone(4, 3, black)

    group = Rules.get_group(board, 3, 3)

    assert group == {
        (3, 3),
        (3, 4),
        (4, 3),
    }


def test_get_group_does_not_include_opponent_stones():
    board = Board(9)

    black = Stone("black")
    white = Stone("white")

    board.place_stone(3, 3, black)
    board.place_stone(3, 4, black)
    board.place_stone(4, 3, white)

    group = Rules.get_group(board, 3, 3)

    assert group == {
        (3, 3),
        (3, 4),
    }


def test_get_liberties_returns_empty_adjacent_positions():
    board = Board(9)

    black = Stone("black")
    board.place_stone(3, 3, black)

    group = Rules.get_group(board, 3, 3)
    liberties = Rules.get_liberties(board, group)

    assert liberties == {
        (2, 3),
        (4, 3),
        (3, 2),
        (3, 4),
    }


def test_connected_stones_share_liberties():
    board = Board(9)

    black = Stone("black")

    board.place_stone(3, 3, black)
    board.place_stone(3, 4, black)

    group = Rules.get_group(board, 3, 3)
    liberties = Rules.get_liberties(board, group)

    assert liberties == {
        (2, 3),
        (4, 3),
        (3, 2),
        (2, 4),
        (4, 4),
        (3, 5),
    }

def test_get_captured_groups_finds_group_with_no_liberties():
    board = Board(9)

    black = Stone("black")
    white = Stone("white")

    # White stone at (3, 3)
    board.place_stone(3, 3, white)

    # Surround the white stone on three sides
    board.place_stone(2, 3, black)
    board.place_stone(4, 3, black)
    board.place_stone(3, 2, black)

    # Black is about to place the final surrounding stone
    board.place_stone(3, 4, black)

    captured_groups = Rules.get_captured_groups(
        board,
        3,
        4
    )

    assert len(captured_groups) == 1
    assert captured_groups[0] == {(3, 3)}


def test_capture_group_removes_stones():
    board = Board(9)

    black = Stone("black")
    white = Stone("white")

    board.place_stone(3, 3, white)

    captured_group = {(3, 3)}

    Rules.capture_group(board, captured_group)

    assert board.get(3, 3) is None

def test_suicide_move_is_invalid():
    board = Board(9)

    black = Stone("black")
    white = Stone("white")

    # Surround an empty intersection with white stones.
    board.place_stone(2, 3, white)
    board.place_stone(4, 3, white)
    board.place_stone(3, 2, white)
    board.place_stone(3, 4, white)

    # Black would have zero liberties if placed at (3, 3).
    assert Rules.is_valid_move(
        board,
        3,
        3,
        black
    ) is False


def test_move_is_valid_when_it_captures():
    board = Board(9)

    black = Stone("black")
    white = Stone("white")

    # White has one remaining liberty at (3, 4).
    board.place_stone(3, 3, white)

    board.place_stone(2, 3, black)
    board.place_stone(4, 3, black)
    board.place_stone(3, 2, black)

    # Although Black's new stone would initially have no
    # liberty, it captures White and therefore is legal.
    assert Rules.is_valid_move(
        board,
        3,
        4,
        black
    ) is True


def test_ko_prevents_immediate_recreation_of_previous_board():
    board = Board(4)

    black = Stone("black")
    white = Stone("white")

    # Create a one-stone Ko position.
    board.place_stone(0, 1, black)
    board.place_stone(1, 0, black)
    board.place_stone(2, 1, black)

    board.place_stone(1, 1, white)

    board.place_stone(0, 2, white)
    board.place_stone(1, 3, white)
    board.place_stone(2, 2, white)

    # Save the position before Black captures.
    previous_board_state = (
        (None, "black", "white", None),
        ("black", "white", None, "white"),
        (None, "black", "white", None),
        (None, None, None, None),
    )

    # Black captures White at (1, 1).
    board.place_stone(1, 2, black)

    # White's immediate recapture would recreate
    # the previous board position, so Ko rejects it.
    assert Rules.is_valid_move(
        board,
        1,
        1,
        white,
        previous_board_state
    ) is False
