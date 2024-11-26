#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 72% runtime / 55% mem


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        minutesPerUser = {}
        for userID, minute in logs:
            if userID not in minutesPerUser:
                minutesPerUser[userID] = {minute}
            else:
                minutesPerUser[userID].add(minute)

        result = [0] * k
        for minutes in minutesPerUser.values():
            if len(minutes) <= k:
                result[len(minutes) - 1] += 1

        return result


def test_1():
    logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k = 5
    output = Solution().findingUsersActiveMinutes(logs, k)
    expected = [0, 2, 0, 0, 0]
    assert output == expected


def test_2():
    logs = [[1, 1], [2, 2], [2, 3]]
    k = 4
    output = Solution().findingUsersActiveMinutes(logs, k)
    expected = [1, 1, 0, 0]
    assert output == expected


def test_3():
    logs = [
        [283268890, 14532],
        [283268891, 14530],
        [283268889, 14530],
        [283268892, 14530],
        [283268890, 14531]]
    k = 2
    output = Solution().findingUsersActiveMinutes(logs, k)
    expected = [3, 1]
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
