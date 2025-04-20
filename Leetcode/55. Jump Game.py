'''
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
'''

'''
This question is a classic example of the greedy algorithm.
nums = [2, 3, 1, 1, 4]
output = True
Question explanation: 
First number is 2 so you can jump 1 or 2 steps forward.
Jumping 1 step forwards to 3 is the best option because it allows you to jump 2 steps forward to 4, which is the end of the array. Problem solved.
'''


# To solve this problem, we only care if we can reach the last number or not.
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True
    

'''
Line by line explaination:

max_reach = 0
# This keeps track of the farthest index you can reach so far.
# At the start, you haven't made any jumps yet, so max_reach starts as 0.

for i in range(len(nums)):
    if i > max_reach:
        return False
    max_reach = max(max_reach, i + nums[i])
return True

#If a list has 5 elements, i will take values from 0 to 4.
# If i(0-5) is greater than max_reach(starting from 0), it means you can't reach this index, so return False.
# If you can reach this index i (0-5), update max_reach to be the maximum of its current value and the index you can reach from this position (i + nums[i]).
'''