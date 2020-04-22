class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect  
        def insert(list, n):
            list = list[:-2]
            bisect.insort(list, n)  
            return list

        stones.sort()
        while (len(stones) > 1):
            stones = insert(stones,abs(stones[-1]-stones[-2]))

        return stones[0] if stones else 0

    
