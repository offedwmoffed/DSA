class Solution:
    def longestCommonPrefix(self, strs:list):
        longest_prefix =""
        first_word = strs[0]
        i = 0
        for char in first_word:
            for word in strs:
                if i >= len(word):
                    return longest_prefix
                elif word[i]!=char and len(longest_prefix) == 0:
                    return ""
                elif word[i] != char and len(longest_prefix)>=1:
                    return longest_prefix
            else:
                longest_prefix += char
                i += 1
        return longest_prefix
            
