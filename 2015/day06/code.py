class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of instructions.
        """
        data = open(path, "r").read().split("\n")
        data = [x.replace("turn ", "").split(" ") for x in data]
        return data

    def part1(self, instructions: list) -> int:
        """
        Calculates how many lights are turned on after following all instructions.

        Args:
            instructions (list): List of instructions.

        Returns:
            int: Number of lights that are on at the end.
        """

        # Create grid of 1000x1000 lights where 0 indicates off and 1 indicates on.
        grid = [[0] * 1000 for _ in range(1000)]

        # Loop through instructions list.
        for instruction in instructions:

            # Grab start and stop x, y coordinates of lights that need to be updated.
            start = [int(x) for x in instruction[1].split(",")]
            stop = [int(x) for x in instruction[3].split(",")]
            x0, x1, y0, y1 = start[0], stop[0] + 1, start[1], stop[1] + 1

            # Loop over lights that need to be updated for this instruction.
            for x in range(x0, x1):
                for y in range(y0, y1):

                    # Update lights (turn on, turn off, or toggle).
                    if "on" in instruction:
                        grid[x][y] = 1
                    elif "off" in instruction:
                        grid[x][y] = 0
                    elif "toggle" in instruction:
                        grid[x][y] = int(not grid[x][y])

        # Return the number of on lights by summing the grid.
        return sum([sum(x) for x in grid])

    def part2(self, instructions: list) -> int:
        """
        Calculates total grid brightness after following all instructions.

        Args:
            instructions (list): List of instructions.

        Returns:
            int: Total grid brightness at end.
        """

        # Create grid of 1000x1000 lights where the int element represents the brightness.
        grid = [[0] * 1000 for _ in range(1000)]

        # Loop through instructions list.
        for instruction in instructions:

            # Grab start and stop x, y coordinates of lights that need to be updated.
            start = [int(x) for x in instruction[1].split(",")]
            stop = [int(x) for x in instruction[3].split(",")]
            x0, x1, y0, y1 = start[0], stop[0] + 1, start[1], stop[1] + 1

            # Loop over lights that need to be updated for this instruction.
            for x in range(x0, x1):
                for y in range(y0, y1):

                    # Update lights (turn on, turn off, or toggle).
                    if "on" in instruction:
                        grid[x][y] += 1
                    elif "off" in instruction and grid[x][y] > 0:
                        grid[x][y] -= 1
                    elif "toggle" in instruction:
                        grid[x][y] += 2

        # Return total brightness of grid with a sum.
        return sum([sum(x) for x in grid])


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(instructions=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(instructions=input_data)
    print(f"Part 2: {pt2_soln}")
