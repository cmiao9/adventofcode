from re import finditer
from random import shuffle


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
        molecules = {}
        for sequence in self.start_sequences:
            molecules[sequence] = []
            for replacement in self.replacements:
                for i, j in [m.span() for m in finditer(replacement[0], sequence)]:
                    new_sequence = sequence[:i] + replacement[1] + sequence[j:]
                    molecules[sequence].append(new_sequence)
        return [len(set(x)) for x in molecules.values()]

    def part2(self) -> list:
        """Calculates number of steps it takes to construct medicine molecule."""
        steps = {}
        for start_sequence in self.start_sequences:
            steps[start_sequence] = 0
            sequence = start_sequence
            while True:
                while True:
                    updated = False
                    for replacement in self.replacements:
                        matches = [m.span() for m in finditer(replacement[1], sequence)]
                        if matches:
                            i, j = matches[0]
                            sequence = sequence[:i] + replacement[0] + sequence[j:]
                            steps[start_sequence] += 1
                            updated = True
                        else:
                            break
                    if not updated:
                        break
                if not any(c != "e" for c in sequence):
                    break
                else:
                    shuffle(self.replacements)
        return list(steps.values())


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
