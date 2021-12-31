from math import prod


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [[int(y) for y in list(x)] for x in data]
        self.grid = data

    def part1(self) -> int:
        """Returns sum of risk levels of all low points on heightmap."""
        total_sum = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                total_sum += self.calculate_risk(row, col)
        return total_sum

    def calculate_risk(self, row: int, col: int) -> int:
        """
        Calculates risk level given coordinates of grid. Returns 0 if not a low point.

        Args:
            row (int): Index of row in grid.
            col (int): Index of col in grid.

        Returns:
            int: Risk level of given coordinates. Returns 0 if not low point.
        """

        # Check if point is low point.
        is_low = True
        is_low = (
            self.grid[row][col - 1] > self.grid[row][col] and is_low
            if col - 1 >= 0
            else is_low
        )
        is_low = (
            self.grid[row][col + 1] > self.grid[row][col] and is_low
            if col + 1 < len(self.grid[0])
            else is_low
        )
        is_low = (
            self.grid[row - 1][col] > self.grid[row][col] and is_low
            if row - 1 >= 0
            else is_low
        )
        is_low = (
            self.grid[row + 1][col] > self.grid[row][col] and is_low
            if row + 1 < len(self.grid)
            else is_low
        )

        # Return risk level.
        risk = 1 + self.grid[row][col] if is_low else 0
        return risk

    def calculate_basin_size(
        self, row: int, col: int, current_basin: list, current_size: int
    ) -> tuple:
        """
        Calculates basin size given coordinates of low point.

        Args:
            row (int): Index of row in grid.
            col (int): Index of col in grid.
            current_basin (list): Running list of coordinates in basin.
            current_size (int): Running size of basin.

        Returns:
            tuple: Tuple containing final basin size and coordinates.
        """
        if (
            row - 1 >= 0
            and self.grid[row - 1][col] != 9
            and [row - 1, col] not in current_basin
        ):
            current_size, current_basin = self.calculate_basin_size(
                row - 1, col, current_basin + [[row - 1, col]], current_size + 1
            )
        if (
            row + 1 < len(self.grid)
            and self.grid[row + 1][col] != 9
            and [row + 1, col] not in current_basin
        ):
            current_size, current_basin = self.calculate_basin_size(
                row + 1, col, current_basin + [[row + 1, col]], current_size + 1
            )
        if (
            col - 1 >= 0
            and self.grid[row][col - 1] != 9
            and [row, col - 1] not in current_basin
        ):
            current_size, current_basin = self.calculate_basin_size(
                row, col - 1, current_basin + [[row, col - 1]], current_size + 1
            )
        if (
            col + 1 < len(self.grid[0])
            and self.grid[row][col + 1] != 9
            and [row, col + 1] not in current_basin
        ):
            current_size, current_basin = self.calculate_basin_size(
                row, col + 1, current_basin + [[row, col + 1]], current_size + 1
            )
        return current_size, current_basin

    def part2(self) -> int:
        """Returns product of 3 largest basins in grid."""

        # Compile all basins.
        basins = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.calculate_risk(row, col):
                    basin_size, _ = self.calculate_basin_size(row, col, [[row, col]], 1)
                    basins.append(basin_size)

        # Return product of 3 largest basins.
        basins = sorted(basins)[-3:]
        return prod(basins)


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
