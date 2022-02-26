class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [[int(y) for y in list(x)] for x in data]
        self.grid = data

    def print_grid(self, grid) -> None:
        """Prints grid."""
        print()
        [print(" ".join([str(x) for x in row])) for row in grid]
        print()

    def part1(self) -> int:
        """Returns lowest risk of path from top left to bottom right of grid."""


        return

    def djisktra(self, grid: list) -> int:
        """todo"""

        # Initialize unvisited nodes set and distance values for Djisktra's.
        unvisited, distances = [], {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                unvisited.append([i, j])
                distances[f"{i},{j}"] = float("inf")

        # Start at upper left corner.
        distances["0,0"] = 0
        unvisited.remove([0, 0])

        # Loop until all nodes are visited.
        while unvisited:

            current_node = self.get_smallest_unvisited_node(unvisited)
            for neighbor in self.get_unvisited_neighbors(grid, current_node[0], current_node[1], unvisited):
                new_distance = grid


    def get_smallest_unvisited_node(self, unvisited: list) -> list:
        """todo"""

    def get_unvisited_neighbors(self, grid: list, i: int, j: int, unvisited: list) -> list:
        """todo"""



    def part2(self) -> None:
        """todo"""
        return


if __name__ == "__main__":
    solution = Solution("test.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
