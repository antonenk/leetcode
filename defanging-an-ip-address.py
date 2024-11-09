#!/usr/bin/python3

# https://leetcode.com/problems/defanging-an-ip-address/description/


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


def test_1():
    assert Solution().defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"


if __name__ == '__main__':
    test_1()
