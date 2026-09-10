from app.game.stone import Stone


class Rules:
    DIRECTIONS = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
    ]

    @staticmethod
    def get_group(board, row, col):
        stone = board.get(row, col)

        if stone is None:
            return set()

        group = set()
        stack = [(row, col)]

        while stack:
            current = stack.pop()

            if current in group:
                continue

            current_row, current_col = current
            current_stone = board.get(current_row, current_col)

            if current_stone is None:
                continue

            if current_stone.color != stone.color:
                continue

            group.add(current)

            for neighbor in board.get_neighbors(
                current_row,
                current_col
            ):
                if neighbor not in group:
                    stack.append(neighbor)

        return group

    @staticmethod
    def get_liberties(board, group):
        liberties = set()

        for row, col in group:
            for neighbor in board.get_neighbors(row, col):
                neighbor_row, neighbor_col = neighbor

                if board.get(neighbor_row, neighbor_col) is None:
                    liberties.add(neighbor)

        return liberties

    @staticmethod
    def get_group_liberties(board, row, col):
        group = Rules.get_group(board, row, col)
        liberties = Rules.get_liberties(board, group)

        return group, liberties

    @staticmethod
    def capture_group(board, group):
        for row, col in group:
            board.remove_stone(row, col)

    @staticmethod
    def get_captured_groups(board, row, col):
        stone = board.get(row, col)

        if stone is None:
            return []

        captured_groups = []

        for neighbor_row, neighbor_col in board.get_neighbors(
            row,
            col
        ):
            neighbor = board.get(neighbor_row, neighbor_col)

            if neighbor is None:
                continue

            if neighbor.color == stone.color:
                continue

            group = Rules.get_group(
                board,
                neighbor_row,
                neighbor_col
            )

            liberties = Rules.get_liberties(board, group)

            if not liberties:
                captured_groups.append(group)

        return captured_groups

    @staticmethod
    def is_valid_move(
        board,
        row,
        col,
        stone,
        previous_board_state=None
    ):
        if not board.is_on_board(row, col):
            return False

        if board.get(row, col) is not None:
            return False

        # Save the original board so we can undo the simulation.
        original_board = [
            row_data.copy()
            for row_data in board.grid
        ]

        # Temporarily place the stone.
        test_stone = Stone(stone.color)
        board.place_stone(row, col, test_stone)

        # Find opponent groups that would be captured.
        captured_groups = Rules.get_captured_groups(
            board,
            row,
            col
        )

        # Remove captured groups temporarily.
        for group in captured_groups:
            Rules.capture_group(board, group)

        # Check for suicide.
        group, liberties = Rules.get_group_liberties(
            board,
            row,
            col
        )

        if not liberties:
            board.grid = original_board
            return False

        # Create the board state after the simulated move.
        new_board_state = tuple(
            tuple(
                stone.color if stone else None
                for stone in board_row
            )
            for board_row in board.grid
        )

        # Restore the original board.
        board.grid = original_board

        # Ko rule:
        # The new board cannot recreate the previous board position.
        if (
            previous_board_state is not None
            and new_board_state == previous_board_state
        ):
            return False

        return True