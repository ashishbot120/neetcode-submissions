class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeat = {}
        for i in nums:
            repeat[i]=1+repeat.get(i,0)
        
        freq =[[] for j in range(len(nums)+1)]

        for n, c in repeat.items():
            freq[c].append(n)

        res=[]
        for l in range(len(freq)-1,0,-1):
            for n in freq[l]:
                res.append(n)

                if len(res)==k:
                    return res
            