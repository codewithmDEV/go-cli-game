from __future__ import annotations

STONE_BLACK = "●"
STONE_WHITE = "◯"
EMPTY_INTERSECTION = "┼"
LETTERS = "ABCDEFGHJKLMNOPQRSTUVWXYZ"  # Skips 'I'

def render_board(board_matrix: list[list[str]], captured_black: int = 0, captured_white: int = 0) -> str:
    size = len(board_matrix)
    cols = LETTERS[:size]
    lines = []
    
    col_header = "    " + " ".join(cols)
    lines.append(col_header)
    
    for row_idx in range(size):
        row_num = size - row_idx
        row_str = f"{row_num:2d} "
        
        for col_idx in range(size):
            cell = board_matrix[row_idx][col_idx]
            if cell == "B":
                symbol = STONE_BLACK
            elif cell == "W":
                symbol = STONE_WHITE
            else:
                symbol = EMPTY_INTERSECTION
                
            row_str += f" {symbol}"
            
        row_str += f" {row_num}"
        lines.append(row_str)
        
    lines.append(col_header)
    lines.append("-" * len(col_header))
    lines.append(f" Prisoners -> Black: {captured_black} | White: {captured_white}")
    lines.append("-" * len(col_header))
    
    return "\n".join(lines)

def display_message(msg: str, is_error: bool = False) -> None:
    if is_error:
        print(f"\n[ERROR] {msg}\n")
    else:
        print(f"\n[INFO] {msg}\n")