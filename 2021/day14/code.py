class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        rules = []
        for row in data:
            if "->" in row:
                rules.append(row.split(" -> "))
            elif row:
                start_sequence = row
        self.rules = rules
        self.start_sequence = start_sequence
        self.steps = 2

    def part1(self) -> int:
        """Returns the difference between the most and least common element quantity after iterating for given steps."""

        # Create final sequence after performing given number of steps.
        sequence = self.start_sequence
        for step in range(self.steps):
            sequence = self.perform_replacement(sequence)

        # Compute difference between most and least common elements and return.
        count_dict = {x: sequence.count(x) for x in sequence}
        return max(count_dict.values()) - min(count_dict.values())

    def perform_replacement(self, sequence: str) -> str:
        """todo"""
        new_sequence = sequence[0]
        for i in range(len(sequence) - 1):
            pair = sequence[i:i+2]
            if pair in [x[0] for x in self.rules]:
                replacement = [x[1] for x in self.rules if x[0] == pair][0]
                new_sequence += replacement + pair[1]
            else:
                new_sequence += pair[1]
        return new_sequence

    def part2(self) -> int:
        """Returns the difference between the most and least common element quantity after iterating for given steps."""

        # Create final sequence after performing given number of steps.
        self.steps = 40
        sequence = self.start_sequence
        for step in range(self.steps):
            for rule in self.rules:
                sequence.replace(rule[0], rule[0][0] + rule[1] + rule[0][1])  # fix this

        # Compute difference between most and least common elements and return.
        count_dict = {x: sequence.count(x) for x in sequence}
        return max(count_dict.values()) - min(count_dict.values())


if __name__ == "__main__":
    solution = Solution("test.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
