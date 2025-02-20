#!/usr/bin/python3

# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
# beats 100% runtime / 51% mem

def isPossibleToGetTotal(num: str, total: int) -> bool:
    if int(num) == total:
        return True

    for i in range(1, len(num)):
        firstPart = num[0:i]
        secondPart = num[i:]
        if isPossibleToGetTotal(secondPart, total - int(firstPart)):
            return True

    return False


punishComponent = [
    1,
    9,
    10,
    36,
    45,
    55,
    82,
    91,
    99,
    100,
    235,
    297,
    369,
    370,
    379,
    414,
    657,
    675,
    703,
    756,
    792,
    909,
    918,
    945,
    964,
    990,
    991,
    999,
    1000,
]


class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(len(punishComponent)):
            if punishComponent[i] <= n:
                result += punishComponent[i] * punishComponent[i]
            else:
                break
        return result


def test_1():
    assert Solution().punishmentNumber(10) == 182


def test_2():
    assert Solution().punishmentNumber(37) == 1478


if __name__ == '__main__':
    for i in range(1, 1001):
        if isPossibleToGetTotal(str(i * i), i):
            print(f"    {i},")
    test_1()
    test_2()
