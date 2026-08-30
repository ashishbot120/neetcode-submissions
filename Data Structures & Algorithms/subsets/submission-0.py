class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i,subset):
            if i == len(nums):
                result.append(subset.copy())
                return
            #dont take num
            backtrack(i+1,subset)
            #take num
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
        backtrack(0,[])
        return result