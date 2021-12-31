from typing import List


class Solution:
    def __init__(self, path: str) -> None:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.
        """
        data = open(path, "r").read().strip().split("\n")
        data = [int(x, 16) for x in data]
        self.data = data

        print(self.parse_packet("00111000000000000110111101000101001010010001001000000000"))

    def part1(self) -> list:
        """Returns sum of packet version numbers."""
        total_sums = []
        # for num in self.data:
        #     total_sums.append(self.get_version_sum(format(num, 'b')))
        return total_sums

    def parse_packet(
        self,
        binary_num: str,
        total_lengths: list = None,
        num_subpackets: list = None,
        parsed_packet: str = "",
    ) -> str:
        """todo"""

        packet_version = int(binary_num[:3], 2)
        packet_type_id = int(binary_num[3:6], 2)

        parsed_packet = (
            parsed_packet
            + f" packet_version {packet_version} packet_type_id {packet_type_id} "
        )

        # Parse literal values.
        if packet_type_id == 4:
            literal, remaining_bits = self.parse_literal(binary_num[6:])
            parsed_packet = parsed_packet + f" literal {literal} "

            if total_lengths:
                total_lengths[-1] -= len(binary_num) - len(remaining_bits)
            if num_subpackets:
                num_subpackets[-1] -= 1

        # Parse operator packets.
        else:
            length_type_id = binary_num[6]
            parsed_packet = parsed_packet + f" length_type_id {length_type_id} "

            if length_type_id == "0":
                total_length = int(binary_num[7:22], 2)
                parsed_packet = parsed_packet + f" total_length {total_length} "

                if total_lengths:
                    total_lengths[-1] -= 22
                if num_subpackets:
                    num_subpackets[-1] -= 1

                remaining_bits = binary_num[22:]
                total_lengths = [] if total_lengths is None else total_lengths
                parsed_packet = self.parse_packet(
                    remaining_bits, total_lengths + [total_length], num_subpackets, parsed_packet
                )

            elif length_type_id == "1":
                num_subpacket = int(binary_num[7:18], 2)
                parsed_packet = parsed_packet + f" num_subpacket {num_subpacket} "

                if total_lengths:
                    total_lengths[-1] -= 18
                if num_subpackets:
                    num_subpackets[-1] -= 1

                remaining_bits =str(int(binary_num[18:], 2))
                parsed_packet = parsed_packet + self.parse_packet(remaining_bits)

        return parsed_packet

    def parse_subpacket(self, binary_num: str) -> tuple:
        """todo"""

    def parse_literal(self, binary_num: str) -> tuple:
        """todo"""
        literal_str = ""
        group_id = 1
        while group_id:
            group_id = int(binary_num[0])
            literal_str += binary_num[1:5]
            binary_num = binary_num[5:]
        return int(literal_str, 2), binary_num

    def part2(self) -> None:
        """todo"""
        return


if __name__ == "__main__":
    solution = Solution("test.txt")
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
