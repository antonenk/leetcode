#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 89% runtime / 79% mem


class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        countOfResponses: dict[str, int] = {}
        for nonuniqueResponses in responses:
            for response in set(nonuniqueResponses):
                countOfResponses[response] = countOfResponses.get(response, 0) + 1
        maxCount = 0
        for response, count in countOfResponses.items():
            if count > maxCount:
                maxCount = count
                mostFrequentResponse = response
            elif count == maxCount and response < mostFrequentResponse:
                mostFrequentResponse = response

        return mostFrequentResponse


def test_1():
    responses = [
        ["good", "ok", "good", "ok"],
        ["ok", "bad", "good", "ok", "ok"],
        ["good"],
        ["bad"]
        ]
    assert Solution().findCommonResponse(responses) == "good"


def test_2():
    responses = [
        ["good", "ok", "good"],
        ["ok", "bad"],
        ["bad", "notsure"],
        ["great", "good"]
        ]
    assert Solution().findCommonResponse(responses) == "bad"


if __name__ == '__main__':
    test_1()
    test_2()
