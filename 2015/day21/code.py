from itertools import combinations


class Solution:
    def __init__(self, test_path: str, input_path: str) -> None:
        """
        Loads data from given file path.

        Args:
            test_path (str): Path to test data.
            input_path (str): Path to input data.
        """

        # Parse shop items stored in test_path.
        test_data = open(test_path, "r").read().strip().split("\n")
        shop = {}
        for row in test_data:
            if row:
                if ":" in row:
                    new_class = row.split(":")[0].lower()
                    shop[new_class] = {}
                else:
                    shop[new_class][row.split()[0].lower()] = {
                        "cost": int(row.split()[1]),
                        "damage": int(row.split()[2]),
                        "armor": int(row.split()[3]),
                    }
        self.shop = shop

        # Parse boss stats stored in input_path.
        input_data = open(input_path, "r").read().strip().split("\n")
        boss = {}
        for row in input_data:
            boss[row.split(":")[0].lower()] = int(row.split(":")[1])
        self.boss = boss

        self.test_path = test_path
        self.input_path = input_path

    def part1(self) -> int:
        """Calculates minimum required gold to spend and beat boss."""

        # Iterate over weapons (must buy 1).
        min_cost = -1
        for weapon in self.shop["weapons"]:

            # Iterate over armor. (buy 0 or 1)
            for armor in [] + list(self.shop["armor"]):

                # Iterate over rings. (buy 0 or 1 or 2)
                for rings in (
                    []
                    + [[x] for x in self.shop["rings"]]
                    + list(combinations(list(self.shop["rings"]), 2))
                ):

                    # Update cost if lower than current minimum cost and defeats boss.
                    if self.defeats_boss(weapon, armor, rings):
                        cost = self.compile_stats(weapon, armor, rings, "cost")
                        if min_cost == -1 or cost < min_cost:
                            min_cost = cost

        # Return minimum cost.
        return min_cost

    def compile_stats(self, weapon, armor, rings, stat) -> int:
        """Compile item stats."""
        stats = self.shop["weapons"][weapon][stat]
        stats = stats + self.shop["armor"][armor][stat] if armor else stats
        for ring in rings:
            stats += self.shop["rings"][ring][stat]
        return stats

    def defeats_boss(self, weapon, armor, rings) -> bool:
        """Check whether given player items will defeat the boss."""

        # Reset boss and calculate player stats.
        self.__init__(self.test_path, self.input_path)
        player = {
            "hit points": 100,
            "damage": self.compile_stats(weapon, armor, rings, "damage"),
            "armor": self.compile_stats(weapon, armor, rings, "armor"),
        }

        # Take turns until someone dies.
        while True:

            # Take player turn.
            self.boss["hit points"] -= max(player["damage"] - self.boss["armor"], 1)
            if self.boss["hit points"] < 0:
                return True

            # Take boss turn, and check if player dead.
            player["hit points"] -= max(self.boss["damage"] - player["armor"], 1)
            if player["hit points"] < 0:
                return False

    def part2(self) -> int:
        """Calculates maximum required gold to spend and not beat boss."""

        # Iterate over weapons (must buy 1).
        max_cost = 0
        for weapon in self.shop["weapons"]:

            # Iterate over armor. (buy 0 or 1)
            for armor in [[]] + list(self.shop["armor"]):

                # Iterate over rings. (buy 0 or 1 or 2)
                for rings in (
                    [[]]
                    + [[x] for x in self.shop["rings"]]
                    + list(combinations(list(self.shop["rings"]), 2))
                ):

                    # Update cost if higher than current maximum cost and doesn't defeat boss.
                    if not self.defeats_boss(weapon, armor, rings):
                        cost = self.compile_stats(weapon, armor, rings, "cost")
                        max_cost = max(cost, max_cost)

        # Return maximum cost.
        return max_cost


if __name__ == "__main__":
    solution = Solution("test.txt", "input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
