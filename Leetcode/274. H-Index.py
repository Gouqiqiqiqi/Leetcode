'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

The h-index is defined as the maximum value of h such that the given researcher has published at least h papers, 
which have each been cited at least h times.
'''


'''
Understand the question:

citations = [3, 0, 6, 1, 5]
Try all possible values of h from 0 to 5 (because there are 5 papers), and count how many papers have at least that many citations:

h	Number of papers with ≥ h citations
0	5 (all)
1	4 (3,6,1,5)
2	4 (3,6,5,1)
3	3 (3,6,5)
4	2 (6,5)
5	2 (6,5)
6	1 (6)

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
Explain the code:

When the list is sorted descending, you're going through the researcher's most-cited papers first.

At each position i (starting from 0):

i + 1 is how many papers we've seen so far.

citations[i] is the number of citations for the current paper.

So we're asking:

“Does the researcher have at least i + 1 papers with i + 1 or more citations?”

As soon as citations[i] < i + 1, that means:

“We’ve gone too far — there aren’t i + 1 papers with that many citations.”

So the h-index is exactly i at that point.

✏️ Example: citations = [6, 5, 3, 1, 0]
Let’s walk through it:


i	citations[i]	i + 1	Compare	Result
0	6	1	6 ≥ 1 → OK	continue
1	5	2	5 ≥ 2 → OK	continue
2	3	3	3 ≥ 3 → OK	continue
3	1	4	1 < 4 → Stop!	return 3
➡️ So the h-index is 3 (3 papers with at least 3 citations).

✅ Summary:
We compare with i + 1 because:

i + 1 means: this is the (i+1)-th most cited paper.

To have h-index = h, you need h papers with at least h citations.

As soon as citations[i] < i + 1, that h-index is not achievable — so return i.
'''