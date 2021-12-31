from itertools import combinations


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [int(x) for x in data]
        self.data = data
        self.volume = 150

    def part1(self) -> int:
        """
        Calculate how many ways to select containers to fill exact volume.

        Returns:
            int: Number of ways to select containers.
        """
        total = 0
        for i in range(len(self.data)):
            for combination in combinations(self.data, i + 1):
                if sum(combination) == self.volume:
                    total += 1
        return total

    def part2(self) -> int:
        """
        Calculate how many ways to select containers to fill exact volume with minimum total containers.

        Returns:
            int: Number of ways to select containers.
        """
        total, min_containers = 0, len(self.data)
        for i in range(len(self.data)):
            for combination in combinations(self.data, i + 1):
                if sum(combination) == self.volume:
                    if len(combination) == min_containers:
                        total += 1
                    elif len(combination) < min_containers:
                        total = 1
                        min_containers = len(combination)
        return total


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
