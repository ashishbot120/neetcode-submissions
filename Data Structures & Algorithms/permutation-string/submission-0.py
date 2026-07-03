class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False 
        need = {} 
        window = {} 
        for ch in s1: 
            need[ch] = need.get(ch,0)+1 
        for i in range(len(s1)): 
             window[s2[i]] = window.get(s2[i],0)+1 
        if need == window: 
            return True 
        left = 0 
        for right in range(len(s1),len(s2)): 
            window[s2[right]] = window.get(s2[right],0)+1 
            window[s2[left]] -= 1 
            if window[s2[left]] == 0: 
                del window[s2[left]] 
            left += 1 
            if need == window: 
                return True 
        return False