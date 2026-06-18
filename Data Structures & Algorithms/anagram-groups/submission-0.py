class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = {}

        for count in strs:

            char_count = [0] * 26

            for ch in count:
                char_count[ord(ch)-ord('a')]+=1
            
            char_count_tuple=tuple(char_count)

            if char_count_tuple in group_anagram:
                group_anagram[char_count_tuple].append(count)
            else:
                group_anagram[char_count_tuple]=[count]

        return list(group_anagram.values())