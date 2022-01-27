class Solution:
    def load_data(self, path: str) -> list:
        """
        Loads data from given file path.

        Args:
            path (str): Path to data.

        Returns:
            list: List of passwords.
        """
        data = open(path, "r").read().strip().split("\n")
        return data

    def part1(self, passwords: list) -> list:
        """
        Calculates next valid password.

        Args:
            passwords (list): List of passwords.

        Returns:
            list: List of next valid passwords.
        """
        new_passwords = []
        for password in passwords:
            new_password = "".join(self.increment_password(list(password)))
            while not self.check_password(new_password):
                new_password = "".join(self.increment_password(list(new_password)))
            new_passwords.append(new_password)
        return new_passwords

    def increment_password(self, password: list, index: int = -1) -> list:
        """
        Increments given password from given index.

        Args:
            password (list): Password as list of characters.
            index (int): Index to increment.

        Returns:
            list: Next password as list of characters.
        """
        if len(password) + index < 0:
            password = ["z"] + password
        elif password[index] != "z":
            password[index] = chr(ord(password[index]) + 1)
        else:
            password[index] = "a"
            password = self.increment_password(password, index - 1)
        return password

    def check_password(self, password: str) -> bool:
        """
        Checks whether given password is valid.

        Args:
            password (str): Password to check.

        Returns:
            bool: Whether or not password is valid.
        """

        has_increasing_straight = False
        for i in range(len(password) - 2):
            c1, c2, c3 = ord(password[i]), ord(password[i + 1]), ord(password[i + 2])
            if c2 - c1 == 1 and c3 - c2 == 1:
                has_increasing_straight = True

        has_bad_letters = False
        for c in ["i", "o", "l"]:
            if c in password:
                has_bad_letters = True

        unique_pairs = []
        for i in range(len(password) - 1):
            c1, c2 = password[i], password[i + 1]
            if c1 == c2 and c1 not in unique_pairs:
                unique_pairs.append(c1)
        has_unique_pairs = len(unique_pairs) >= 2

        return has_increasing_straight and not has_bad_letters and has_unique_pairs

    def part2(self, passwords: list) -> list:
        """
        Calculates list of second to next valid passwords.

        Args:
            passwords (list): List of passwords.

        Returns:
            list: List of second to next valid passwords.
        """
        return self.part1(self.part1(passwords))


if __name__ == "__main__":
    solution = Solution()
    input_data = solution.load_data("input.txt")

    pt1_soln = solution.part1(passwords=input_data)
    print(f"Part 1: {pt1_soln}")

    pt2_soln = solution.part2(passwords=input_data)
    print(f"Part 2: {pt2_soln}")
