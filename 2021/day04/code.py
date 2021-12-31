class Solution:
    def load_data(self, path: str) -> tuple:
        """
        Loads data from given file path.

        Args:
            path (str): path to data.

        Returns:
            tuple: Tuple containing number calls as a list of integers, and boards as a list of dicts.
        """

        # Read in file.
        data = open(path, "r").read().split("\n")

        # Parse number calls.
        calls = [int(x) for x in data[0].split(",")]

        # Parse boards.
        boards, board, board_index = {}, [], 1
        for row in data[2:]:

            # Start new board.
            if row == "":
                boards[board_index] = {"board": board, "score": 0}
                board_index += 1
                board = []

            # Continue current board.
            else:
                board.append({int(x): False for x in row.split(" ") if x != ""})

        return calls, boards

    def part1(self, calls: list, boards: list) -> tuple:
        """
        Returns winning bingo board and score with given list of calls and boards.

        Args:
            calls (list): Bingo number calls in sequence as list of integers.
            boards (list): Bingo boards as list of dicts.

        Returns:
            tuple: Tuple containing index of winning bingo board and score.
        """

        # Iterate over number calls.
        for num in calls:

            # Iterate over boards.
            best_board, best_score = 0, 0
            for board_index in boards:

                # Check if board is bingo, and if so, if it's highest scoring.
                board = boards[board_index]["board"]
                board, score = self.update_and_score_board(board, num)
                boards[board_index]["board"] = board

                if score > best_score:
                    best_score = score
                    best_board = board_index

            # If there was a bingo, return highest scoring board.
            if best_score:
                return best_board, best_score

        return 0, 0

    def update_and_score_board(self, board: list, num: int) -> tuple:
        """
        Updates and scores given bingo board with most recently called bingo number.

        Args:
            board (list): Bingo boards as list of dicts.
            num (int): Most recently called bingo number to check.

        Returns:
            tuple: Tuple containing updated bingo board and score.
        """

        # Update board by marking instances of num.
        for i, row in enumerate(board):
            for bingo_num in row:
                if bingo_num == num:
                    board[i][bingo_num] = True

        # Check for bingo.
        is_bingo = False

        # Check if there is a row bingo.
        for row in board:
            if all([marked for num, marked in row.items()]):
                is_bingo = True

        # Check if there is a column bingo.
        for col in range(len(board)):
            if all([list(row.values())[col] for row in board]):
                is_bingo = True

        # Compute and return score if there is a bingo.
        if is_bingo:
            sum_unmarked = sum(
                [
                    sum([num for num, marked in row.items() if not marked])
                    for row in board
                ]
            )
            return board, sum_unmarked * num

        # Return 0 as score if no bingo.
        return board, 0

    def part2(self, calls: list, boards: list) -> tuple:
        """
        Returns last winning bingo board and score with given list of calls and boards.

        Args:
            calls (list): Bingo number calls in sequence as list of integers.
            boards (list): Bingo boards as list of dicts.

        Returns:
            tuple: Tuple containing index of last winning bingo board and score.
        """

        # Iterate over number calls.
        for num in calls:

            # Iterate over boards.
            for board_index in boards:
                board = boards[board_index]["board"]

                # Check if board is bingo, and if so, track its score.
                board, score = self.update_and_score_board(board, num)
                boards[board_index]["board"] = board
                boards[board_index]["score"] = score

            # Find lowest scoring board.
            lowest_score, lowest_board_index = -1, -1
            new_boards = {k: v for k, v in boards.items()}
            for board_index in boards:
                board_score = boards[board_index]["score"]
                if lowest_score == -1 or board_score < lowest_score:
                    lowest_score = board_score
                    lowest_board_index = board_index

                # If board is bingo, remove from list of boards
                if board_score > 0:
                    new_boards.pop(board_index)
                boards = new_boards

            # If no remaining boards left (all boards are bingo), return lowest scoring board.
            if not boards:
                return lowest_board_index, lowest_score

        return 0, 0


if __name__ == "__main__":
    solution = Solution()
    bingo_calls, bingo_boards = solution.load_data("input.txt")

    pt1_board, pt1_score = solution.part1(calls=bingo_calls, boards=bingo_boards)
    print(f"Part 1: board {pt1_board}, score {pt1_score}")

    pt2_board, pt2_score = solution.part2(calls=bingo_calls, boards=bingo_boards)
    print(f"Part 2: board {pt2_board}, score {pt2_score}")
