class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                area = height * (i-index)
                maxarea = max(maxarea,area)
                start = index
            stack.append((start,h))
        n = len(heights)
        while stack:
            index,height =stack.pop()
            area = height *(n-index)
            maxarea = max(maxarea,area)
        return maxarea
