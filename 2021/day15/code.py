import heapq


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

    def part1(self) -> int:
        """Returns lowest risk of path from top left to bottom right of grid."""
        return self.djisktra(self.grid)

    def djisktra(self, grid: list) -> int:
        """Run djisktra's on given grid."""

        # Initialize unvisited nodes and min distances for Djisktra's.
        unvisited_heap, unvisited_nodes, distances = [[0, [0, 0]]], [[0, 0]], {"0,0": 0}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i == j == 0:
                    unvisited_nodes.append([i, j])
                    distances[f"{i},{j}"] = float("inf")
        heapq.heapify(unvisited_heap)

        # Loop until all nodes are visited.
        while unvisited_nodes:

            # Visit unvisited node with smallest distance.
            while True:
                min_unvisited = heapq.heappop(unvisited_heap)
                current_distance, current_node = min_unvisited[0], min_unvisited[1]
                if (
                    distances[f"{current_node[0]},{current_node[1]}"]
                    <= current_distance
                ):
                    unvisited_nodes.remove(current_node)
                    break

            # Loop over neighbors and update neighbor distances.
            for neighbor in self.get_unvisited_neighbors(
                grid, current_node[0], current_node[1], unvisited_nodes
            ):
                new_distance = current_distance + grid[neighbor[0]][neighbor[1]]
                if new_distance < distances[f"{neighbor[0]},{neighbor[1]}"]:
                    distances[f"{neighbor[0]},{neighbor[1]}"] = new_distance
                    heapq.heappush(unvisited_heap, [new_distance, neighbor])

            print(len(unvisited_nodes), end="\r")

        # Return smallest distance to lower right corner.
        return distances[f"{len(grid) - 1},{len(grid[0]) - 1}"]

    def get_unvisited_neighbors(
        self, grid: list, i: int, j: int, unvisited_nodes: list
    ) -> list:
        """Return unvisited neighbors of given node."""
        neighbors = []
        if i - 1 >= 0 and [i - 1, j] in unvisited_nodes:
            neighbors.append([i - 1, j])
        if i + 1 < len(grid) and [i + 1, j] in unvisited_nodes:
            neighbors.append([i + 1, j])
        if j - 1 >= 0 and [i, j - 1] in unvisited_nodes:
            neighbors.append([i, j - 1])
        if j + 1 < len(grid[0]) and [i, j + 1] in unvisited_nodes:
            neighbors.append([i, j + 1])
        return neighbors

    def part2(self) -> int:
        """Returns lowest risk of path from top left to bottom right of expanded grid."""

        # Construct expanded grid.
        new_grid = []
        for rep in range(5):
            for row in self.grid:
                new_row = []
                for i in range(5):
                    new_row += self.incr_list(row, i + rep)
                new_grid.append(new_row)

        # Run djisktra.
        return self.djisktra(new_grid)

    def incr_list(self, lst: list, incr: int) -> list:
        """Increment list with given value, maintaining digits 1-9."""
        new_list = []
        for x in lst:
            new_x = (x + incr) % 10
            if new_x != x + incr:
                new_x += 1
            new_list.append(new_x)
        return new_list


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
