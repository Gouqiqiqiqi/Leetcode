'''
Question 28: Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''
#Solution 1: Brute Force Approach
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1

#Solution 2: Knuth–Morris–Pratt KMP algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build the longest prefix suffix (LPS) array
        lps = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
            lps[i] = j

        # Search for the needle in the haystack
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1

        return -1