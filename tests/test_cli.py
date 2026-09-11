import pytest
from app.ui.validators import parse_input
from app.ui.display import render_board

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
        # 'I' fails regex format because Go skips 'I'
        with pytest.raises(ValueError, match="Invalid format"):
            parse_input("I5", board_size=9)

        # 'K' passes format regex but is out of bounds on a 9x9 board (columns are A-J)
        with pytest.raises(ValueError, match="out of bounds"):
            parse_input("K5", board_size=9)
            
        with pytest.raises(ValueError, match="between 1 and 9"):
            parse_input("A10", board_size=9)

class TestDisplay:
    def test_render_board(self):
        grid = [["." for _ in range(9)] for _ in range(9)]
        output = render_board(grid)
        assert "A B C D E F G H J" in output
        assert "Prisoners" in output