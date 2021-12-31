from itertools import count


class Solution:
    def __init__(self, test_path: str, input_path: str) -> None:
        """
        Loads data from given file path.

        Args:
            test_path (str): Path to test data.
            input_path (str): Path to input data.
        """
        test_data = open(test_path, "r").read().strip().split("\n")
        test_data = [x.split() for x in test_data]
        test_data = [[int(y) for y in x] for x in test_data]
        self.grid = test_data

        input_data = open(input_path, "r").read().strip().split("\n")
        input_data = [
            x.replace(",", "").replace(".", "").split(" ") for x in input_data
        ][0]
        input_data = [int(x) for x in input_data if x.isdigit()]
        self.solution_coordinate = input_data

    def part1(self) -> int:
        """Calculates code to give weather machine."""

        # Loop over grid in specified order.
        x, y, i = 1, 1, 1
        code = self.grid[0][0]
        for _ in count():
            if y == i:
                i += 1
                x = i
                y = 1
            else:
                x -= 1
                y += 1

            # Calculate code and stop if at solution coordinate.
            code = code * 252533 % 33554393
            if [x, y] == self.solution_coordinate:
                break

        return code

    def part2(self) -> None:
        """Not applicable!"""
        return


if __name__ == "__main__":
    solution = Solution("test.txt", "input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
