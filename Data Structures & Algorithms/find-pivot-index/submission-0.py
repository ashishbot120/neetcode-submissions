class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left=0
        for i,num in enumerate(nums):
            right=total_sum-left-num
            if right==left:
                return i
            left += num
        return -1