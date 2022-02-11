class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.split(",") for x in data][0]
        data = [int(x) for x in data]
        self.initial_state = data
        self.days = 80

    def part1(self) -> int:
        """
        Calculates number of lantern fish from specified initial state after specified number of days.

        Returns:
            int: Number of lantern fish.
        """

        # Loop over days and update state.
        state = self.initial_state[:]
        for day in range(self.days):
            new_state = state[:]
            for i, fish in enumerate(state):
                if fish == 0:
                    new_state[i] = 6
                    new_state.append(8)
                else:
                    new_state[i] = fish - 1
            state = new_state[:]

        # Return number of fish in final state.
        return len(state)

    def part2(self) -> int:
        """
        Calculates number of lantern fish from specified initial state after specified number of days.

        Returns:
            int: Number of lantern fish.
        """

        # Initialize new data structure to represent fish state.
        self.days = 256
        state = [0] * 9
        for i in range(len(state)):
            state[i] = self.initial_state.count(i)

        # Loop over days and update state.
        for day in range(self.days):
            new_state = [0] * len(state)
            for i in range(len(state)):
                if i == 0:
                    new_state[8] += state[i]
                    new_state[6] += state[i]
                else:
                    new_state[i - 1] += state[i]
            state = new_state[:]

        # Return number of fish in final state.
        return sum(state)


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
