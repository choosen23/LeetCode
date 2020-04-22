class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        aux = []
        for i in range(0,len(prices)-1):
            aux.append(prices[i] - prices[i+1])
        
        res = sum(list(filter(lambda x : x < 0, aux)))
        print(res)
        return res*-1