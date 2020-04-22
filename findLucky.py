class Solution:
    def findLucky(self, arr: List[int]) -> int:
        apper = []
        setaki = set(arr)
        for i in setaki:
            if ( arr.count(i) == i ):
                apper.append(i) 
        
        if ( not apper ):
            return -1
        else:
            return max(apper)