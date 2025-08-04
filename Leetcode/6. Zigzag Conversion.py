'''
6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only 1 row or string is shorter than numRows
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Creates a list of empty strings, one for each row of the zigzag pattern.
        rows = [''] * numRows
        
        # Track current row and direction
        current_row = 0
        going_down = False
        
        # Place each character in the appropriate row
        for char in s:
            rows[current_row] += char
            
            # Change direction at top and bottom rows
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to next row
            current_row += 1 if going_down else -1
        
        # Join all rows together
        return ''.join(rows)



''''
Code Explanation:

rows = [''] * numRows

If numRows = 3, this creates a list with 3 empty strings: ['', '', ''], 
in which each string will hold characters for that row in the zigzag pattern.

I.e.
s = "HELLO"
numRows = 3
Initial state:

rows = ['', '', '']
current_row = 0
moving_down = False
We go through each character in "HELLO" and update the appropriate row:

🔁 1st character 'H':
current_row = 0

rows[0] += 'H' → rows = ['H', '', '']

🔁 2nd character 'E':
Direction changes → current_row = 1

rows[1] += 'E' → rows = ['H', 'E', '']

🔁 3rd character 'L':
current_row = 2

rows[2] += 'L' → rows = ['H', 'E', 'L']

🔁 4th character 'L':
Direction changes (bottom reached) → now going up

current_row = 1

rows[1] += 'L' → rows = ['H', 'EL', 'L']

🔁 5th character 'O':
current_row = 0

rows[0] += 'O' → rows = ['HO', 'EL', 'L']

✅ Final State of rows:

rows = ['HO', 'EL', 'L']
If we join all rows:


''.join(rows) → 'HOELL'
'''
