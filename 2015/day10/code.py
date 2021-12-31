class Solution:
    def load_data(self, path: str) -> str:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            str: Look and say sequence.
        """
        data = open(path, "r").read().strip().split("\n")
        return data[0]

    def part1(self, sequence: str, iterations: int = 40) -> str:
        """
        Compute length of given sequence using look and say for given iterations.

        Args:
            sequence (str): Starting integer sequence.
            iterations (int): Number of iterations.

        Returns:
            str: Length of final look and say sequence.
        """

        # Loop over iterations.
        for i in range(iterations):

            # Loop over digits in sequence.
            new_seq, run = "", ""
            for c in sequence:

                # Add digit to run if part of current run.
                if not run or c == run[0]:
                    run += c

                # Otherwise, update the new sequence and reset the current run.
                else:
                    new_seq += str(len(run)) + run[0]
                    run = c

            # Final update of new sequence.
            new_seq += str(len(run)) + run[0]

            # Use new sequence as starting sequence for next iteration.
            sequence = new_seq

        # Return length of final sequence.
        return len(new_seq)

    def part2(self, sequence: str) -> str:
        """
        Compute length of given sequence using look and say for 50 iterations.

        Args:
            sequence (str): Starting integer sequence.

        Returns:
            str: Length of final look and say sequence.
        """
        return self.part1(sequence, 50)


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(sequence=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(sequence=input_data)
    print(f"Part 2: {pt2_soln}")
