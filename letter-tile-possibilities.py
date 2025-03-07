#!/usr/bin/python3

# https://leetcode.com/problems/letter-tile-possibilities/description/
# beats 77% runtime / 19% mem


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        combination: dict[str, int] = {}
        for symbol in tiles:
            combination[symbol] = combination.get(symbol, 0) + 1

        tilesCount = 0
        combinations = {"": combination}
        nextCombinations = {}
        for length in range(1, len(tiles) + 1):
            for prefix, combination in combinations.items():
                for symbol, count in combination.items():
                    nextCombination = combination.copy()
                    if count == 1:
                        del nextCombination[symbol]
                    else:
                        nextCombination[symbol] = count - 1
                    nextCombinations[prefix + symbol] = nextCombination
                    tilesCount += 1

            combinations = nextCombinations
            nextCombinations = {}

        return tilesCount


def test_1():
    assert Solution().numTilePossibilities("AAB") == 8


def test_2():
    assert Solution().numTilePossibilities("AAABBC") == 188


def test_3():
    assert Solution().numTilePossibilities("V") == 1


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
