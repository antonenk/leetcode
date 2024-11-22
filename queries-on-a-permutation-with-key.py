#!/usr/bin/python3

# https://leetcode.com/problems/queries-on-a-permutation-with-key/description/
# beats 65% runtime / 72% mem


class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = [i + 1 for i in range(m)]
        positions = []
        for query in queries:
            position = p.index(query)
            positions.append(position)
            p.remove(query)
            p.insert(0, query)
        return positions


def test_1():
    queries = [3,1,2,1]
    m = 5
    output = Solution().processQueries(queries, m)
    expected = [2,1,2,1] 
    assert output == expected


def test_2():
    queries = [4,1,2,2]
    m = 4
    output = Solution().processQueries(queries, m)
    expected = [3,1,2,0]
    assert output == expected


if __name__ == '__main__':
    test_1()
    test_2()
