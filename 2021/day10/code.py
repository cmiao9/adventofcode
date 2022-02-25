class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        self.data = data

    def part1(self) -> int:
        """Returns total syntax error score for errors in data."""
        score = 0
        for row in self.data:
            score += self.calculate_score_corrupt(row)
        return score

    def calculate_score_corrupt(self, s: str) -> int:
        """
        Calculates syntax error score of given string. Returns 0 if valid or incomplete, but not corrupted.

        Args:
            s (str): String input.

        Returns:
            int: Syntax error score.
        """
        chunks_dict = {
            ")": ["(", 3],
            "]": ["[", 57],
            "}": ["{", 1197],
            ">": ["<", 25137],
        }
        open_chunks = []
        for c in s:
            if c in [x[0] for x in chunks_dict.values()]:
                open_chunks.append(c)
            elif c in chunks_dict.keys():
                if chunks_dict[c][0] != open_chunks[-1]:
                    return chunks_dict[c][1]
                else:
                    open_chunks = open_chunks[:-1]
        return 0

    def calculate_score_incomplete(self, s: str) -> int:
        """
        Calculates autocomplete score of given string. Returns 0 if valid or corrupted.

        Args:
            s (str): String input.

        Returns:
            int: Autocomplete score.
        """

        # Accumulate all open chunks.
        chunks_dict = {")": ["(", 1], "]": ["[", 2], "}": ["{", 3], ">": ["<", 4]}
        open_chunks = []
        for c in s:
            if c in [x[0] for x in chunks_dict.values()]:
                open_chunks.append(c)
            elif c in chunks_dict.keys():
                if chunks_dict[c][0] != open_chunks[-1]:
                    return 0
                else:
                    open_chunks = open_chunks[:-1]

        # Calculate score and return.
        score = 0
        for chunk in reversed(open_chunks):
            chunk_point = [
                chunks_dict[key][1]
                for key in chunks_dict
                if chunks_dict[key][0] == chunk
            ][0]
            score = score * 5 + chunk_point
        return score

    def part2(self) -> int:
        """Returns middle score of incomplete strings."""
        scores = []
        for row in self.data:
            score = self.calculate_score_incomplete(row)
            if score:
                scores.append(score)
        return sorted(scores)[int((len(scores) - 1) / 2)]


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
