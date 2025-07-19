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

        for i in range(len(strs[0])):   # Loop through each character of the first word ("flower")
            char = strs[0][i]           # Take the current character from the first word

            for word in strs[1:]:       # Loop through all the other words (from 2nd to last)
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]  # If mismatch found, return prefix up to index i

        return strs[0]  # If no mismatch found, return the entire first string, i.e. the longest common prefix is the first string itself

'''
Note:

This problem uses a double loop to compare characters of the first string with all other strings.

First loop (outer loop): Pick letter-by-letter from the first word.

Second loop (inner loop): Check if other words agree at that letter's position.

If a mismatch is found, return the prefix up to that point.

'''


'''
if i >= len(word) is a very important check to avoid index errors when comparing characters in shorter strings.

Imagine This Example:
["cat", "car", "ca"]
First word: "cat"

Second word: "car"

Third word: "ca"

Now, step-by-step:

At i = 0 (first letter):
"cat"[0] → 'c'
"car"[0] → 'c'
"ca"[0] → 'c'
✅ All same.

At i = 1 (second letter):
"cat"[1] → 'a'
"car"[1] → 'a'
"ca"[1] → 'a'
✅ All same.

At i = 2 (third letter):
"cat"[2] → 't'
"car"[2] → 'r'
"ca" → Does index 2 exist?
❌ No! "ca" is only 2 letters long (indexes 0 and 1).


If you don't include:
if i >= len(word)
Your code would crash (IndexError), because you're asking:
word[2]
for a word that has only 2 letters.
'''