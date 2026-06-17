class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_available = {}
        for i in range(len(nums)):
            needed_val = target - nums[i]
            if needed_val in num_available:
                return [num_available[needed_val],i]
            else:
                num_available[nums[i]]=i
        return []  