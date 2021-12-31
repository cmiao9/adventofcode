class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        self.data = data

    def part1(self) -> None:
        """todo"""
        return

    def part2(self) -> None:
        """todo"""
        return


if __name__ == "__main__":
    solution = Solution("test.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
