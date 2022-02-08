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
        return 0

    def part2(self) -> None:
        """todo"""
        return


if __name__ == "__main__":
    solution = Solution("test.txt", "input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
