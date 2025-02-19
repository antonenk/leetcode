#!/usr/bin/python3

# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
# beats 100% runtime / 94% mem


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        p = 2 ** (n - 1)
        if k <= p:
            symbol = "a"
            index = k - 1
        elif k <= 2 * p:
            symbol = "b"
            index = k - p - 1
        elif k <= 3 * p:
            symbol = "c"
            index = k - 2 * p - 1
        else:
            return ""
        symbols = [symbol]
        if n > 1:
            choices = '{0:010b}'.format(index)[11-n:]
            for choice in choices:
                if symbol == "a":
                    symbol = "b" if choice == "0" else "c"
                elif symbol == "b":
                    symbol = "a" if choice == "0" else "c"
                else:
                    symbol = "a" if choice == "0" else "b"
                symbols.append(symbol)

        return "".join(symbols)


def test_1():
    assert Solution().getHappyString(1, 3) == "c"


def test_2():
    assert Solution().getHappyString(1, 4) == ""


def test_3():
    assert Solution().getHappyString(3, 9) == "cab"


def test_4():
    assert Solution().getHappyString(2, 1) == "ab"


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
