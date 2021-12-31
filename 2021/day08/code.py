class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.split(" | ") for x in data]
        data = [[y.split(" ") for y in x] for x in data]
        self.data = data

    def part1(self) -> int:
        """
        Returns number of instances of digits 1, 4, 7, 8 in output values.

        Returns:
            int: Number of instances.
        """
        num_total = 0
        for row in self.data:
            for s in row[1]:
                num_total = num_total + 1 if len(s) in [2, 4, 3, 7] else num_total
        return num_total

    def part2(self) -> int:
        """
        Returns sum of all decoded output values.

        Returns:
            int: Sum of output values.
        """

        # Map unique digits from part 1.
        digits_segments = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        digits_mapping = {}
        for i, row in enumerate(self.data):
            digits_mapping[i] = {}
            for s in row[0]:

                # Parse digits (1, 4, 7, 8).
                if len(s) in [2, 4, 3, 7]:
                    digit = [
                        x for x in digits_segments if digits_segments[x] == len(s)
                    ][0]
                    digits_mapping[i][digit] = "".join(sorted(list(s)))

        # Map rest of digits.
        for i, row in enumerate(self.data):
            for s in row[0]:

                # Parse digits (2, 3, 5).
                if len(s) == 5:
                    if len("".join(set(s).intersection(digits_mapping[i][4]))) == 2:
                        digits_mapping[i][2] = "".join(sorted(list(s)))
                    elif len("".join(set(s).intersection(digits_mapping[i][1]))) == 2:
                        digits_mapping[i][3] = "".join(sorted(list(s)))
                    else:
                        digits_mapping[i][5] = "".join(sorted(list(s)))

                # Parse digits (0, 6, 9)
                elif len(s) == 6:
                    if len("".join(set(s).intersection(digits_mapping[i][4]))) == 4:
                        digits_mapping[i][9] = "".join(sorted(list(s)))
                    elif len("".join(set(s).intersection(digits_mapping[i][1]))) == 2:
                        digits_mapping[i][0] = "".join(sorted(list(s)))
                    else:
                        digits_mapping[i][6] = "".join(sorted(list(s)))

            digits_mapping[i] = {
                key: digits_mapping[i][key] for key in sorted(digits_mapping[i])
            }

        # Compute and return sum of outputs.
        total_sum = 0
        for i, row in enumerate(self.data):
            output_number = ""
            for s in row[1]:
                digit = [
                    x
                    for x in digits_mapping[i]
                    if digits_mapping[i][x] == "".join(sorted(list(s)))
                ][0]
                output_number += str(digit)
            total_sum += int(output_number)
        return total_sum


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
