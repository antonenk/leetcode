#!/usr/bin/python3

# https://leetcode.com/problems/count-the-number-of-complete-components/description/
# beats 100% runtime / 93% mem

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        componentOfVertex = [-1] * n
        edgesInComponent: list[int] = []
        componentIds: set[int] = set()
        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]
            if componentOfVertex[vertex1] == -1:
                if componentOfVertex[vertex2] == -1:
                    componentId = len(edgesInComponent)
                    edgesInComponent.append(1)
                    componentIds.add(componentId)
                    componentOfVertex[vertex1] = componentId
                    componentOfVertex[vertex2] = componentId
                else:
                    componentId = componentOfVertex[vertex2]
                    componentOfVertex[vertex1] = componentId
                    edgesInComponent[componentId] += 1
            else:
                if componentOfVertex[vertex2] == -1:
                    componentId = componentOfVertex[vertex1]
                    componentOfVertex[vertex2] = componentId
                    edgesInComponent[componentId] += 1
                else:
                    componentId = componentOfVertex[vertex1]
                    anotherComponentId = componentOfVertex[vertex2]
                    if componentId != anotherComponentId:
                        componentIds.remove(anotherComponentId)
                        edgesInComponent[componentId] += edgesInComponent[anotherComponentId] + 1
                        for i in range(n):
                            if componentOfVertex[i] == anotherComponentId:
                                componentOfVertex[i] = componentId
                    else:
                        edgesInComponent[componentId] += 1

        completeComponentsCount = 0
        verticesInComponent = [0] * len(edgesInComponent)
        for componentId in componentOfVertex:
            if componentId == -1:
                completeComponentsCount += 1
            else:
                verticesInComponent[componentId] += 1

        for componentId in componentIds:
            maxEdges = verticesInComponent[componentId] * (verticesInComponent[componentId] - 1) // 2
            if edgesInComponent[componentId] == maxEdges:
                completeComponentsCount += 1

        return completeComponentsCount


def test_1():
    assert Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]) == 3


def test_2():
    assert Solution().countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]) == 1


if __name__ == '__main__':
    test_1()
    test_2()
