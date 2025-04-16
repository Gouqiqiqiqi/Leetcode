'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    k = 2  # write pointer, start from 2 since the first two elements are always allowed
    for i in range(2, len(nums)):  # read pointer
        # Only write if the current number is not equal to the number two places before
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return k


nums = [1,1,1,2,2,3]
k = removeDuplicates(nums)  # Output: 5, nums = [1,1,2,2,3,_] (the value of _ does not matter)
print(k)
print(nums)


'''
Reflection:
This is simiar to Question 26, but with a twist.
The twist is that we can have at most two duplicates of each number.
The key difference is 
:if nums[i] != nums[k - 2]: 
rather than 
:nums[i] != nums[i - 1]:


why it is nums[k - 2] rather than ums[i - 1]?
Because we are allowed to have at most two duplicates of each number.

why it is nums[k - 2] rather than ums[i - 2]?
If you used nums[i - 2], you might:
Let in too many duplicates (because it checks earlier input, not written result).
Skip valid entries if the first few were already skipped.

'''


'''
Step-by-step CORRECT: if nums[i] != nums[k - 2]: 
nums = [1, 1, 1, 2, 2, 3]

Iteriation 1: Start: i = 2, k = 2
i = 2
nums[i] = 1

nums[k - 2] = nums[0] = 1

1 == 1 → ❌ don't write it

k = 2

nums = [1, 1, 1, 2, 2, 3] (unchanged)

Iteriation 2: Start: i = 3, k = 2
i = 3
nums[i] = 2

nums[k - 2] = nums[0] = 1

2 != 1 → ✅ write it to nums[k] = nums[3]

nums = [1, 1, 2, 2, 2, 3]

k = 3

Iteriation 3: Start: i = 4, k = 3
i = 4
nums[i] = 2

nums[k - 2] = nums[1] = 1

2 != 1 → ✅ write it to nums[k] = nums[4]

nums = [1, 1, 2, 2, 2, 3] (still fine)

k = 4

Iteriation 4: Start: i = 5, k = 4
i = 5
nums[i] = 3

nums[k - 2] = nums[2] = 2

3 != 2 → ✅ write it to nums[k] = nums[5]

nums = [1, 1, 2, 2, 3, 3]

k = 5
'''

'''
Step-by-step WRONG: if nums[i] != nums[i - 2]: 
nums = [1, 1, 1, 2, 2, 3]

Iteriation 1: Start: i = 2, k = 2
nums[i] = 1

nums[i - 2] = nums[0] = 1

1 == 1 → ❌ don't write

nums = [1, 1, 2, 2, 3, 3]

k = 2

Iteriation 2: Start: i = 3, k = 2
nums[i] = 2

nums[i - 2] = nums[1] = 1

2 != 1 → ✅ write to nums[k] = nums[3]

nums = [1, 1, 2, 2, 2, 3]

k = 3

Iteriation 3: Start: i = 4, k = 3
nums[i] = 2

nums[i - 2] = nums[2] = 2

2 == 2 → ❌ skip

k = 3 (unchanged)

Iteriation 4: Start: i = 5, k = 3
nums[i] = 3

nums[i - 2] = nums[3] = 2

3 != 2 → ✅ write to nums[k] = nums[5]

nums = [1, 1, 3, 2, 2, 3]

k = 4

This causes wrong orders of the numbers.
nums = [1, 1, 3, 2, 2, 3]
correct answer is nums = [1, 1, 2, 2, 3, 3] 
'''