#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 49% runtime / 41% mem


class UndergroundSystem:

    def __init__(self):
        self.activeTravels = {}
        self.completedTravels = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.activeTravels[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.activeTravels[id]
        if startStation not in self.completedTravels:
            self.completedTravels[startStation] = {}

        if stationName not in self.completedTravels[startStation]:
            self.completedTravels[startStation][stationName] = (t - startTime, 1)
        else:
            totalTime, totalCount = self.completedTravels[startStation][stationName]
            self.completedTravels[startStation][stationName] = (totalTime + t - startTime, totalCount + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalCount = self.completedTravels[startStation][endStation]
        return totalTime / totalCount


def test_1():
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    assert undergroundSystem.getAverageTime("Paradise", "Cambridge") == 14 / 1
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == (10 + 12) / 2
    undergroundSystem.checkIn(10, "Leyton", 24)
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == (10 + 12) / 2
    undergroundSystem.checkOut(10, "Waterloo", 38)
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == (10 + 12 + 14) / 3


def test_2():
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(10, "Leyton", 3)
    undergroundSystem.checkOut(10, "Paradise", 8)
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 5 / 1
    undergroundSystem.checkIn(5, "Leyton", 10)
    undergroundSystem.checkOut(5, "Paradise", 16)
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == (5 + 6) / 2
    undergroundSystem.checkIn(2, "Leyton", 21)
    undergroundSystem.checkOut(2, "Paradise", 30)
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == (5 + 6 + 9) / 3


if __name__ == '__main__':
    test_1()
    test_2()
