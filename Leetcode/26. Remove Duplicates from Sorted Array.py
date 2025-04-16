'''
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
Step-by-step:

🌀 Iteration 1: Start: i = 1, k = 1
            if nums[i] != nums[k-1]:
nums[1] = 0, nums[0] = 0 → Duplicate, so skip

--------------------------------------------------------

🌀 Iteration 2: Start: i = 2, k = 1
nums[2] = 1, nums[1] = 0 → Different, so it's unique

                nums[k] = nums[i]  # nums[1] = 1
                k += 1             # k = 2
nums = [0, 1, 1, 1, 2, 2, 3, 3, 4]
We placed 1 at index 1.

---------------------------------------------------------

🌀 Iteration 3: Start: i = 3, k = 2
nums[3] = 1, nums[2] = 1 → Duplicate → skip

----------------------------------------------------------

🌀 Iteration 4: Start: i = 4, k = 2
nums[4] = 1, nums[3] = 1 → Duplicate → skip

----------------------------------------------------------

🌀 Iteration 5: Start: i = 5, k = 2
nums[5] = 2, nums[4] = 1 → Different → unique

                nums[k] = nums[i]  # nums[2] = 2
                k += 1             # k = 3
nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]

------------------------------------------------------------   

🌀 Iteration 6: Start: i = 6, k = 3
nums[6] = 2, nums[5] = 2 → Duplicate → skip

------------------------------------------------------------

🌀 Iteration 7: Start: i = 7, k = 3
nums[7] = 3, nums[6] = 2 → Unique

                nums[k] = nums[i]  # nums[3] = 3
                k += 1             # k = 4
nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]

------------------------------------------------------------

🌀 Iteration 8: Start: i = 8, k = 4
nums[8] = 3, nums[7] = 3 → Duplicate → skip

------------------------------------------------------------

🌀 Iteration 9: Start: i = 9, k = 4
nums[9] = 4, nums[8] = 3 → Unique

                nums[k] = nums[i]  # nums[4] = 4
                k += 1             # k = 5
nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

final result:
k = 5
nums[:k] = [0, 1, 2, 3, 4]
'''