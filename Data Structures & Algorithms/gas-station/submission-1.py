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
        




#NB: first we check if total of gas is less than total cost and if so we return -1 and then we start with tank as 0 and start too as 0 and then we use a for loop to visit each station in i and we add gas[i] minus cost[i] to tank and if tank is negative we set start to i + 1 and reset tank to 0 again and finally we return start after the loop finishes.
            




