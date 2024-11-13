#!/usr/bin/python3

# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
# beats 92% runtime / 89% mem


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        beams_count = 0
        devices_count_in_previous_row = None
        for row in bank:
            devices_count = row.count("1")
            if devices_count > 0:
                if devices_count_in_previous_row is not None:
                    beams_count += devices_count_in_previous_row * devices_count
                devices_count_in_previous_row = devices_count
        return beams_count


def test_1():
    bank = ["011001",
            "000000",
            "010100",
            "001000"]
    assert Solution().numberOfBeams(bank) == 8


def test_2():
    bank = ["000",
            "111",
            "000"]
    assert Solution().numberOfBeams(bank) == 0


if __name__ == '__main__':
    test_1()
    test_2()
