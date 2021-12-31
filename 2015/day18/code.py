class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        board = [list(x.replace(".", "0").replace("#", "1")) for x in data]
        board = [[int(y) for y in x] for x in board]
        self.path = path
        self.board = board
        self.steps = 100

    def part1(self) -> int:
        """Calculate how many lights on after given number of steps."""

        # Loop over number of steps.
        for step in range(self.steps):

            # Iterate over board and update each element accordingly.
            neighbors_board = self.get_neighbors_board()
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] and neighbors_board[row][col] not in [2, 3]:
                        self.board[row][col] = 0
                    elif neighbors_board[row][col] == 3:
                        self.board[row][col] = 1

        # Return number of lights on.
        return sum([sum(x) for x in self.board])

    def get_neighbors_board(self) -> list:
        """Creates board of neighbors that are on."""

        # Initialize neighbors board.
        neighbors = []
        for row in range(len(self.board)):
            neighbors.append([0] * len(self.board[0]))

        # Iterate over board and count neighbors.
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):

                total = 0
                if row - 1 >= 0:
                    total = (
                        total + self.board[row - 1][col - 1] if col - 1 >= 0 else total
                    )
                    total += self.board[row - 1][col]
                    total = (
                        total + self.board[row - 1][col + 1]
                        if col + 1 < len(self.board[0])
                        else total
                    )
                if row + 1 < len(self.board):
                    total = (
                        total + self.board[row + 1][col - 1] if col - 1 >= 0 else total
                    )
                    total += self.board[row + 1][col]
                    total = (
                        total + self.board[row + 1][col + 1]
                        if col + 1 < len(self.board[0])
                        else total
                    )
                total = total + self.board[row][col - 1] if col - 1 >= 0 else total
                total = (
                    total + self.board[row][col + 1]
                    if col + 1 < len(self.board[0])
                    else total
                )
                neighbors[row][col] = total

        # Return neighbors board.
        return neighbors

    def print_board(self):
        """Prints board state to terminal."""

        print()
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                print(self.board[row][col], end="")
            print()
        print()

    def part2(self) -> int:
        """Calculate how many lights on after given number of steps first turning 4 corners on."""

        self.__init__(self.path)

        # Loop over number of steps.
        for step in range(self.steps):

            # Enforce corners always on.
            for row in [0, len(self.board) - 1]:
                for col in [0, len(self.board[0]) - 1]:
                    self.board[row][col] = 1

            # Iterate over board and update each element accordingly.
            neighbors_board = self.get_neighbors_board()
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] and neighbors_board[row][col] not in [2, 3]:
                        self.board[row][col] = 0
                    elif neighbors_board[row][col] == 3:
                        self.board[row][col] = 1

        # Return number of lights on.
        for row in [0, len(self.board) - 1]:
            for col in [0, len(self.board[0]) - 1]:
                self.board[row][col] = 1
        return sum([sum(x) for x in self.board])


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
