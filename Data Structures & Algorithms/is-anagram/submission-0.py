class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        anagram = {}
        for char in s:
            anagram[char] = anagram.get(char,0)+1

        for char in t:
            if char not in anagram:
                return False
            
            anagram[char]-=1

            if anagram[char]<0:
                return False

        
        return True