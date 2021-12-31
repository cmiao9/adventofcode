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

    def part1(self, strings: list) -> int:
        """
        Calculates number of string literals minus number of values in memory for list of strings.

        Args:
            strings (list): List of strings.

        Returns:
            int: Number of string literals minus number of values in memory.
        """

        # Loop over list of strings.
        num_literals, num_memory = 0, 0
        for s in strings:

            # Count string literals.
            s_len = len(s)
            num_literals += s_len

            # Count characters in memory.
            num_subtract = 2

            # Remove start and end quotes.
            s = s[1:-1]

            # Check for escape characters
            while "\\" in s:
                i = s.index("\\")
                if s[i + 1] in ["\\", '"']:
                    num_subtract += 1
                    s = s[0:i] + s[i + 2 :]
                elif s[i + 1] == "x":
                    num_subtract += 3
                    s = s[:i] + s[i + 4 :]

            num_memory += s_len - num_subtract

        return num_literals - num_memory

    def part2(self, strings: list) -> int:
        """
        Calculates number of newly encoded strings minus number of original string literals.

        Args:
            strings (list): List of strings.

        Returns:
            int: Number of newly encoded strings minus number of original string literals.
        """

        # Loop over list of strings.
        num_old, num_new = 0, 0
        for s in strings:

            # Count string literals.
            num_old += len(s)

            # Count newly encoded string.
            num_new += len(s) + s.count('"') + s.count("\\") + 2

        return num_new - num_old


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(strings=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(strings=input_data)
    print(f"Part 2: {pt2_soln}")
