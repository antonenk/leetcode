#!/usr/bin/python3

# https://leetcode.com/problems/sort-vowels-in-a-string/description/
# beats 89% runtime / 9% mem


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        vowelsInString = []
        vowelsPositions = []
        result = list(s)
        for i in range(len(result)):
            if result[i] in vowels:
                vowelsInString.append(result[i])
                vowelsPositions.append(i)
        vowelsInString.sort()
        for j in range(len(vowelsInString)):
            result[vowelsPositions[j]] = vowelsInString[j]
        return "".join(result)


def test_1():
    assert Solution().sortVowels("lEetcOde") == "lEOtcede"


def test_2():
    assert Solution().sortVowels("lYmpH") == "lYmpH"


if __name__ == '__main__':
    test_1()
    test_2()
