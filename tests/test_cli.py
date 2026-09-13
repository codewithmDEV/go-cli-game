import pytest
from app.ui.validators import parse_input
from app.ui.display import render_board, STONE_BLACK, STONE_WHITE

class MockStone:
    def __init__(self, color: str):
        self.color = color

class TestInputValidator:
    def test_valid_commands(self):
        assert parse_input("pass") == ("pass", None)
        assert parse_input("RESIGN") == ("resign", None)

    def test_valid_coordinates(self):
        cmd, coords = parse_input("D4", board_size=9)
        assert cmd == "play"
        assert coords == (5, 3)

    def test_skips_letter_i(self):
        cmd, coords = parse_input("J1", board_size=9)
        assert cmd == "play"

    def test_invalid_inputs(self):
        with pytest.raises(ValueError, match="Invalid format"):
            parse_input("I5", board_size=9)

        with pytest.raises(ValueError, match="out of bounds"):
            parse_input("K5", board_size=9)
            
        with pytest.raises(ValueError, match="between 1 and 9"):
            parse_input("A10", board_size=9)

class TestDisplay:
    def test_render_board_with_stone_objects(self):
        # 9x9 board initialized with None for empty intersections
        grid = [[None for _ in range(9)] for _ in range(9)]
        
        # Place Stone objects matching core engine structure
        grid[0][0] = MockStone("black")
        grid[0][1] = MockStone("white")
        
        output = render_board(grid, captured_black=1, captured_white=2)
        
        assert "A B C D E F G H J" in output
        assert STONE_BLACK in output
        assert STONE_WHITE in output
        assert "Prisoners -> Black: 1 | White: 2" in output