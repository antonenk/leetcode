#!/usr/bin/python3

class Solution:
    def validStrings(self, n: int) -> list[str]:
        if n == 1:
            return ["0", "1"]

        result = []
        for prefix in self.validStrings(n-1):
            if prefix[-1] == "0":
                result.append(prefix + "1")
            else:
                result.append(prefix + "0")
                result.append(prefix + "1")
        return result


def test_1():
    assert Solution().validStrings(3) == ["010", "011", "101", "110", "111"]


def test_2():
    assert Solution().validStrings(1) == ["0", "1"]


if __name__ == '__main__':
    test_1()
    test_2()
