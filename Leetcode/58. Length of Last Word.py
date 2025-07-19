'''
Question 58: Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.


'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
    

'''
Notes to solution:

len(): This function returns the number of characters 

i.e. len("Hello") returns 5

rstrip(): This method removes trailing whitespace only from the string.

i.e. "   Hello   ".rstrip() returns "   Hello"

lstrip(): This method removes leading whitespace only from the string.
i.e. "   Hello   ".lstrip() returns "Hello   "

strip(): This method removes both leading and trailing whitespace from the string.
i.e. "   Hello   ".strip() returns "Hello"

split(): This method splits the string into a list of words based on whitespace.
i.e. "Hello World".split() returns ['Hello', 'World']

With a specific separator (split(separator)):
Splits the string wherever the specified separator appears.
i.e. separate only strings by commas:
s = "apple,banana,,;cherry"
print(s.split(','))  # Output: ['apple', 'banana', '', ';cherry']
i.e separate only strings by semicolons:
s = "apple,banana,,;cherry"
print(s.split(';'))  # Output: ['apple,banana,,', 'cherry']

Optional argument — maxsplit:
You can limit the number of splits:
s = "one two three four"
print(s.split(maxsplit=2))  # Output: ['one', 'two', 'three four']



So the [-1] in the solution accesses the last element of a list.

'''