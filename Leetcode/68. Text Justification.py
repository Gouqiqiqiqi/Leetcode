'''
Question 68: Text Justification
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

'''

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        
        while i < len(words):
            # Step 1: Pack words for current line
            line_words = [words[i]]
            line_length = len(words[i])
            i += 1
            
            # Add as many words as possible to current line
            while i < len(words) and line_length + 1 + len(words[i]) <= maxWidth:
                line_words.append(words[i])
                line_length += 1 + len(words[i])  # +1 for minimum space
                i += 1
            
            # Step 2: Format the line (inline)
            num_words = len(line_words)
            
            # Last line or single word - left justify
            if i == len(words) or num_words == 1:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # Full justify - distribute spaces evenly
                total_chars = sum(len(word) for word in line_words)
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1
                
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                line = ''
                for j, word in enumerate(line_words):
                    line += word
                    if j < gaps:
                        # Add base spaces + 1 extra for first 'extra_spaces' gaps
                        line += ' ' * (spaces_per_gap + (1 if j < extra_spaces else 0))
            
            result.append(line)
        
        return result