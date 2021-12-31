class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.replace(",", "").replace("+", "").split(" ") for x in data]
        self.data = data
        self.register = {"a": 0, "b": 0}
        self.path = path

    def part1(self) -> dict:
        """Parses instruction list and returns final register state."""

        # Loop until index outside instruction list.
        i = 0
        while True:
            if i < 0 or i >= len(self.data):
                break
            instruction = self.data[i]

            # Parse instructions.
            if "hlf" in instruction:
                self.register[instruction[1]] /= 2
                i += 1
            elif "tpl" in instruction:
                self.register[instruction[1]] *= 3
                i += 1
            elif "inc" in instruction:
                self.register[instruction[1]] += 1
                i += 1
            elif "jmp" in instruction:
                i += int(instruction[1])
            elif "jie" in instruction:
                if not self.register[instruction[1]] % 2:
                    i += int(instruction[2])
                else:
                    i += 1
            elif "jio" in instruction:
                if self.register[instruction[1]] == 1:
                    i += int(instruction[2])
                else:
                    i += 1

        # Return register.
        return self.register

    def part2(self) -> dict:
        """Parses instruction list and returns final register state."""
        self.__init__(self.path)
        self.register["a"] = 1
        return self.part1()


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
