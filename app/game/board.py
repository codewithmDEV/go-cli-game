class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [
            [None for _ in range(size)]
            for _ in range(size)
        ]


    def is_on_board(self, row, col):
        return (
            0 <= row < self.size
            and 0 <= col < self.size
        )


    def get(self, row, col):
        if not self.is_on_board(row, col):
            return None
        return self.grid[row][col]

    def place_stone(self, row, col, stone):
        if not self.is_on_board(row, col):
            raise ValueError("Position is off the board.")
        if self.grid[row][col] is not None:
            raise ValueError("Position is already occupied.")
        self.grid[row][col] = stone


    def remove_stone(self, row, col):
        if self.is_on_board(row, col):
            self.grid[row][col] = None


    def get_neighbors(self, row, col):
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]
        neighbors = []

        for row_change, col_change in directions:
            neighbor_row = row + row_change
            neighbor_col = col + col_change
            if self.is_on_board(neighbor_row, neighbor_col):
                neighbors.append((neighbor_row, neighbor_col))
        return neighbors