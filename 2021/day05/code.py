class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """

        # Read in line data.
        data = open(path, "r").read().strip().split("\n")
        data = [x.replace(",", " ").replace(" -> ", " ").split() for x in data]
        data = [[int(y) for y in x] for x in data]
        self.data = data

        # Create grid tracking line intersections.
        max_coordinate = max([max(x) for x in data]) + 1
        self.grid = []
        for x in range(max_coordinate):
            self.grid.append([])
            for y in range(max_coordinate):
                self.grid[x].append(0)

        self.path = path

    def part1(self, include_diagonal=False) -> int:
        """
        Calculates number of points where at least 2 horizontal or vertical lines overlap.

        Args:
            include_diagonal (bool): Whether to include diagonal lines.

        Returns:
            int: Number of points where at least 2 lines intersect.
        """

        # Loop over all lines, considering only vertical and horizontal ones.
        for line in self.data:
            y1, x1, y2, x2 = line[0], line[1], line[2], line[3]

            # Process horizontal and vertical lines.
            if x1 == x2 or y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        self.grid[x][y] += 1

            # Process diagonal lines.
            elif include_diagonal:
                first_x = x1 if x1 < x2 else x2
                second_x = x2 if first_x == x1 else x1
                first_y = y1 if first_x == x1 else y2
                second_y = y2 if first_y == y1 else y1
                y_increment = 1 if first_y < second_y else -1
                y = first_y
                for x in range(first_x, second_x + 1):
                    self.grid[x][y] += 1
                    y += y_increment

        # Count intersections >= 2.
        num_points = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                if self.grid[x][y] >= 2:
                    num_points += 1

        return num_points

    def print_grid(self) -> None:
        """Display intersections grid."""
        print()
        for row in self.grid:
            print(" ".join([str(x) for x in row]))
        print()

    def part2(self) -> int:
        """
        Calculates number of points where at least 2 lines overlap.

        Returns:
            int: Number of points where at least 2 lines intersect.
        """
        self.__init__(self.path)
        return self.part1(True)


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
