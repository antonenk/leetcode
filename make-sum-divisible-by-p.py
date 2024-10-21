class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        sumOfNums = 0
        for num in nums:
            sumOfNums += num

        module = sumOfNums % p
        if module == 0:
            return 0

        for subArrayLen in range(1, len(nums) - 1):
            for i in range(len(nums) - subArrayLen + 1):
                subArraySum = 0
                for j in range(subArrayLen):
                    subArraySum += nums[i+j]
                if subArraySum % p == module:
                    return subArrayLen

        return -1


def test_1():
    nums = [3, 1, 4, 2]
    p = 6
    assert Solution().minSubarray(nums, p) == 1


def test_2():
    nums = [6, 3, 5, 2]
    p = 9
    assert Solution().minSubarray(nums, p) == 2


def test_3():
    nums = [1, 2, 3]
    p = 3
    assert Solution().minSubarray(nums, p) == 0


def test_no_subarray():
    nums = [1, 2, 3]
    p = 10
    assert Solution().minSubarray(nums, p) == -1
