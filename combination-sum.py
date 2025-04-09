#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 90% runtime / 41% mem

def combinationSumR(candidates: list[int], target: int, candidatesCount: int) -> list[list[int]]:
    combinations = []
    for index in range(candidatesCount):
        candidate = candidates[index]
        if candidate > target:
            break
        elif candidate == target:
            combinations.append([candidate])
        else:
            subCombinations = combinationSumR(candidates, target - candidate, index + 1)
            for subCombination in subCombinations:
                subCombination.append(candidate)
                combinations.append(subCombination)

    return combinations


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        return combinationSumR(candidates, target, len(candidates))


def test_1():
    output = Solution().combinationSum([2, 3, 6, 7], 7)
    assert output == [[2, 2, 3], [7]]


def test_2():
    output = Solution().combinationSum([2, 3, 5], 8)
    assert output == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_3():
    output = Solution().combinationSum([2], 1)
    assert output == []


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
