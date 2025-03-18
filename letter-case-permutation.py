#!/usr/bin/python3

# https://leetcode.com/problems/letter-case-permutation/description/
# beats 12% runtime / 98% mem


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        template = list(s)
        digits = set(list("0123456789"))
        letters = []
        for position in range(len(template)):
            symbol = template[position]
            if symbol not in digits:
                letters.append((position, symbol.lower(), symbol.upper()))

        lettersCount = len(letters)
        maskFormat = '0' + str(lettersCount) + 'b'
        result = []
        for mask in range(2 ** lettersCount):
            maskString = format(mask, maskFormat)
            for letterId in range(lettersCount):
                position, lower, upper = letters[letterId]
                if maskString[letterId] == '0':
                    template[position] = lower
                else:
                    template[position] = upper
            result.append("".join(template))

        return result


def test_1():
    assert Solution().letterCasePermutation("a1b2") == ["a1b2", "a1B2", "A1b2", "A1B2"]


def test_2():
    assert Solution().letterCasePermutation("3z4") == ["3z4", "3Z4"]


if __name__ == '__main__':
    test_1()
    test_2()
