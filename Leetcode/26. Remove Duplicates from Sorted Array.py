'''
Question 26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''


'''
Note:
For i in range(len(nums)):
    print(nums[i])
    # This will print all elements of nums

For i in range(8, len(nums)):
    print(nums[i])
    # This will print elements of nums starting from index 8 to the end
'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums: #Optional line, to include if you want the solution to always work even if the list is empty *
            return 0
        k = 1   # Start from 1 instead of 0 because the first element is always unique
        #nums.sort() If the list is not sorted, use this line to sort it first, otherwise the solution will not work *
        for i in range(1, len(nums)): #Start a loop from the second element (index 1) to the end, again, because the first element is always unique
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        #del nums[k:] # Optional: Remove the duplicates from the list
        return k


nums = [0,0,1,1,2,2,3,3,4]
solution = Solution()
k = solution.removeDuplicates(nums)
    
print(k)          # Output: 5
print(nums[:k])   # Output: [0, 1, 2, 3, 4]

'''
Using 
if nums[i] != nums[k-1]: 
is better than 
if nums[i] != nums[i-1]:

✅ Method 1:
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        # nums.sort()  # Not needed if nums is already sorted
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k
Compares nums[i] with nums[k-1]

This is a more robust method because it always compares the current number to the last unique number (which is at index k-1)

Safer in scenarios where the list might not be fully sorted

✅ Method 2:
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        # nums.sort()  # Not needed if nums is already sorted
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: 
                nums[k] = nums[i]
                k += 1
        return k
Compares nums[i] with nums[i-1]

Relies entirely on the fact that the array is already sorted, because only then are duplicates adjacent

This method is less robust in scenarios where the list might not be fully sorted

'''

'''
Detailed Explanation:

nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]
k = 1
i = 1

🧠 Iteration by Iteration:

i = 1, k = 1:
Compare: nums[1] = 0 vs nums[k-1] = nums[0] = 0

Equal → Duplicate → Do nothing

k = 1

i = 2, k = 1:
Compare: nums[2] = 1 vs nums[0] = 0

Not equal → New unique element

Assign: nums[1] = 1

Increment k = 2

nums becomes: [0, 1, 1, 1, 2, 2, 3, 3, 4]

i = 3, k = 2:
Compare: nums[3] = 1 vs nums[1] = 1

Equal → Duplicate → Do nothing

k = 2

i = 4, k = 2:
Compare: nums[4] = 2 vs nums[1] = 1

Not equal → New unique element

Assign: nums[2] = 2

Increment k = 3

nums becomes: [0, 1, 2, 1, 2, 2, 3, 3, 4]

i = 5, k = 3:
Compare: nums[5] = 2 vs nums[2] = 2

Equal → Duplicate → Do nothing

k = 3

i = 6, k = 3:
Compare: nums[6] = 3 vs nums[2] = 2

Not equal → New unique element

Assign: nums[3] = 3

Increment k = 4

nums becomes: [0, 1, 2, 3, 2, 2, 3, 3, 4]

i = 7, k = 4:
Compare: nums[7] = 3 vs nums[3] = 3

Equal → Duplicate → Do nothing

k = 4

i = 8, k = 4:
Compare: nums[8] = 4 vs nums[3] = 3

Not equal → New unique element

Assign: nums[4] = 4

Increment k = 5

nums becomes: [0, 1, 2, 3, 4, 2, 3, 3, 4]

✅ Final Result:
k = 5 → Number of unique elements

First k elements of nums = [0, 1, 2, 3, 4]

Rest of the array doesn't matter

📌 Summary:
This method works by:

Keeping track of the last unique element via nums[k-1]

Ensuring that any new unique number gets copied to the correct position (nums[k])

'''