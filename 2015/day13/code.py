from itertools import permutations


class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of happiness instructions.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.replace(".", "").split(" ") for x in data]
        return data

    def part1(self, data: list) -> int:
        """
        Calculates total change in happiness with optimal seating arrangement.

        Args:
            data (list): List of happiness instructions.

        Returns:
            int: Total change in happiness with optimal seating arrangement.
        """

        # Get unique people.
        unique_people = []
        for row in data:
            p1, p2 = row[0], row[-1]
            for p in [p1, p2]:
                if p not in unique_people:
                    unique_people.append(p)

        # Get all happiness changes.
        happiness_map = {}
        for row in data:
            p1, p2 = row[0], row[-1]
            direction = 1 if "gain" in row else -1
            happiness = direction * int(row[3])
            if p1 not in happiness_map:
                happiness_map[p1] = {}
            happiness_map[p1][p2] = happiness

        # Loop through all seating arrangements.
        max_happiness = 0
        for arrangement in permutations(unique_people):
            arrangement = list(arrangement)
            arrangement.append(arrangement[0])
            arrangement_happiness = 0

            # Loop through pairs of neighbors.
            for i in range(len(arrangement) - 1):
                p1, p2 = arrangement[i], arrangement[i + 1]
                arrangement_happiness += happiness_map[p1][p2]
                arrangement_happiness += happiness_map[p2][p1]

            # Update max happiness if this is the best current arrangement.
            if arrangement_happiness > max_happiness:
                max_happiness = arrangement_happiness

        return max_happiness

    def part2(self, data: list) -> int:
        """
        Calculates total change in happiness with optimal seating arrangement including neutral you.

        Args:
            data (list): List of happiness instructions.

        Returns:
            int: Total change in happiness with optimal seating arrangement.
        """

        # Get unique people.
        unique_people = ["you"]
        for row in data:
            p1, p2 = row[0], row[-1]
            for p in [p1, p2]:
                if p not in unique_people:
                    unique_people.append(p)

        # Get all happiness changes.
        happiness_map = {"you": {}}
        for row in data:
            p1, p2 = row[0], row[-1]
            direction = 1 if "gain" in row else -1
            happiness = direction * int(row[3])
            if p1 not in happiness_map:
                happiness_map[p1] = {}
            happiness_map[p1][p2] = happiness
            happiness_map[p1]["you"] = 0
            happiness_map["you"][p1] = 0

        # Loop through all seating arrangements.
        max_happiness = 0
        for arrangement in permutations(unique_people):
            arrangement = list(arrangement)
            arrangement.append(arrangement[0])
            arrangement_happiness = 0

            # Loop through pairs of neighbors.
            for i in range(len(arrangement) - 1):
                p1, p2 = arrangement[i], arrangement[i + 1]
                arrangement_happiness += happiness_map[p1][p2]
                arrangement_happiness += happiness_map[p2][p1]

            # Update max happiness if this is the best current arrangement.
            if arrangement_happiness > max_happiness:
                max_happiness = arrangement_happiness

        return max_happiness


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(data=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(data=input_data)
    print(f"Part 2: {pt2_soln}")
