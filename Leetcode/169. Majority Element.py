'''
Question:

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

'''
#Boyer–Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Boyer-Moore Voting Algorithm
        """
        count = 0 #Assign 0 to count
        candidate = None #Assign None to candidate

        for i in nums:
            if count == 0:  #Check if count is 0
                candidate = i   #Assign i to candidate
            count += (1 if candidate == i else -1) #Check if i is equal to candidate, if yes, increment count by 1, else decrement count by 1

        return candidate
    
nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums))  # Output: 2

'''
Breakdown:

How It Works
Initialization:

Start with count = 0 and candidate = None.

Iteration:

For each element i in the list nums:

If count is 0, set candidate = i. This means that when our count drops to zero, we start considering a new candidate.

Increase the count by 1 if the current element i equals the candidate; otherwise, decrease count by 1.

Conclusion:

After iterating through the list, the variable candidate holds the majority element if one exists (assuming the input always has a valid majority element).



Step-by-Step Execution

nums = [2, 2, 1, 1, 1, 2, 2]

Initial state:

count = 0

candidate = None

Iteration 1: (Element = 2)

Since count == 0, set candidate = 2.

Check: Is current element (2) equal to candidate (2)? Yes.

Update count: count = 0 + 1 → count = 1

State: candidate = 2, count = 1

Iteration 2: (Element = 2)

Current element is 2 and candidate is 2.

They match, so increment count: count = 1 + 1 → count = 2

State: candidate = 2, count = 2

Iteration 3: (Element = 1)

Current element is 1 and candidate is 2, so they do not match.

Decrement count: count = 2 - 1 → count = 1

State: candidate = 2, count = 1

Iteration 4: (Element = 1)

Current element is 1, candidate is still 2.

They do not match, so decrement count: count = 1 - 1 → count = 0

State: candidate = 2, count = 0

Iteration 5: (Element = 1)

Now count == 0, so we change candidate: set candidate = 1.

Check: Current element is 1 and candidate is 1 (immediate match).

Increment count: count = 0 + 1 → count = 1

State: candidate = 1, count = 1

Iteration 6: (Element = 2)

Current element is 2 and candidate is 1.

They do not match, so decrement count: count = 1 - 1 → count = 0

State: candidate = 1, count = 0

Iteration 7: (Element = 2)

Since count == 0, update candidate: set candidate = 2.

Check: Current element 2 matches the new candidate 2.

Increment count: count = 0 + 1 → count = 1

Final State: candidate = 2, count = 1


'''


'''

= vs ==:
= is used for assignment, while == is used for comparison.



'''
