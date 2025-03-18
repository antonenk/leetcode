#!/usr/bin/python3

# https://leetcode.com/problems/letter-case-permutation/description/
# beats 9% runtime / 74% mem


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        template = list(s)
        digits = set(list("0123456789"))
        letterPositions = []
        for position in range(len(template)):
            if template[position] not in digits:
                letterPositions.append(position)

        lettersCount = len(letterPositions)
        maskFormat = '0' + str(lettersCount) + 'b'
        result = []
        for mask in range(2 ** lettersCount):
            maskString = format(mask, maskFormat)
            for letterId in range(lettersCount):
                letterPosition = letterPositions[letterId]
                letter = template[letterPosition]
                if maskString[letterId] == '0':
                    template[letterPosition] = letter.lower()
                else:
                    template[letterPosition] = letter.upper()
            result.append("".join(template))

        return result


def test_1():
    assert Solution().letterCasePermutation("a1b2") == ["a1b2", "a1B2", "A1b2", "A1B2"]


def test_2():
    assert Solution().letterCasePermutation("3z4") == ["3z4", "3Z4"]


if __name__ == '__main__':
    test_1()
    test_2()
