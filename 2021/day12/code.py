class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.split("-") for x in data]
        connections = []
        for connection in data:
            loc1, loc2 = connection[0], connection[1]
            if "start" in connection:
                loc = [x for x in connection if x != "start"][0]
                connections.append(["start", loc])
            elif "end" in connection:
                loc = [x for x in connection if x != "end"][0]
                connections.append([loc, "end"])
            else:
                connections.append([loc1, loc2])
                connections.append([loc2, loc1])
        self.connections = connections

    def part1(self) -> int:
        """Calculates number of paths from start to end, only visiting small caves at most once."""
        start_connections = [x for x in self.connections if "start" in x]
        connections = [x for x in self.connections if "start" not in x]
        paths = self.find_paths(start_connections, connections, 1)
        return len(paths)

    def find_paths(
        self, current_paths: list, connections: list, max_small_cave: int
    ) -> list:
        """
        Calculates all paths from start to end that satisfy the small cave requirement.

        Args:
            current_paths (list): List of existing current paths.
            connections (list): List of available connections.
            max_small_cave (int): Maximum visits to a single small cave.

        Returns:
            list: List of all paths from start to end that satisfy the small cave requirement.
        """
        paths = []
        for path in current_paths:
            if "end" in path:
                paths.append(path)
            else:
                for possible_connection in self.get_possible_connections(
                    path, connections, max_small_cave
                ):
                    new_path = path[:] + [possible_connection[1]]
                    paths.extend(
                        self.find_paths([new_path], connections, max_small_cave,)
                    )
        return [x for x in paths if x]

    def get_possible_connections(
        self, path: list, connections: list, max_small_cave: int
    ) -> list:
        """
        Gets all possible connections to given path.

        Args:
            path (list): Current path.
            connections (list): Available connections.
            max_small_cave (int): Maximum visits to a single small cave.

        Returns:
            list: List of all possible connections for given path.
        """

        # Count visited small caves in path.
        small_caves = {}
        for loc in path:
            if loc not in ["start", "end"] and loc == loc.lower():
                if loc not in small_caves:
                    small_caves[loc] = 1
                else:
                    small_caves[loc] += 1

        # Get possible connections for given path.
        possible_connections = []
        for connection in connections:
            if connection[0] == path[-1]:
                if connection[1] != "end" and connection[1] == connection[1].lower():
                    if not (
                        [
                            val
                            for key, val in small_caves.items()
                            if val >= max_small_cave
                        ]
                        and connection[1] in path
                    ):
                        possible_connections.append(connection)
                else:
                    possible_connections.append(connection)
        return possible_connections

    def part2(self) -> int:
        """Calculates number of paths from start to end, only visiting small caves at most once, except one twice."""
        start_connections = [x for x in self.connections if "start" in x]
        connections = [x for x in self.connections if "start" not in x]
        paths = self.find_paths(start_connections, connections, 2)
        return len(paths)

    def print_paths(self, paths) -> None:
        """Prints paths."""
        [print(path) for path in paths]


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
