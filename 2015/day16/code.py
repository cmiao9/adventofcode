class Solution:
    def __init__(self, test_path: str, input_path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """

        # Process test data.
        test_data = open(test_path, "r").read().strip().split("\n")
        test_data = [x.replace(":", "").split(" ") for x in test_data]
        test_data = {x[0]: int(x[1]) for x in test_data}
        self.test_data = test_data

        # Process input data.
        input_data = open(input_path, "r").read().strip().split("\n")
        input_data = [
            x.replace(":", "").replace(",", "").split(" ") for x in input_data
        ]
        input_data = {
            x[1]: {x[2]: int(x[3]), x[4]: int(x[5]), x[6]: int(x[7])}
            for x in input_data
        }
        self.input_data = input_data

    def part1(self) -> int:
        """
        Calculates which aunt gave gift.

        Returns:
            int: Index of aunt who gave gift.
        """

        # Iterate over Aunt Sues.
        for aunt in self.input_data:
            is_aunt = True

            # Check gift items for each aunt.
            for item in self.input_data[aunt]:
                is_aunt = (
                    False
                    if self.input_data[aunt][item] != self.test_data[item]
                    else is_aunt
                )

            # If there is a match, return this aunt.
            if is_aunt:
                return aunt
        return 0

    def part2(self) -> int:
        """
        Calculates which aunt gave gift.

        Returns:
            int: Index of aunt who gave gift.
        """

        # Iterate over Aunt Sues.
        for aunt in self.input_data:
            is_aunt = True

            # Check gift items for each aunt.
            for item in self.input_data[aunt]:
                if item in ["cats", "trees"]:
                    is_aunt = (
                        False
                        if self.input_data[aunt][item] <= self.test_data[item]
                        else is_aunt
                    )
                elif item in ["pomeranians", "goldfish"]:
                    is_aunt = (
                        False
                        if self.input_data[aunt][item] >= self.test_data[item]
                        else is_aunt
                    )
                else:
                    is_aunt = (
                        False
                        if self.input_data[aunt][item] != self.test_data[item]
                        else is_aunt
                    )

            # If there is a match, return this aunt.
            if is_aunt:
                return aunt
        return 0


if __name__ == "__main__":
    solution = Solution("test.txt", "input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
