#!/usr/bin/python3

# https://leetcode.com/problems/removing-stars-from-a-string/description/
# beats 76% runtime / 22% mem


class Solution:
    def removeStars(self, s: str) -> str:
        result: list[str] = []
        for ch in s:
            if ch == "*":
                result.pop()
            else:
                result.append(ch)
        return "".join(result)


def test_1():
    assert Solution().removeStars("leet**cod*e") == "lecoe"


def test_2():
    assert Solution().removeStars("erase*****") == ""


if __name__ == '__main__':
    test_1()
    test_2()
