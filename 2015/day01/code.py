class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List containing floor instructions as strings.
        """
        data = open(path, "r").read().split("\n")
        return data

    def part1(self, instructions: list) -> list:
        """
        Returns list of final floors after parsing instructions list.

        Args:
            instructions (list): List of instruction strings in parentheses.

        Returns:
            list: List of final integer floors.
        """
        floors = []
        for s in instructions:
            floor = 0
            for c in s:
                floor = floor + 1 if (c == "(") else floor - 1
            floors.append(floor)
        return floors

    def part2(self, instructions: list) -> list:
        """
        Returns list of basement positions after parsing instructions list.

        Args:
            instructions (list): List of instruction strings in parentheses.

        Returns:
            list: List of final integer basement positions.
        """
        positions = []
        for s in instructions:
            floor = 0
            for i, c in enumerate(s):
                floor = floor + 1 if (c == "(") else floor - 1
                if floor == -1:
                    break
            positions.append(i + 1)
        return positions


if __name__ == "__main__":
    solution = Solution()
    instruction_data = solution.load_data("input.txt")

    pt1_floor = solution.part1(instructions=instruction_data)
    print(f"Part 1: {pt1_floor}")

    pt2_position = solution.part2(instructions=instruction_data)
    print(f"Part 2: {pt2_position}")
