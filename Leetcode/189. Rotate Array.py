'''
Question: 189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''


#Solution:

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums) 
        k %= n 

        # Helper function to reverse a subarray in-place
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the whole array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the rest
        reverse(k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]


'''
Notes:

1. k %= n is short for k = k % n, which gives the remainder of k divided by n.
i.e. 
nums = [1, 2, 3, 4, 5]
n = len(nums) = 5
k = 8
k % n = 8 % 5 = 3 # Where 3 is the reminder of 8 divided by 5.
'''