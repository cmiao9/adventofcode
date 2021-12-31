from hashlib import md5


class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of keys.
        """
        data = open(path, "r").read().split("\n")
        return data

    def part1(self, keys: list, prefix: str = "00000") -> list:
        """
        Gets smallest integer that when appended to end of key will yield an MD5 hash that starts with 5 zeros.

        Args:
            keys (list): List of secret key strings to use in hash.
            prefix (string): Optional string prefix of hash.

        Returns:
            list: List of integer results by key.
        """
        results = []
        for key in keys:
            i, md5_hash = 0, md5("sample".encode())
            while md5_hash.hexdigest()[: len(prefix)] != prefix:
                sample_string = key + str(i)
                md5_hash = md5(sample_string.encode())
                i += 1
            results.append(i - 1)
        return results

    def part2(self, keys: list) -> list:
        """
        Gets smallest integer that when appended to end of key will yield an MD5 hash that starts with 6 zeros.

        Args:
            keys (list): List of secret key strings to use in hash.

        Returns:
            list: List of integer results by key.
        """
        return self.part1(keys=keys, prefix="000000")


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(keys=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(keys=input_data)
    print(f"Part 2: {pt2_soln}")
