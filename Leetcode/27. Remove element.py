'''
Question:

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

Return k
'''

'''
Approach:
1. Initialize a variable k to 0, which will keep track of the number of elements not equal to val.
2. Iterate through the array nums using a for loop.
3. For each element in nums, check if it is not equal to val.
4. If the element is not equal to val, assign it to nums[k] and increment k by 1.
5. After the loop, k will contain the number of elements not equal to val.
6. Return k.
'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0 # Start from 0 because we don't know how many elements are not equal to val
        # Iterate through the array nums
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
    

nums = [3,2,2,3,3]
val = 2
sol = Solution()
count = sol.removeElement(nums, val)  # Output: 3
print(count)  # Print the number of elements not equal to val


'''
Step-by-step:
Start with:
nums = [3, 2, 2, 3, 3]
val = 2
k = 0
------------------------------------------------------------

Iteration 1 (i=0):
nums[0] = 3, which is not 2 → valid
Now k = 0, i = 0, so we copy nums[0] to nums[0]
Copy nums[0] to nums[0] → stays the same

k = 1

------------------------------------------------------------

Iteration 2 (i=1):
Now k = 1, i = 1
nums[1] = 2 → skip (it's equal to val)

------------------------------------------------------------

Iteration 3 (i=2):
Now k = 1, i = 2
nums[2] = 2 → skip

------------------------------------------------------------

Iteration 4 (i=3):
Now k = 1, i = 3
nums[3] = 3 → valid

Copy to nums[1]: nums[1] = 3

nums = [3, 3, 2, 3, 3]

k = 2
------------------------------------------------------------

Iteration 5 (i=4):
Now k = 2, i = 4
nums[4] = 3 → valid

Copy to nums[2]: nums[2] = 3

nums = [3, 3, 3, 3, 3]

k = 3
------------------------------------------------------------
As you can see, the first 3 elements of nums are now the elements that are not equal to val (2), but the list is not trimmed, instead,
2 have been replaced by 3. The final list is [3, 3, 3] followed by irrelevant elements.

'''

'''
There are other derivation of the same problem, such as:
Question 1:
Counting the number of occurrences of val in the array

Solution:
def countOccurrences(nums, val):
    count = 0
    for num in nums:
        if num == val:
            count += 1
    return count

nums = [3,2,2,3,3]
val = 2
occurrences = countOccurrences(nums, val)
print(occurrences)

Or just

nums = [3,2,2,3,3]
val = 2
occurrences_count = nums.count(val) # This will give the number of occurrences of val in nums
print(occurrences_count)


Question 2:
Find value of k in the array nums, remove all occurrences of val in nums in-place, return a new array with the remaining elements.

class Solution:
    def removeElementAndReturnArray(self, nums: list[int], val: int) -> int:
        count = 0  # Number of elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        # Trim the original list to only include the first k elements
        del nums[count:]
        return count  

# Example usage
nums = [3, 2, 2, 3, 3]
val = 2
sol = Solution()
k = sol.removeElementAndReturnArray(nums, val)

print(k)
print(nums)

'''


'''
Special notes:

In this question, using:

for i in nums:
    if i != val:
        nums[k] = i
        k += 1
will not work!, beacuse the for loop will iterate over the original list nums, and if you modify nums while iterating over it, 
it will lead to unexpected behavior.
This is because the for loop will not be aware of the changes made to nums, and it will continue to iterate over the original list, 
which may result in skipping elements or accessing out-of-bounds indices. Therefore, it is essential to avoid modifying the list while iterating over it.

❌ Broken version:

nums = [3, 2, 2, 3]
val = 3

for i in nums:  # i = 3, then 2, then 2, then 3
    if nums[i] != val:  # nums[3]?? nums[2]?? unpredictable!
i = 3 → you're trying nums[3] — that works by chance.

But if i = 10? You get an IndexError.

You are confusing the element (i) with an index.

'''