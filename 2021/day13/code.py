class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """

        # Read in dots and folds from data.
        data = open(path, "r").read().strip().split("\n")
        dots, folds = [], []
        for row in data:
            if "," in row:
                dots.append([int(x) for x in row.split(",")])
            elif "fold" in row:
                fold = row.split(" ")[2].split("=")
                fold[1] = int(fold[1])
                folds.append(fold)

        # Create initial grid.
        grid = []
        i_max = 2 if "input" in path else 1  # jank fix. Leon was here!
        for i in range((max([x[1] for x in dots]) + i_max)):
            grid.append([0] * (max([x[0] for x in dots]) + 1))
        for dot in dots:
            grid[dot[1]][dot[0]] = 1
        self.grid = grid
        self.folds = folds

    def print_grid(self, grid) -> None:
        """Prints grid."""
        print()
        for row in grid:
            row2 = [str(x).replace("0", ".").replace("1", "#") for x in row]
            print(" ".join(row2))
        print()

    def part1(self) -> int:
        """Returns number of dots after performing first fold instruction."""
        grid = self.grid
        grid = self.perform_fold(grid, self.folds[0])
        return sum([sum(x) for x in grid])

    def perform_fold(self, grid: list, fold: list) -> list:
        """
        Performs given fold on grid and returns updated grid.

        Args:
            grid (list): Given grid.
            fold (list): Given fold.

        Returns:
            list: Updated grid after fold.
        """

        # Preprocess vertical folds.
        if fold[0] == "y":
            original_fold = grid[:][: fold[1]]
            new_fold = grid[:][fold[1] + 1 :]
            new_fold = list(reversed(new_fold))

        # Preprocess horizontal folds.
        elif fold[0] == "x":
            original_fold = [row[: fold[1]] for row in grid]
            new_fold = [row[fold[1] + 1 :] for row in grid]
            new_fold = [list(reversed(row)) for row in new_fold]

        # Create new grid with correct dimensions.
        new_grid = []
        for i in range(max(len(original_fold), len(new_fold))):
            new_grid.append([0] * max(len(original_fold[0]), len(new_fold[0])))

        # Perform fold and return updated grid.
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                original_val = (
                    original_fold[i][j]
                    if 0 <= i < len(original_fold) and 0 <= j < len(original_fold[0])
                    else 0
                )
                new_val = (
                    new_fold[i][j]
                    if 0 <= i < len(new_fold) and 0 <= j < len(new_fold[0])
                    else 0
                )
                new_grid[i][j] = int(original_val or new_val)
        return new_grid

    def part2(self) -> None:
        """Prints final grid after completing all folds."""
        grid = self.grid
        for fold in self.folds:
            grid = self.perform_fold(grid, fold)
        self.print_grid(grid)


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
