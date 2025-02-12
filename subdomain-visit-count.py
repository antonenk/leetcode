#!/usr/bin/python3

# https://leetcode.com/problems/subdomain-visit-count/description/
# beats 94% runtime / 48% mem


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        visitsPerDomain: dict[str, int] = {}
        for cpdomain in cpdomains:
            fields = cpdomain.split(" ")
            visits = int(fields[0])
            domainComponents = fields[1].split(".")
            for i in range(len(domainComponents)):
                domain = ".".join(domainComponents[i:])
                visitsPerDomain[domain] = visitsPerDomain.get(domain, 0) + visits
        return [f"{visitsPerDomain[domain]} {domain}" for domain in visitsPerDomain.keys()]


def test_1():
    cpdomains = ["9001 discuss.leetcode.com"]
    expected = [
        "9001 discuss.leetcode.com",
        "9001 leetcode.com",
        "9001 com"
        ]
    assert Solution().subdomainVisits(cpdomains) == expected


def test_2():
    cpdomains = [
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org",
        ]
    expected = [
        "900 google.mail.com",
        "901 mail.com",
        "951 com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org",
        "5 org",
        ]
    assert Solution().subdomainVisits(cpdomains) == expected


if __name__ == '__main__':
    test_1()
    test_2()
