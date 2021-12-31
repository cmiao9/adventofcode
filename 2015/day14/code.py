class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List containing reindeer information.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.split(" ") for x in data]
        return data

    def part1(self, data: list, time: int = 2503) -> int:
        """
        Returns distance traveled of winning reindeer.

        Args:
            data (list): List containing reindeer information.
            time (int): Total race time.

        Returns:
            int: Total distance traveled by winning reindeer.
        """

        # Get all reindeer stats and initialize starting distance to 0.
        stats, distances = {}, {}
        for row in data:
            reindeer, speed, sustain, rest = (
                row[0],
                int(row[3]),
                int(row[6]),
                int(row[13]),
            )
            stats[reindeer] = {"speed": speed, "sustain": sustain, "rest": rest}
            distances[reindeer] = 0

        # Calculate reindeer distances over time.
        for second in range(time):
            for reindeer in distances:
                distances[reindeer] += self.track_distance(stats[reindeer], second)

        # Return winning distance.
        return max(list(distances.values()))

    def track_distance(self, reindeer_stats: dict, second: int) -> int:
        """
        Returns distance reindeer traveled in the last second.

        Args:
            reindeer_stats (dict): Reindeer speed, sustain, and rest times.
            second (int): Current time.

        Returns:
            int: Distance reindeer traveled in last second.
        """
        speed, sustain, rest = (
            reindeer_stats["speed"],
            reindeer_stats["sustain"],
            reindeer_stats["rest"],
        )
        loop_second = second % (sustain + rest)
        if loop_second < sustain:
            return speed
        return 0

    def part2(self, data: list, time: int = 2503) -> int:
        """
        Returns points of winning reindeer.

        Args:
            data (list): List containing reindeer information.
            time (int): Total race time.

        Returns:
            int: Number of points of winning reindeer.
        """

        # Get all reindeer stats and initialize starting distance to 0.
        stats, distances = {}, {}
        for row in data:
            reindeer, speed, sustain, rest = (
                row[0],
                int(row[3]),
                int(row[6]),
                int(row[13]),
            )
            stats[reindeer] = {"speed": speed, "sustain": sustain, "rest": rest}
            distances[reindeer] = 0

        # Calculate reindeer points over time.
        points = dict(distances)
        for second in range(time):
            for reindeer in distances:
                distances[reindeer] += self.track_distance(stats[reindeer], second)

            # Update reindeer points every second.
            max_distance = max(list(distances.values()))
            reindeer_points = [r for r in distances if distances[r] == max_distance]
            for reindeer in reindeer_points:
                points[reindeer] += 1

        # Return winning points.
        return max(list(points.values()))


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(data=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(data=input_data)
    print(f"Part 2: {pt2_soln}")
