class Solution:
    def countElements(self, arr: List[int]) -> int:
        suma = set(arr)
        
        def isTrue(element):
            if (element + 1) in suma:
                return 1
            else:
                return 0
        
        sum = 0
        for i in arr:
            sum = sum + isTrue(i)
            
        return sum