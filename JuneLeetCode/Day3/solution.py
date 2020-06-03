import numpy as np
class Solution:
    def twoCitySchedCost(self, costs):
        
        lValue = len(costs)//2
        delta = [(a - b) for a, b in costs]
        ordered = sorted((value, i) for (i, value) in enumerate(delta))
        cost = 0
        for value,i in ordered[:lValue]:
            cost += costs[i][0]
        for value,i in ordered[lValue:]:
            cost += costs[i][1]
        return cost


if __name__ == "__main__":
    a = Solution()
    print(a.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))