class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of strings.
        """
        data = open(path, "r").read().split("\n")
        return data

    def part1(self, strings: list) -> int:
        """
        Counts how many strings are nice in given string list.

        Args:
            strings (list): List of strings.

        Returns:
            int: Number of nice strings.
        """

        # Loop over strings in list.
        num_nice = 0
        for s in strings:

            # Loop over characters in string.
            num_vowels, has_double_letter, has_bad_str = 0, False, False
            for i, c in enumerate(s):

                # Check for number of vowels, double letter, and naughty strings.
                if c in "aeiou":
                    num_vowels += 1

                if i < len(s) - 1:
                    if s[i : i + 2] in ["ab", "cd", "pq", "xy"]:
                        has_bad_str = True
                    if s[i] == s[i + 1]:
                        has_double_letter = True

            # Update nice string counter.
            if not has_bad_str and (num_vowels >= 3 and has_double_letter):
                num_nice += 1

        return num_nice

    def part2(self, strings: list) -> int:
        """
        Counts how many strings are nice in given string list.

        Args:
            strings (list): List of strings.

        Returns:
            int: Number of nice strings.
        """

        # Loop over strings in list.
        num_nice = 0
        for s in strings:

            # Loop over characters in string.
            has_repeat_letter, has_2_letter_pairs, letter_pairs = False, False, []
            for i, c in enumerate(s):

                # Check for two letter pairs.
                if i < len(s) - 1:
                    if s[i : i + 2] in letter_pairs[:-1]:
                        has_2_letter_pairs = True
                    letter_pairs.append(s[i : i + 2])

                # Check for repeat letters.
                if i < len(s) - 2:
                    if s[i] == s[i + 2]:
                        has_repeat_letter = True

            # Update nice string counter.
            if has_repeat_letter and has_2_letter_pairs:
                num_nice += 1

        return num_nice


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(strings=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(strings=input_data)
    print(f"Part 2: {pt2_soln}")
