class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob(nums,start,end):
            prev1 = 0
            prev2 = 0
            for i in range(start,end+1):
                robcurrent = nums[i] + prev1
                skipcurrent = prev2
                curr = max(robcurrent,skipcurrent)
                prev1 = prev2
                prev2 = curr
            return prev2
        case1 = rob(nums,0,n-2)
        case2 = rob(nums,1,n-1)
        return max(case1,case2)