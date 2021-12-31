from statistics import mean


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [[int(y) for y in x.split(",")] for x in data][0]
        self.positions = data

    def part1(self) -> int:
        """
        Minimum fuel to align all crabs.

        Returns:
            int: Minimum fuel amount.
        """
        min_fuel = 0
        for position in self.positions:
            fuel = sum([abs(x - position) for x in self.positions])
            min_fuel = fuel if not min_fuel or fuel < min_fuel else min_fuel
        return min_fuel

    def part2(self) -> None:
        """
        Minimum fuel to align all crabs.

        Returns:
            int: Minimum fuel amount.
        """
        min_fuel = 0
        center = round(mean(self.positions))
        for position in range(center - 2, center + 2):
            fuel = sum(
                [sum(list(range(abs(x - position) + 1))) for x in self.positions]
            )
            min_fuel = fuel if not min_fuel or fuel < min_fuel else min_fuel
        return min_fuel


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
