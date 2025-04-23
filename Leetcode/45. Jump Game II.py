'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
    
nums = [2, 3, 1, 1, 4]
s = Solution()
print(s.jump(nums))  # Output: 2

'''
Let's understand the variable names used in the code:
- jumps: This variable keeps track of the number of jumps made. We increase this counter but want to minimize it.
- current_end: This variable represents the farthest index that can be reached with the current number of jumps.
- farthest: This variable keeps track of the farthest index that can be reached from the current index.
'''

'''
nums = [2, 3, 1, 1, 4]

At Index 0:

i = 0
nums[0] = 2
current_end = 0
farthest = 0
jumps = 0

i + nums[i] = 0 + 2 = 2

farthest = max(0, 2) = 2

Now i == current_end → Time to jump:

jumps = 1

current_end = farthest = 2

🔍 State after index 0:

jumps = 1
current_end = 2
farthest = 2


At Index 1:
i = 1
nums[1] = 3
current_end = 2
farthest = 2
jumps = 1

i + nums[i] = 1 + 3 = 4

farthest = max(2, 4) = 4

Now i != current_end → Keep going, don’t jump yet.

🔍 State after index 1:

jumps = 1
current_end = 2
farthest = 4


At Index 2:
i = 2
nums[2] = 1
current_end = 2
farthest = 4
jumps = 1

i + nums[i] = 2 + 1 = 3

farthest = max(4, 3) = 4 → stays 4

Now i == current_end → Time to jump:

jumps = 2

current_end = farthest = 4

🔍 State after index 2:

jumps = 2
current_end = 4
farthest = 4


At Index 3:
i = 3
nums[3] = 1
current_end = 4
farthest = 4
jumps = 2

i + nums[i] = 3 + 1 = 4

farthest = max(4, 4) = 4

Now i != current_end → Keep going.

🔍 State after index 3:
jumps = 2
current_end = 4
farthest = 4

⛳️ Final Output:
Total jumps needed = 2



Index | nums[i] | i + nums[i] | farthest | current_end | jumps | Action
0     |       2 |           2 |        2 |     0 → 2 |     1 | Jump
1     |       3 |           4 |        4 |         2 |     1 | Continue
2     |       1 |           3 |        4 |     2 → 4 |     2 | Jump
3     |       1 |           4 |        4 |         4 |     2 | Continue
'''