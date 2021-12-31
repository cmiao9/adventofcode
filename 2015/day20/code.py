from itertools import count
from math import sqrt


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        self.data = int(data[0])

    def part1(self) -> int:
        """
        Finds house with at least given number of presents.

        Args:
            Number of house with at least given number of presents.
        """

        # Loop over houses.
        for house in count(1):

            # Loop over elves.
            presents, max_elf = (1 + house) * 10, sqrt(house)
            for elf in count(2):

                # Loop from 2 to square root of house.
                if elf > max_elf:
                    break

                # Check if elf visits given house.
                if house % elf == 0:
                    presents += int(elf * 10 + house / elf * 10)
            print(house, presents, end="\r")

            # If given house satisfies minimum presents requirement, return.
            if presents >= self.data:
                return house

    def part2(self) -> None:
        """
        Finds house with at least given number of presents.

        Args:
            Number of house with at least given number of presents.
        """

        # Loop over houses.
        elves = [0] * int(self.data / 10)
        for house in count(1):

            # Loop over elves.
            presents, max_elf = (1 + house) * 11, sqrt(house)
            for elf in count(2):

                # Loop from 2 to square root of house.
                if elf > max_elf:
                    break

                # Check if elf visits given house.
                if house % elf == 0:
                    if elves[elf] < 50:
                        presents += int(elf * 11)
                        elves[elf] += 1
                    if elves[int(house / elf)] < 50:
                        presents += int(int(house / elf) * 11)
                        elves[int(house / elf)] += 1
            print(house, presents, end="\r")

            # If given house satisfies minimum presents requirement, return.
            if presents >= self.data:
                return house


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
