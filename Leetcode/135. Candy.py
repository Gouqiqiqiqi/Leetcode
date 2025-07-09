'''
Question 135: Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

'''

#  Two-pass greedy algorithm
class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candy = [1] * n  # We should give at least one candy to each child

        # Step 2: Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # Step 3: Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)  # Total candies needed
    

'''
Index in python:

arr = ['a', 'b', 'c', 'd']

| Index | Value | Notes           |
| ----- | ----- | --------------- |
| 0     | 'a'   | First element   |
| 1     | 'b'   |                 |
| 2     | 'c'   |                 |
| 3     | 'd'   | Last element    |
| -1    | 'd'   | Same as index 3 |
| -2    | 'c'   |                 |
| -3    | 'b'   |                 |
| -4    | 'a'   | Same as index 0 |


start = n - 2: starts at the second-to-last item

stop = -1: will stop before reaching -1 (so it ends at index 0)

So in reverse, if you want to reach index 0, you need to stop at -1. If you say stop = 0, it will stop at index 1, which is not what you want.

step = -1: moves backward (right to left)
'''