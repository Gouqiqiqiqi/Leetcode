'''
Questions: 134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique.
'''

'''
Let's undertsand the problem with an example:
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

So:
If we start from station 0:
Station 0: Get 1, need 3 to go → short by 2
If we start from station 1:
Station 1: Get 2, need 4 → short by 2
If we start from station 2:
Station 2: Get 3, need 5 → short by 2
If we start from station 3:
Station 3: Get 4, need 1 → extra 3
If we start from station 4:
Station 4: Get 5, need 2 → extra 3

So we can start from station 3 or 4.
But which one is the best?
'''


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_tank = 0 # This is the total gas we have
        curr_tank = 0 # This is the current gas we have
        start_station = 0 # This is the index of the starting gas station

        for i in range(len(gas)):
            diff = gas[i] - cost[i] # This is the difference between the gas we have and the gas we need
            total_tank += diff # This answers the question: can we complete the circuit?
            curr_tank += diff # This answers the question: can we reach the next station?

            # If we can't reach the next station from current start
            if curr_tank < 0: # If we can't reach the next station from current start
                start_station = i + 1 # We need to start from the next station
                curr_tank = 0 # Reset the current tank to 0, as we are starting from the next station

        return start_station if total_tank >= 0 else -1 # If we can complete the circuit, return the starting station index, else return -1, meaning we can't complete the circuit
    



