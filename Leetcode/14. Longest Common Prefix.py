'''
Question 14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]

