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


#NB: First we check if total gas is less than total cost and if it is we return -1, then we let tank = 0 and start to be = 0. Also, we use a for loop to check for each station in i we add gas and subtract cost from tank and if tank is negative, we set start to i +1 and we reset tank to 0 again and finally return start after the loop finishes.
            




