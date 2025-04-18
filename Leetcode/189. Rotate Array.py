'''
Question: 189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''


#Solution:

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        #if k < 0: #if k is negative, we can convert it to a positive rotation by adding n to k.
            #k = n + k
            
        nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]


'''
Explanation:

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums) 
        k %= n #This is neccessary for the function to work. Because rotating an array of length n by n or more times is the same as rotating it by k % n times
        nums[:] = nums[-k:] + nums[:-k]

        
#For example:
[1, 2, 3, 4, 5, 6, 7]
#Since rotating by the length of the array (or a multiple of it) results in the same array, we do:
n = len(nums)  # 7
k = k % n  # 8 % 7 = 1
#So rotating right by 8 steps is the same as rotating by 1 step.
#The output will be:
#[7, 1, 2, 3, 4, 5, 6]

#Meanwhile, if k is smaller than n...
i.e  k = 2, n = 7
#Then we can just rotate the array by 2 steps.
#The output will be:
#[6, 7, 1, 2, 3, 4, 5]
'''

'''
[1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums) = 7
nums[:] = nums[-k:] + nums[:-k]
nums[:] = #This is used to modify the original list in place.

nums[-k:] = [5, 6, 7] #This gets the last k elements of the array.
nums[:-k] = [1, 2, 3, 4] #This gets the first n-k elements of the array.

nums[-k:] is equal to nums[len(nums)-k:] which is equal to nums[7-3:] = nums[4:] = [5, 6, 7]
nums[:-k] is equal to nums[:len(nums)-k] which is equal to nums[:7-3] = nums[:4] = [1, 2, 3, 4]
'''











'''
Notes:

1. k %= n is short for k = k % n, which gives the remainder of k divided by n.
i.e. 
nums = [1, 2, 3, 4, 5]
n = len(nums) = 5
k = 8
k % n = 8 % 5 = 3 # Where 3 is the reminder of 8 divided by 5.


Some maths basics:
3 ÷ 7 = 0 remainder 3 (since 7 × 0 = 0, and 3 − 0 = 3)
7 ÷ 3 = 2 remainder 1 (since 3 × 2 = 6, and 7 − 6 = 1)
'''

