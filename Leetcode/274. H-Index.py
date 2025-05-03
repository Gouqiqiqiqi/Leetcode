'''
Question:

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

The h-index is defined as the maximum value of h such that the given researcher has published at least h papers, 
which have each been cited at least h times.
'''


'''
Understand the question:

citations = [3, 0, 6, 1, 5]
Try all possible values of h from 0 to 5 (because there are 5 papers), and count how many papers have at least that many citations:

| h | Papers with ≥ h citations     | Count |
|---|-------------------------------|---------|
| 0 | 6, 5, 3, 1, 0                 | 5 ✅    |
| 1 | 6, 5, 3, 1                    | 4 ✅    |
| 2 | 6, 5, 3                       | 3 ✅    |
| 3 | 6, 5, 3                       | 3 ✅    |
| 4 | 6, 5                          | 2 ❌    |

Now, find the largest h such that:

number of papers with ≥ h citations ≥ h
For h = 3, there are 3 papers with ≥ 3 citations → ✅

For h = 4, only 2 papers with ≥ 4 → ❌

So the h-index is 3.

'''

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        for i in range(n):
            if citations[i] < i + 1:
                return i
        return n

citations = [3, 0, 6, 1, 5]
c = Solution()
print(c.hIndex(citations)) # Output: 3

'''
Let's break down the variables:

If list = [3, 0, 6, 1, 5]
list.sort(reverse=True) = [6, 5, 3, 1, 0]
n = len(citations) = 5
i = [0, 1, 2, 3, 4]

citations[i] is the number of citations for the i-th paper.
i + 1 is the number of papers we've seen so far, because we start from 0, therefore we need to add 1.

| i | citations [i] | i + 1 | Check: citations [i] < i + 1 | Result         |
| - | ------------- | ----- | ---------------------------- | -------------- |
| 0 | 6             | 1     | 6 < 1 → **False**            | Keep going     |
| 1 | 5             | 2     | 5 < 2 → **False**            | Keep going     |
| 2 | 3             | 3     | 3 < 3 → **False**            | Keep going     |
| 3 | 1             | 4     | 1 < 4 → **True**             | **Return 3** ✅ |
| 4 | 0             | 5     | not reached                  | Loop exited    |

'''

'''
One key sentence in the code is:
if citations[i] < i + 1:
instead of 
if citations[i] < i:
This is because python is 0-indexed, and we need to compare the number of papers with the number of citations.
When index i is 0, it means we have seen 1 paper, and we need to compare it with the number of citations.
'''

'''
Another key sentence in the code is:
                return i
        return n

This means the h index = i, if the condition is met. If no i satisfies citations[i] < i + 1, return n.
This means all papers have at least n citations, so the h index is n, or h index = n = i + 1.
'''