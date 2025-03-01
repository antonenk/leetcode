#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 48% runtime / 99% mem


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        result = set()
        for f in folder:
            components = f.split("/")
            isChild = False
            for j in range(2, len(components)):
                parent = "/".join(components[:j])
                if parent in result:
                    isChild = True
                    break
            if not isChild:
                result.add(f)

        return list(result)


def test_1():
    assert Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]) == ["/a", "/c/d", "/c/f"]


def test_2():
    assert Solution().removeSubfolders(["/a", "/a/b/c", "/a/b/d"]) == ["/a"]


def test_3():
    assert Solution().removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]) == ["/a/b/c", "/a/b/ca", "/a/b/d"]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
