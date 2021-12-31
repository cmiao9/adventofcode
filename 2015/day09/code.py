from itertools import permutations


class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: todo
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.split(" ") for x in data]
        return data

    def part1(self, locations: list, min_max: str = "min") -> int:
        """
        Calculates distance of shortest route that visits all locations in list.

        Args:
            locations (list): List of distances between locations.
            min_max (str): Specify whether to return the min or max distance.

        Returns:
            int: Distance of shortest route that visits all locations.
        """

        # Grab all locations to map out all possible routes, and create distances dictionary.
        unique_locations, distances = [], {}
        for location in locations:
            loc1, loc2, dist = location[0], location[2], int(location[4])

            # Compile list of unique locations.
            for loc in [loc1, loc2]:
                if loc not in unique_locations:
                    unique_locations.append(loc)

                # Compile a dictionary of all distances.
                if loc not in distances:
                    distances[loc] = {}

            distances[loc1][loc2] = dist
            distances[loc2][loc1] = dist

        # Construct all possible routes and distances.
        route_distances = []
        for route in permutations(unique_locations):
            distance = 0
            for i in range(len(route) - 1):
                loc1, loc2 = route[i], route[i + 1]
                distance += distances[loc1][loc2]
            route_distances.append(distance)

        # Returns either minimum or maximum route distance.
        if min_max == "min":
            return min(route_distances)
        elif min_max == "max":
            return max(route_distances)

    def part2(self, locations: list) -> int:
        """
        Calculates distance of longest route that visits all locations in list.

        Args:
            locations (list): List of distances between locations.

        Returns:
            int: Distance of longest route that visits all locations.
        """
        return self.part1(locations, "max")


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(locations=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(locations=input_data)
    print(f"Part 2: {pt2_soln}")
