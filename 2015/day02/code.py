class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of lists containing integer dimensions (l, w, h) of each present.
        """
        data = open(path, "r").read().split("\n")
        data = [[int(x) for x in s.split("x")] for s in data]
        return data

    def part1(self, presents: list) -> int:
        """
        Calculates total required wrapping paper to wrap all presents.

        Args:
            presents (list): List of lists containing integer dimensions (l, w, h) of each present.

        Returns:
            int: Total required wrapping paper (in square feet).
        """
        total_paper = 0
        for l, w, h in presents:
            surface_area = 2 * l * w + 2 * w * h + 2 * h * l
            min_surface = min(l * w, w * h, h * l)
            total_paper += surface_area + min_surface
        return total_paper

    def part2(self, presents: list) -> int:
        """
        Calculates total required ribbon to tie all presents.

        Args:
            presents (list): List of lists containing integer dimensions (l, w, h) of each present.

        Returns:
            int: Total required ribbon (in feet).
        """
        total_ribbon = 0
        for l, w, h in presents:
            volume = l * w * h
            min_perimeter = 2 * min(l + w, w + h, h + l)
            total_ribbon += volume + min_perimeter
        return total_ribbon


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(presents=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(presents=input_data)
    print(f"Part 2: {pt2_soln}")
