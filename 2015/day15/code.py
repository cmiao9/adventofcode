from itertools import combinations
from math import prod


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.replace(",", "").lower().split(" ") for x in data]

        # Compile ingredient information.
        stats = {}
        for row in data:
            stats[row[0]] = {
                "capacity": int(row[2]),
                "durability": int(row[4]),
                "flavor": int(row[6]),
                "texture": int(row[8]),
                "calories": int(row[10]),
            }
        self.stats = stats

    def part1(self, total_volume: int = 100) -> int:
        """
        Computes score of most optimal recipe with given total volume.

        Args:
            total_volume (int): Total volume of ingredients required.

        Returns:
            int: Score of most optimal recipe.
        """
        return self.find_recipe(total_volume)

    def find_recipe(self, total_volume: int, calories: int = 0) -> int:
        """
        Finds optimal recipe with given ingredient property stats, total required volume, and required calorie count.

        Args:
            total_volume (int): Total volume of ingredients required.
            calories (int): Required calories of recipe.

        Returns:
            int: Score of optimal recipe.
        """

        # Loop through "bars" (recipes) of stars and bars method.
        max_score = 0
        bar_indices = list(range(total_volume))
        for bars in combinations(bar_indices, len(self.stats) - 1):
            bars = [0] + sorted(bars) + [total_volume]

            # Parse ingredient volumes with given bar configuration.
            volumes = {ingredient: 0 for ingredient in self.stats}
            for i, ingredient in enumerate(volumes):
                volumes[ingredient] = bars[i + 1] - bars[i]

            # Calculate score and update max score if applicable.
            score = self.calculate_score(volumes, calories)
            max_score = score if score > max_score else max_score

        # Return highest scoring recipe score.
        return max_score

    def calculate_score(self, volumes: dict, calories: int = 0) -> int:
        """
        Calculates score of given volumes of ingredients, enforcing required calorie count constraint.

        Args:
            volumes (dict): Volumes of ingredients in this recipe.
            calories (int): Required calories of recipe.

        Returns:
            int: Score of given recipe. Returns 0 if there are negative properties or doesn't meet calorie count.
        """

        # Loop through ingredient volumes and compile property sums.
        score = {}
        for ingredient in volumes:
            for prop in self.stats[ingredient]:
                if prop not in score:
                    score[prop] = 0
                score[prop] += volumes[ingredient] * (self.stats[ingredient][prop])

        # Enforce calorie count if provided.
        if calories and score["calories"] != calories:
            return 0

        # Compute sum as product of properties, enforcing non-negative properties constraint.
        score = {key: max(0, val) for key, val in score.items() if key != "calories"}
        final_score = prod(list(score.values()))
        return final_score

    def part2(self, total_volume: int = 100, calories: int = 500) -> int:
        """
        Computes score of most optimal recipe with given total volume and calorie count.

        Args:
            total_volume (int): Total volume of ingredients required.
            calories (int): Caloric count required for recipe.

        Returns:
            int: Score of most optimal recipe.
        """
        return self.find_recipe(total_volume, calories)


if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
