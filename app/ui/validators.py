from __future__ import annotations
import re

VALID_COMMANDS = {"pass", "resign", "help", "quit"}

def parse_input(raw_input: str, board_size: int = 9) -> tuple[str, tuple[int, int] | None]:
    cleaned = raw_input.strip().lower()
    
    if not cleaned:
        raise ValueError("Input cannot be empty.")
        
    if cleaned in VALID_COMMANDS:
        return cleaned, None

    # Go notation skips 'I' to avoid confusion with '1'
    pattern = rf"^([a-hj-z])([1-9]\d*)$"
    match = re.match(pattern, cleaned)
    
    if not match:
        raise ValueError("Invalid format. Use coordinates (e.g., 'D4') or 'pass'/'resign'.")
        
    col_str, row_str = match.groups()
    
    letters = "abcdefghjklmnopqrstuvwxyz"[:board_size]
    if col_str not in letters:
        raise ValueError(f"Column '{col_str.upper()}' is out of bounds (A-{letters[-1].upper()}).")
        
    col_idx = letters.index(col_str)
    row_num = int(row_str)
    
    if not (1 <= row_num <= board_size):
        raise ValueError(f"Row must be between 1 and {board_size}.")
        
    row_idx = board_size - row_num
    return "play", (row_idx, col_idx)