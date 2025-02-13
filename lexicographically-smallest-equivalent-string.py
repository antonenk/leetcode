#!/usr/bin/python3

# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
# beats 100% runtime / 95% mem

lettersBase = ord("a")
lettersCount = ord("z") - lettersBase + 1


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equivalents = [c for c in range(lettersCount)]
        for i in range(len(s1)):
            c1 = equivalents[ord(s1[i]) - lettersBase]
            c2 = equivalents[ord(s2[i]) - lettersBase]
            if c1 == c2:
                continue
            elif c1 > c2:
                c1, c2 = c2, c1
            for c in range(lettersCount):
                if equivalents[c] == c2:
                    equivalents[c] = c1
        return "".join([chr(equivalents[ord(ch) - lettersBase] + lettersBase) for ch in baseStr])


def test_1():
    assert Solution().smallestEquivalentString("parker", "morris", "parser") == "makkek"


def test_2():
    assert Solution().smallestEquivalentString("hello", "world", "hold") == "hdld"


def test_3():
    assert Solution().smallestEquivalentString("leetcode", "programs", "sourcecode") == "aauaaaaada"


def test_4():
    assert Solution().smallestEquivalentString(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "mcwcglxvlrwdtlmjwauaviyhuuoygi") == "mcwcglxvlrwdtlmjwauaviyhuuoygi"


def test_5():
    assert Solution().smallestEquivalentString(
        "opecenadojbodihfgmpijpfocomhcncicefpohkibjckijghii",
        "ndlbhpaeppgekfhnjnmmplmdoifdhbglmedpjgleofgnahglbe",
        "ttusuhhrabgsswpaapxoxdanchyccmpjitwwmfioedtbiggfru") == "ttusuaaraaasswaaaaxaxaaaaayaaaaaatwwaaaaaataaaaaru"


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
