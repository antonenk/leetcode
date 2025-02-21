#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 100% runtime / 92% mem

def generateRestOfParenthesis(s: str, opensLeft: int, closesLeft: int) -> list[str]:
    if opensLeft == 0:
        result = [s + ")" * closesLeft]
    else:
        result = generateRestOfParenthesis(s + "(", opensLeft - 1, closesLeft)
        if closesLeft > opensLeft:
            result += generateRestOfParenthesis(s + ")", opensLeft, closesLeft - 1)

    return result


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return generateRestOfParenthesis("", n, n)


def test_1():
    assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


def test_2():
    assert Solution().generateParenthesis(1) == ["()"]


if __name__ == '__main__':
    test_1()
    test_2()
