
class Solution:

    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: todo
        """
        data = open(path, "r").read().strip().split("\n")
        return data

    def part1(self) -> None:
        """
        todo
        """
        return

    def part2(self) -> None:
        """
        todo
        """
        return


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("test.txt")

    pt1_soln = solution.part1()
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2()
    print(f"Part 2: {pt2_soln}")
