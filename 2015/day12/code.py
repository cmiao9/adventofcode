import json


class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: Json data.
        """
        data = open(path, "r").read().strip()
        data = json.loads(data)
        return data

    def part1(self, json_data: list) -> int:
        """
        Calculates sum of all numbers in json document.

        Args:
            json_data (list): Json data.

        Returns:
            int: Sum of all numbers in json document.
        """
        sum_json = 0
        for element in json_data:
            sum_json = self.accumulate_sum(element, sum_json)
        return sum_json

    def accumulate_sum(self, json_element, sum_json: int, ignore_word: str = "") -> int:
        """
        Updates given sum with json element.

        Args:
            json_element: Json element.
            sum_json (int): Current sum.
            ignore_word (str): Word to ignore if it appears in dictionary.

        Returns:
            int: Updated sum.
        """
        if isinstance(json_element, int):
            sum_json += json_element
        elif isinstance(json_element, list):
            for element in json_element:
                sum_json = self.accumulate_sum(element, sum_json, ignore_word)
        elif isinstance(json_element, dict):
            dict_elements = list(json_element.keys()) + list(json_element.values())
            if not ignore_word or ignore_word not in dict_elements:
                for key in json_element:
                    sum_json = self.accumulate_sum(
                        json_element[key], sum_json, ignore_word
                    )
        return sum_json

    def part2(self, json_data: list) -> int:
        """
        Calculates sum of all numbers in json document, ignoring dictionaries containing the "red" keyword.

        Args:
            json_data (list): Json data.

        Returns:
            int: Sum of all numbers in json document.
        """
        sum_json = 0
        for element in json_data:
            sum_json = self.accumulate_sum(element, sum_json, "red")
        return sum_json


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(json_data=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(json_data=input_data)
    print(f"Part 2: {pt2_soln}")
