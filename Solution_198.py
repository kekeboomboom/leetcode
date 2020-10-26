from typing import List


class Solution_198:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            prev = nums[0]
            cur = max(prev, nums[2])
            for i in range(2, length):
                cur, prev = max(prev + nums[i], cur), cur
            return cur


if __name__ == '__main__':
    # Solution_198().rob([1, 2, 3, 1])

    print(Solution_198().rob2([2, 7, 9, 3, 1]))
