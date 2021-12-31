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
        self.steps = 10

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
        """Performs a single replacement step on given sequence."""
        new_sequence = sequence[0]
        for i in range(len(sequence) - 1):
            pair = sequence[i : i + 2]
            if pair in [x[0] for x in self.rules]:
                replacement = [x[1] for x in self.rules if x[0] == pair][0]
                new_sequence += replacement + pair[1]
            else:
                new_sequence += pair[1]
        return new_sequence

    def part1_v2(self) -> int:
        """Returns the difference between the most and least common element quantity after iterating for given steps."""

        # Create final sequence after performing given number of steps.
        sequence = self.start_sequence
        for step in range(self.steps):
            for rule in self.rules:
                sequence = sequence.replace(
                    rule[0], rule[0][0] + rule[1].lower() + rule[0][1]
                )
                sequence = sequence.replace(
                    rule[0], rule[0][0] + rule[1].lower() + rule[0][1]
                )
            sequence = sequence.upper()

        # Compute difference between most and least common elements and return.
        count_dict = {x: sequence.count(x) for x in sequence}
        return max(count_dict.values()) - min(count_dict.values())

    def part2(self) -> int:
        """Returns the difference between the most and least common element quantity after iterating for given steps."""

        self.steps = 40

        # Dictionary containing index of rules.
        rev_rules = {}
        for i in range(len(self.rules)):
            rev_rules[self.rules[i][0]] = i

        # Initialize results grid (self.steps x len(self.rules)).
        results = []
        for i in range(self.steps + 1):
            results.append([0] * len(self.rules))

        # Add initial values (for step = 0).
        for j in range(len(self.rules)):
            rule_dict = self.frequency_dict()
            rule_dict[self.rules[j][0][0]] += 1
            rule_dict[self.rules[j][0][1]] += 1
            results[0][j] = rule_dict

        # Iterate over steps.
        for i in range(1, self.steps + 1):
            for j in range(len(self.rules)):

                rule = self.rules[j]
                left_str = rule[0][0] + rule[1]
                right_str = rule[1] + rule[0][1]

                middle_letter = self.frequency_dict()
                middle_letter[rule[1]] -= 1

                results[i][j] = self.dict_add(
                    results[i - 1][rev_rules[left_str]],
                    results[i - 1][rev_rules[right_str]],
                )
                results[i][j] = self.dict_add(results[i][j], middle_letter)

        # Run with starting sequence.
        result_dict = self.frequency_dict()
        for i in range(len(self.start_sequence) - 1):
            rule = self.start_sequence[i : i + 2]
            result_dict = self.dict_add(
                result_dict, results[self.steps][rev_rules[rule]]
            )
        middle_letters = self.frequency_dict()
        for i in range(1, len(self.start_sequence) - 1):
            middle_letters[self.start_sequence[i]] -= 1
        result_dict = self.dict_add(result_dict, middle_letters)

        # Return difference between most and least frequenct letters.
        return max(list(result_dict.values())) - min(list(result_dict.values()))

    def frequency_dict(self) -> dict:
        """Returns dictionary of letter frequency, initialized to 0."""
        letters_dict = {}
        for i in range(len(self.rules)):
            for letter in self.rules[i][0]:
                letters_dict[letter] = 0
        return letters_dict

    def dict_add(self, dict1: dict, dict2: dict) -> dict:
        """Adds 2 dictionaries by key."""
        dict3 = {}
        for key in dict1:
            dict3[key] = dict1[key] + dict2[key]
        return dict3


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
