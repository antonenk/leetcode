#!/usr/bin/python3

# https://leetcode.com/problems/design-browser-history/description/
# beats 76% runtime / 55% mem


class BrowserHistory:

    def __init__(self, homepage: str):
        self.position = 0
        self.pages = [homepage]

    def visit(self, url: str) -> None:
        self.position += 1
        if len(self.pages) > self.position:
            for i in range(len(self.pages) - self.position):
                self.pages.pop(self.position)
        self.pages.append(url)

    def back(self, steps: int) -> str:
        self.position -= steps
        if self.position < 0:
            self.position = 0
        return self.pages[self.position]

    def forward(self, steps: int) -> str:
        self.position += steps
        if self.position >= len(self.pages):
            self.position = len(self.pages) - 1
        return self.pages[self.position]


def test_1():
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    assert browserHistory.back(1) == "facebook.com"
    assert browserHistory.back(1) == "google.com"
    assert browserHistory.forward(1) == "facebook.com"
    browserHistory.visit("linkedin.com")
    assert browserHistory.forward(2) == "linkedin.com"
    assert browserHistory.back(2) == "google.com"
    assert browserHistory.back(7) == "leetcode.com"


if __name__ == '__main__':
    test_1()
