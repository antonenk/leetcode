#!/usr/bin/python3

# https://leetcode.com/problems/unique-paths-iii/description/

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        starting_square = None
        ending_square = None
        obstacles = set()

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    starting_square = (y, x)
                elif grid[y][x] == 2:
                    ending_square = (y, x)
                elif grid[y][x] == -1:
                    obstacles.add((y, x))

        path_len = height * width - len(obstacles)
        paths = [[starting_square]]

        for step_number in range(1, path_len):
            new_paths = []
            for path in paths:
                last_y, last_x = path[-1]
                next_steps = []
                if last_y > 0:
                    next_steps.append((last_y - 1, last_x))
                if last_y < height - 1:
                    next_steps.append((last_y + 1, last_x))
                if last_x > 0:
                    next_steps.append((last_y, last_x - 1))
                if last_x < width - 1:
                    next_steps.append((last_y, last_x + 1))

                for next_step in next_steps:
                    if next_step in path:
                        continue
                    if next_step in obstacles:
                        continue
                    if step_number < (path_len - 1) and next_step == ending_square:
                        continue
                    new_path = path.copy()
                    new_path.append(next_step)
                    new_paths.append(new_path)

            paths = new_paths

        return len(paths)


def test_1():
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    assert Solution().uniquePathsIII(grid) == 2


def test_2():
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    assert Solution().uniquePathsIII(grid) == 4


if __name__ == '__main__':
    test_1()
    test_2()
