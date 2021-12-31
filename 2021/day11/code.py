from itertools import count


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
        self.steps = 100

    def part1(self) -> int:
        """Returns number of total flashes after given steps."""
        total_flashes = 0
        grid = self.copy(self.grid)
        for step in range(self.steps):
            num_flashes, grid = self.count_flashes(grid)
            total_flashes += num_flashes
        return total_flashes

    def count_flashes(self, grid: list) -> tuple:
        """
        Returns tuple containing number of flashes and updated grid after 1 step.

        Args:
            grid (list): Current grid state.

        Returns:
            tuple: Tuple containing number of flashes and updated grid after 1 step.
        """

        # Increment all energy levels.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1

        # Count flashes.
        grid, num_flashes = self.simulate_flashes(self.copy(grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    grid[i][j] = 0
        return num_flashes, grid

    def simulate_flashes(self, grid: list) -> tuple:
        """
        Loops over grid to count and simulate flashes.

        Args:
            grid (list): Current state of grid after increment.

        Returns:
            tuple: Tuple containing updated grid and total flashes.
        """
        flashed = []
        while True:
            has_flashed = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] > 9 and [i, j] not in flashed:
                        has_flashed = True
                        flashed.append([i, j])
                        for i2 in range(max(0, i - 1), min(len(grid), i + 2)):
                            for j2 in range(max(0, j - 1), min(len(grid), j + 2)):
                                grid[i2][j2] += 1
            if not has_flashed:
                return grid, len(flashed)

    def copy(self, x):
        """Returns a deep copy of x."""
        if isinstance(x, dict):
            return {self.copy(key): self.copy(val) for key, val in x.items()}
        elif isinstance(x, list):
            return [self.copy(y) for y in x]
        else:
            return x

    def part2(self) -> int:
        """Returns first step all octopuses flash simultaneously."""
        grid = self.copy(self.grid)
        for step in count():
            num_flashes, grid = self.count_flashes(grid)
            if num_flashes == len(grid) * len(grid[0]):
                return step + 1


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
