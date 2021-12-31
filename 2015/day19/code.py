from random import shuffle
from re import finditer


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        replacements = [x.replace(" => ", " ").split(" ") for x in data if "=>" in x]
        start_sequences = [x for x in data if x and "=>" not in x]
        self.replacements = replacements
        self.start_sequences = start_sequences

    def part1(self) -> list:
        """Calculates number of distinct molecules that can be created with a single replacement."""

        # Loop over start sequences.
        molecules = {}
        for sequence in self.start_sequences:

            # Loop over replacement rules.
            molecules[sequence] = []
            for replacement in self.replacements:

                # Replace all instances of given rule to generate a new sequence.
                for i, j in [m.span() for m in finditer(replacement[0], sequence)]:
                    new_sequence = sequence[:i] + replacement[1] + sequence[j:]
                    molecules[sequence].append(new_sequence)

        # Return distinct molecules created.
        return [len(set(x)) for x in molecules.values()]

    def part2(self) -> list:
        """Calculates number of steps it takes to construct medicine molecule."""

        # Loop over start sequences.
        steps = {}
        for start_sequence in self.start_sequences:
            steps[start_sequence] = 0
            sequence = start_sequence

            # Loop until start sequence is reduced to only e.
            while True:

                # Loop until no more replacements can be made.
                while True:

                    # Loop over replacements.
                    updated = False
                    for replacement in self.replacements:

                        # Make replacement if possible, otherwise move on the next replacement.
                        matches = [m.span() for m in finditer(replacement[1], sequence)]
                        if matches:
                            i, j = matches[0]
                            sequence = sequence[:i] + replacement[0] + sequence[j:]
                            steps[start_sequence] += 1
                            updated = True
                        else:
                            break

                    # If no replacements were made, stop.
                    if not updated:
                        break

                # Check if start sequence is reduced to only e. Otherwise, shuffle replacements and restart.
                if not any(c != "e" for c in sequence):
                    break
                else:
                    shuffle(self.replacements)

        # Return number of steps required to generate start sequences.
        return list(steps.values())


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
