'''
Question 151: Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()

        word.reverse()

        return ' '.join(word) # Remember to join the words with a single space
    

'''
Original string s	'the sky is blue'
After s.split()	['the', 'sky', 'is', 'blue']
After .reverse()	['blue', 'is', 'sky', 'the']
After ' '.join()	'blue is sky the'
'''


'''
Some additional notes:

.reverse() modifies the list in place, reversing the order of the elements.

i.e. word = ['the', 'sky', 'is', 'blue']
     word.reverse()
     # Now word is ['blue', 'is', 'sky', 'the']


why s.split.reverse() will not work?
You're trying to chain two method calls:

s.split() → gives you ['the', 'sky', 'is', 'blue']

.reverse() → modifies that list in-place and returns None

So the whole expression becomes:
s.split().reverse()  # → None

# This is because reverse() modifies the list in place and returns None.
# So you end up with:
# s.split().reverse()  # → None


🔍 Why you can't do s.split().reverse()
Because .reverse() does not return the reversed list — it just returns None.
Therefore you need a variable word to hold the result of s.split() before calling .reverse().

'''