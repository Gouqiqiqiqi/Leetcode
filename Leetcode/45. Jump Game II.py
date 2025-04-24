'''
Problem: Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Approach: Greedy algorithm that minimizes the number of jumps by always choosing the position 
that allows you to go the farthest in the next jump.
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        # Number of jumps needed to reach the end
        jumps = 0
        # Farthest position reachable with the current number of jumps
        current_end = 0
        # Farthest position reachable from any position seen so far
        farthest_index = 0

        for i in range(len(nums) - 1):
            # Update the farthest position that can be reached from current position
            farthest_index = max(farthest_index, i + nums[i])
            
            # If we've reached the boundary of our current jump range,
            # we must make another jump to continue
            if i == current_end:
                jumps += 1
                current_end = farthest_index

        return jumps
    
nums = [2, 3, 1, 1, 4]
s = Solution()
print(s.jump(nums))  # Output: 2

'''
Key Insights for the Algorithm:

1. We maintain three variables:
   - jumps: Counts the minimum number of jumps needed to reach the end
   - current_end: Marks the furthest we can go with our current jump count
   - farthest_index: Tracks the furthest position we can potentially reach

2. At each position, we:
   - Look ahead to find the farthest we can jump from there
   - Only increment our jump counter when we've reached the limit of our current jump
   - Always choose the position that lets us go the furthest for the next jump

3. Time Complexity: O(n) as we make a single pass through the array
   Space Complexity: O(1) as we only use three variables regardless of input size

Example walkthrough for nums = [2, 3, 1, 1, 4]:

Index 0: nums[0] = 2
- From position 0, we can jump to positions 1 or 2
- current_end = 0, so we must jump (jumps = 1)
- Update current_end = 2 (furthest we can go in 1 jump)

Index 1: nums[1] = 3
- From position 1, we can reach position 4 (1 + 3)
- farthest_index becomes 4
- i != current_end, so we don't jump yet

Index 2: nums[2] = 1
- i == current_end, so we need another jump (jumps = 2)
- Update current_end = 4 (furthest we can go in 2 jumps)

Index 3: nums[3] = 1
- We continue, but don't need another jump since we can already reach the end

Result: 2 jumps needed
'''