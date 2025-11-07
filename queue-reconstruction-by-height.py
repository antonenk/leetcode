#!/usr/bin/python3

# https://leetcode.com/problems/queue-reconstruction-by-height/description/
# beats 14% runtime / 41% mem


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        personsCount = len(people)
        queue: list[list[int]] = [None] * personsCount  # type: ignore
        people.sort(key=lambda x: x[0])
        for person in people:
            h = person[0]
            k = person[1]
            for i in range(personsCount):
                if queue[i] is None:
                    if k > 0:
                        k -= 1
                    else:
                        queue[i] = person
                        break
                else:
                    if queue[i][0] == h:
                        k -= 1
        return queue


def test_1():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    output = Solution().reconstructQueue(people)
    assert output == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]


def test_2():
    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    output = Solution().reconstructQueue(people)
    assert output == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]


if __name__ == '__main__':
    test_1()
    test_2()
