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

    def print_grid(self, grid) -> None:
        """Prints grid."""
        print()
        [print(" ".join([str(x) for x in row])) for row in grid]
        print()

    def part1(self) -> int:
        """Returns lowest risk of path from top left to bottom right of grid."""
        return

    def find_paths(self, grid: list) -> list:
        """todo"""
        paths = []
        while True:


    def part2(self) -> None:
        """todo"""
        return


if __name__ == "__main__":
    solution = Solution("test.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
