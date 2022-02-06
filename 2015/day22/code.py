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
                        "heal": int(row.split()[4]),
                        "effect": int(row.split()[5]),
                        "mana": int(row.split()[6]),
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
        """Calculates minimum required mana to spend and beat boss."""

        player = {"hit points": 10, "mana": 250, "damage": 0, "armor": 0}
        boss = {"hit points": 13, "damage": 8}
        (
            player_state_history,
            boss_state_history,
            spell_history,
            min_cost,
        ) = self.find_min_cost([player], [boss], [], {}, 0, 0)

        print(f"\n player_state_history \n {player_state_history} \n")
        print(f"\n boss_state_history \n {boss_state_history} \n")
        print(f"\n spell_history \n {spell_history} \n")

        # player = {"hit points": 50, "mana": 500, "damage": 0, "armor": 0}
        # (
        #     player_state_history,
        #     boss_state_history,
        #     spell_history,
        #     min_cost,
        # ) = self.find_min_cost([player], [self.boss], [], {}, 0, 0)
        #
        # print(f"\n player_state_history \n {player_state_history} \n")
        # print(f"\n boss_state_history \n {boss_state_history} \n")
        # print(f"\n spell_history \n {spell_history} \n")

        return min_cost

    def find_min_cost(
        self,
        player_state_history: list,
        boss_state_history: list,
        spell_history: list,
        running_effects: dict,
        running_cost: int,
        min_cost: int,
    ) -> tuple:
        """todo"""

        new_player_state_history = self.copy(player_state_history)
        new_boss_state_history = self.copy(boss_state_history)
        player_history_dict = (
            {} if not player_state_history else player_state_history[-1]
        )
        boss_history_dict = {} if not boss_state_history else boss_state_history[-1]

        player_state = self.copy(player_history_dict)
        boss_state = self.copy(boss_history_dict)
        new_spell_history = self.copy(spell_history)
        effects = self.copy(running_effects)

        # Loop through all possible spells
        for spell in self.get_possible_spells(player_state["mana"], effects):
            new_running_cost = running_cost + self.shop["spells"][spell]["cost"]

            # Do player turn.
            new_player_state, new_boss_state, new_effects = self.apply_effects(
                player_state, boss_state, effects
            )
            new_player_state, new_boss_state, new_effects = self.use_spell(
                new_player_state, new_boss_state, spell, new_effects
            )
            new_player_state, new_boss_state, new_effects = self.apply_effects(
                new_player_state, new_boss_state, new_effects
            )
            new_player_state["mana"] -= self.shop["spells"][spell]["cost"]
            if new_boss_state["hit points"] <= 0 and (
                not min_cost or new_running_cost < min_cost
            ):
                new_player_state_history.append(new_player_state)
                new_boss_state_history.append(new_boss_state)
                new_spell_history.append(spell)
                min_cost = new_running_cost
                continue

            # Do boss turn.
            new_player_state["hit points"] -= max(
                new_boss_state["damage"] - new_player_state["armor"], 1
            )
            if new_player_state["hit points"] <= 0:
                continue

            # If neither player nor boss died after this spell, continue fighting.
            (
                spell_player_state_history,
                spell_boss_state_history,
                spell_spell_history,
                new_min_cost,
            ) = self.find_min_cost(
                player_state_history + [new_player_state],
                boss_state_history + [new_boss_state],
                spell_history + [spell],
                new_effects,
                new_running_cost,
                min_cost,
            )
            new_min_cost = min_cost if not new_min_cost else new_min_cost
            if (not min_cost and new_min_cost) or new_min_cost < min_cost:
                min_cost = new_min_cost
                new_player_state_history = spell_player_state_history
                new_boss_state_history = spell_boss_state_history
                new_spell_history = spell_spell_history

        return (
            new_player_state_history,
            new_boss_state_history,
            new_spell_history,
            min_cost,
        )

    def copy(self, x):
        """todo"""
        if isinstance(x, dict):
            return {self.copy(key): self.copy(val) for key, val in x.items()}
        elif isinstance(x, list):
            return [self.copy(y) for y in x]
        else:
            return x

    def get_possible_spells(self, mana: int, effects: dict) -> list:
        """todo"""
        possible_spells = []
        for spell in self.shop["spells"]:
            if spell not in effects and self.shop["spells"][spell]["cost"] <= mana:
                possible_spells.append(spell)
        return possible_spells

    def update_player_state(self, player_state: dict, spell: str) -> dict:
        """todo"""

        spell_stats = self.shop["spells"][spell]
        new_player_state = {
            "hit points": player_state["hit points"] + spell_stats["heal"],
            "mana": player_state["mana"] + spell_stats["mana"],
            "damage": player_state["damage"] + spell_stats["damage"],
            "armor": player_state["armor"] + spell_stats["armor"],
        }
        return new_player_state

    def use_spell(
        self, player_state: dict, boss_state: dict, spell: str, effects: dict
    ) -> tuple:
        """todo"""

        # Process effects.
        new_effects = self.copy(effects)
        effects_length = self.shop["spells"][spell]["effect"]
        if effects_length > 0:
            new_effects[spell] = effects_length
            return player_state, boss_state, new_effects

        # Update player state with specified spell.
        new_player_state = self.copy(player_state)
        new_boss_state = self.copy(boss_state)
        new_player_state = self.update_player_state(new_player_state, spell)

        # Update boss state accordingly.
        new_boss_state["hit points"] = (
            new_boss_state["hit points"] - new_player_state["damage"]
        )
        new_player_state["damage"] = 0
        return new_player_state, new_boss_state, new_effects

    def apply_effects(
        self, player_state: dict, boss_state: dict, effects: dict
    ) -> tuple:
        """todo"""

        new_player_state = self.copy(player_state)
        new_boss_state = self.copy(boss_state)
        new_effects = {}
        for effect in effects:
            if effect == "shield":
                new_player_state = self.update_player_state(new_player_state, effect)
            elif effect == "poison":
                new_boss_state["hit points"] -= self.shop["spells"][effect]["damage"]

            if effects[effect] > 1:
                new_effects[effect] = effects[effect] - 1
        new_player_state["damage"] = 0
        return new_player_state, new_boss_state, new_effects

    def part2(self) -> int:
        """Calculates maximum required mana to spend and not beat boss."""

        # todo
        return 0


if __name__ == "__main__":
    solution = Solution("test.txt", "input.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
