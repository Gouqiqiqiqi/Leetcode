'''
Question 45: Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Approach: Greedy algorithm that minimizes the numuber of jumps by always choosing the position 
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
    
nums = [2, 3, 1, 1, 4, 5]
s = Solution()
print(s.jump(nums))  # Output: 3

'''
Key Insights for the Algorithm:

1. We maintain three variables:
   - jumps: Counts the minimum number of jumps needed to reach the end
   - current_end: Marks the furthest we can go within our current index range
   - farthest_index: Tracks the furthest position we can reach for each index

2. At each index, we:
   - Look ahead to find the farthest we can jump
   - Only increment our jump counter when we've reached the current_end
   - At current_end, always choose the index in the range that lets us go the furthest for the next jump

Logic walkthrough:

nums = [2, 3, 1, 1, 4]

when i = 0, nums[i] = 2.
At index 0, we can jump to index 1 or index 2 (0 + 2).
Index 2 is the current farthest place we can reach.
Therefore our current_end can be updated to 2 (index 2).
We loop index 1 and 2 to find their farthest positions reachable, using farthest_index = max(farthest_index, i + nums[i]).
Index 1 gives us 1 + nums[1] = 4, and index 2 gives us 2 + nums[2] = 3.
Now the farthest_index is 4.
Once we reach index 2 (our current end), when i = 2 == current_end, we need to jump again.
And we jump from nums[1] to nums[4] which is the farthest we can reach from index 1.

How does the program know when to stop?

The loop runs from index 0 to index len(nums) - 2. 
We never need to evaluate the last index, since the goal is just to reach it, not jump from it. 
At each step, we update the farthest position we can reach. 
Whenever we reach the end of the current jump range (`current_end`), we increase the jump count and extend the range to the new `farthest_index`. 
As soon as the current_end covers or passes the last index, we know we can reach the end, so no more jumps are needed.

In this example, current_end is 4, meaning it can reach index 4. The loop only goes to index 3, because we don't need to evaluate the last index (4).
4 is greater than 3, so we can reach the end of the array.

Example walkthrough for nums = [2, 3, 1, 1, 4]:



Iteration 1: 

i = 0
nums[i] = 2

farthest_index = max(0, 0 + 2) = 2

Since i == current_end (0), it's time to make a jump:

jumps = 1

current_end = farthest_index = 2

✅ We commit to jumping to index 2 or somewhere in that range.

Iteration 2: 

i = 1
nums[i] = 3

farthest_index = max(2, 1 + 3) = 4

i != current_end (2), so we don't increment jumps yet.

🧠 We're analyzing how far we could go from index 1, but haven't reached the end of our current jump.

Iteration 3: 

i = 2
nums[i] = 1

farthest_index = max(4, 2 + 1) = 4 (no change)

Since i == current_end (2), it's time to make a jump:

jumps = 2

current_end = farthest_index = 4

✅ We now commit to jump to index 4 — the end of the array.

Iteration 4: i = 3
Loop ends before i = 4, since we only go to len(nums) - 2.

Final result:
jumps = 2  

✅ Minimum number of jumps needed to reach the end: 2
'''