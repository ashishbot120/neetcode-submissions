class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stor_set = set()
        left = 0
        count = 0
        for right in range(len(s)):
            while s[right] in stor_set:
                stor_set.remove(s[left])
                left += 1
            stor_set.add(s[right])
            count= max(count , right - left +1)
        return count