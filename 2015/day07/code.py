class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of instructions.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [x.split(" ") for x in data]
        return data

    def part1(self, instructions: list) -> dict:
        """
        Performs instructions list to generate final dictionary of wires with corresponding signals.

        Args:
            instructions (list): List of instructions.

        Returns:
            dict: Dictionary containing wires and corresponding signals.
        """

        # Loop over instructions list.
        wires_dict = {}
        while instructions:
            unused_instructions = []
            for instruction in instructions:

                # Check that instruction can be carried out.
                vs = []
                for val in instruction[:-2]:
                    if val not in ["NOT", "AND", "OR", "LSHIFT", "RSHIFT"]:
                        vs.append(self.check_val(val, wires_dict))
                if -1 in vs:
                    unused_instructions.append(instruction)
                    continue

                # Carry out instructions and update wires.
                v1 = vs[0]
                v2 = vs[1] if len(vs) == 2 else -1
                wire = instruction[-1]

                # NOT v1 -> w
                if "NOT" in instruction:
                    wires_dict[wire] = self.correct_out_of_bounds(~v1)

                # v1 LSHIFT v2 -> w
                elif "LSHIFT" in instruction:
                    wires_dict[wire] = self.correct_out_of_bounds(v1 << v2)

                # v1 RSHIFT v2 -> w
                elif "RSHIFT" in instruction:
                    wires_dict[wire] = self.correct_out_of_bounds(v1 >> v2)

                # v1 AND v2 -> w
                elif "AND" in instruction:
                    wires_dict[wire] = self.correct_out_of_bounds(v1 & v2)

                # v1 OR v2 -> w
                elif "OR" in instruction:
                    wires_dict[wire] = self.correct_out_of_bounds(v1 | v2)

                # v1 -> w
                else:
                    wires_dict[wire] = v1

            instructions = unused_instructions

        return wires_dict

    def correct_out_of_bounds(self, x: int) -> int:
        """
        Corrects input signal to be between 0 and 65535.

        Args:
            x (int): Input signal.

        Returns:
            int: Corrected signal between 0 and 65535.

        """
        return x % 65536

    def check_val(self, x: str, wires_dict: dict) -> int:
        """
        Parses instruction string part. Returns -1 if not initialized yet.

        Args:
            x (str): Instruction string part.
            wires_dict (dict): Dictionary of wires and corresponding signals.

        Returns:
            int: Parsed instruction part. Returns -1 if not initialized yet.

        """
        if x.isdigit():
            return int(x)
        if x in wires_dict:
            return wires_dict[x]
        return -1

    def part2(self, instructions: list) -> dict:
        """
        Performs instructions list to generate final dictionary of wires with corresponding signals,
            with b initialized to 46065.

        Args:
            instructions (list): List of instructions.

        Returns:
            dict: Dictionary containing wires and corresponding signals.
        """
        for i, instruction in enumerate(instructions):
            if instruction[1] == "->" and instruction[2] == "b":
                instructions[i][0] = "46065"
        return self.part1(instructions)


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(instructions=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(instructions=input_data)
    print(f"Part 2: {pt2_soln}")
