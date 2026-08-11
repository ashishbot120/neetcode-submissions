class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
     #   n = len(nums)
        for i in range(len(nums)):
            total += nums[i]
        left=0
        for i,num in enumerate(nums):
            right=total-left-num
            if right==left:
                return i
            left += num
        return -1