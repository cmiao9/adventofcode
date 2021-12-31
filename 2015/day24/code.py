from itertools import combinations
from math import prod


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

    def part1(self, num_groups: int = 3) -> int:
        """Calculates quantum entanglement of first group of packages in ideal configuration."""

        # Loop over possible size of passenger trunk.
        valid_combos = []
        for num_passenger_packages in range(0, 1 + int(len(self.data) / num_groups)):

            # Loop over all possible combinations of passenger packages of given size.
            for passenger_packages in combinations(self.data, num_passenger_packages):

                # Check if combination yields a valid configuration.
                if sum(passenger_packages) == sum(self.data) / num_groups:

                    # Update valid combos and enforce minimum package number.
                    if not valid_combos or len(passenger_packages) == len(
                        valid_combos[0]
                    ):
                        valid_combos.append(passenger_packages)
                    elif len(passenger_packages) < len(valid_combos[0]):
                        valid_combos = [passenger_packages]

        # Return quantum entanglement of passenger packages.
        return prod(valid_combos[0])

    def part2(self) -> int:
        """Calculates quantum entanglement of first group of packages in ideal configuration."""
        return self.part1(4)


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
