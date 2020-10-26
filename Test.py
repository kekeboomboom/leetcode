from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number


if __name__ == '__main__':
    result=Solution().singleNumber([1,3,5,5,1])
    print(result)
