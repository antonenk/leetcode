#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 39% runtime / 89% mem

import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def _getRatioIncrease(passed: int, total: int):
            return (passed + 1)/(total + 1) - passed/total
        classesHeap = [(-_getRatioIncrease(c[0], c[1]), c[0], c[1]) for c in classes]

        heapq.heapify(classesHeap)
        for _ in range(extraStudents):
            ratioIncrease, passedStudents, totalStudents = heapq.heappop(classesHeap)
            passedStudents += 1
            totalStudents += 1
            ratioIncrease = _getRatioIncrease(passedStudents, totalStudents)
            heapq.heappush(classesHeap, (-ratioIncrease, passedStudents, totalStudents))

        return sum([p/t for _, p, t in classesHeap]) / len(classes)

    def maxAverageRatio4(self, classes: list[list[int]], extraStudents: int) -> float:
        classesNum = len(classes)
        for c in classes:
            passedStudents = c[0]
            totalStudents = c[1]
            c.append((passedStudents + 1)/(totalStudents + 1) - passedStudents/totalStudents)  # type: ignore

        classes.sort(key=lambda c: c[2])

        while extraStudents > 0:
            c = classes.pop()

            passedStudents = c[0]
            totalStudents = c[1]
            ratioIncrease = c[2]
            if classesNum > 1:
                nextRatioIncrease = classes[-1][2]
            else:
                nextRatioIncrease = 0

            while extraStudents > 0 and nextRatioIncrease <= ratioIncrease:
                extraStudents -= 1
                passedStudents += 1
                totalStudents += 1
                ratioIncrease = (passedStudents + 1)/(totalStudents + 1) - passedStudents/totalStudents  # type: ignore

            for j in range(classesNum - 1, -1, -1):
                if j == 0 or classes[j - 1][2] <= ratioIncrease:
                    classes.insert(j, [passedStudents, totalStudents, ratioIncrease])
                    break

        avg = sum([c[0]/c[1] for c in classes]) / len(classes)
        return avg

    def maxAverageRatio3(self, classes: list[list[int]], extraStudents: int) -> float:
        classesNum = len(classes)
        for c in classes:
            passedStudents = c[0]
            totalStudents = c[1]
            c.append((passedStudents + 1)/(totalStudents + 1) - passedStudents/totalStudents)  # type: ignore

        classes.sort(key=lambda c: c[2])

        while extraStudents > 0:
            c = classes.pop()

            passedStudents = c[0]
            totalStudents = c[1]
            ratioIncrease = c[2]
            if classesNum > 1:
                nextRatioIncrease = classes[-1][2]
            else:
                nextRatioIncrease = 0

            while extraStudents > 0 and nextRatioIncrease <= ratioIncrease:
                extraStudents -= 1
                passedStudents += 1
                totalStudents += 1
                ratioIncrease = (passedStudents + 1)/(totalStudents + 1) - passedStudents/totalStudents  # type: ignore

            for j in range(classesNum - 1, -1, -1):
                if j == 0 or classes[j - 1][2] <= ratioIncrease:
                    classes.insert(j, [passedStudents, totalStudents, ratioIncrease])
                    break

        avg = sum([c[0]/c[1] for c in classes]) / len(classes)
        return avg

    def maxAverageRatio2(self, classes: list[list[int]], extraStudents: int) -> float:
        classesNum = len(classes)
        for c in classes:
            passedStudents = c[0]
            totalStudents = c[1]
            c.append((passedStudents + 1)/(totalStudents + 1) - passedStudents/totalStudents)  # type: ignore

        classes.sort(key=lambda c: c[2])

        for i in range(extraStudents):
            c = classes.pop()
            passedStudents = c[0] + 1
            totalStudents = c[1] + 1
            ratioIncrease = (passedStudents + 1)/(totalStudents + 1) - passedStudents/totalStudents
            for j in range(classesNum - 1, -1, -1):
                if j == 0 or classes[j - 1][2] <= ratioIncrease:
                    classes.insert(j, [passedStudents, totalStudents, ratioIncrease])  # type: ignore
                    break

        avg = sum([c[0]/c[1] for c in classes]) / len(classes)
        return avg

    def maxAverageRatio1(self, classes: list[list[int]], extraStudents: int) -> float:
        ratios = []
        maxClassSize = max([c[1] for c in classes])
        failedStudentsInClass: list[list[int]] = [[] for i in range(maxClassSize + 1)]

        haveFailedStudents = False
        for students in classes:
            passedStudents = students[0]
            totalStudents = students[1]
            if passedStudents == totalStudents:
                ratios.append(1)
            else:
                failedStudentsInClass[totalStudents].append(totalStudents - passedStudents)
                haveFailedStudents = True

        if not haveFailedStudents:
            return 1

        minSize = 1
        while len(failedStudentsInClass[minSize]) == 0:
            minSize += 1

        while extraStudents >= len(failedStudentsInClass[minSize]):
            extraStudents -= len(failedStudentsInClass[minSize])
            if len(failedStudentsInClass) < minSize:
                failedStudentsInClass[minSize + 1].extend(failedStudentsInClass[minSize])
            else:
                failedStudentsInClass[minSize + 1] = failedStudentsInClass[minSize]
            minSize += 1

#        for s in range(size, len(failedStudentsInClass)):

        avg = sum(ratios) / len(ratios)
        return avg


def test_1():
    classes = [[1, 2], [3, 5], [2, 2]]
    assert abs(Solution().maxAverageRatio(classes, 2) - 0.7833333333333333) < 1E-5


def test_2():
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    assert abs(Solution().maxAverageRatio(classes, 4) - 0.5348484848484849) < 1E-5


if __name__ == '__main__':
    test_1()
    test_2()
