from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        doop = 0
        temp = -1
        k = 0
        for i in nums:
            if i == temp:
                if doop > 0:
                    nums.remove(i)
                    doop =0
                else:
                    doop += 1
                    temp = i
                    k += 1
        return k
nums = [1, 1, 1, 2, 2, 3]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)
