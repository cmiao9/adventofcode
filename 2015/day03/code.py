class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of instructions.
        """
        data = open(path, "r").read().split("\n")
        return data

    def part1(self, instructions: list) -> list:
        """
        Counts total unique houses Santa visits.

        Args:
            instructions (list): List of elf instructions directing Santa.

        Returns:
            list: Number of unique houses Santa visits for each instruction string.
        """
        instructions_dict = {">": [1, 0], "<": [-1, 0], "^": [0, 1], "v": [0, -1]}
        results_list = []
        for s in instructions:
            x, y, num_houses, unique_houses = 0, 0, 1, [[0, 0]]
            for c in s:
                x += instructions_dict[c][0]
                y += instructions_dict[c][1]
                if [x, y] not in unique_houses:
                    num_houses += 1
                    unique_houses.append([x, y])
            results_list.append(num_houses)
        return results_list

    def part2(self, instructions: list) -> list:
        """
        Counts total unique houses Santa and Robo Santa visit.

        Args:
            instructions (list): List of elf instructions directing Santa and Robo Santa.

        Returns:
            list: Number of unique houses Santa and Robo Santa visit for each instruction string.
        """
        instructions_dict = {">": [1, 0], "<": [-1, 0], "^": [0, 1], "v": [0, -1]}
        results_list = []
        for instruction in instructions:
            santa_s, robo_s = instruction[0::2], instruction[1::2]
            num_houses, unique_houses = 1, [[0, 0]]
            for s in [santa_s, robo_s]:
                x, y = 0, 0
                for c in s:
                    x += instructions_dict[c][0]
                    y += instructions_dict[c][1]
                    if [x, y] not in unique_houses:
                        num_houses += 1
                        unique_houses.append([x, y])
            results_list.append(num_houses)
        return results_list


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(instructions=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(instructions=input_data)
    print(f"Part 2: {pt2_soln}")
