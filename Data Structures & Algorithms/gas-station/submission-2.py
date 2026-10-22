class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start






#NB: First we are going to check if the total of the gas is less than cost and if is less than the cost we return -1, and then start the tank with 0 and the start with 0 also. for loop to visit  i index : and the gas[i] minus cost[i] which is going going to give me the tank and if tank is less than zero we just add start as [i + i] and then finally we return the result whenthe loop stops.
        