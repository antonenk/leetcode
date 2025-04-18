#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 92% runtime / 93% mem


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        waitingTime = 0
        busyTill = 0
        for customer in customers:
            arrival = customer[0]
            needTime = customer[1]
            if busyTill < arrival:
                busyTill = arrival + needTime
                waitingTime += needTime
            else:
                busyTill += needTime
                waitingTime += busyTill - arrival

        return waitingTime / len(customers)


def test_1():
    assert Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]) == 5


def test_2():
    assert Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25


if __name__ == '__main__':
    test_1()
    test_2()
