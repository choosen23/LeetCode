class Solution:
    from collections import deque
    def backspaceCompare(self, S: str, T: str) -> bool:
        def final(string):
            r = [str(a) for a in string]
            
            res = deque()
            for i in range(0,len(r)):
                
                if r[i] != '#':
                    
                    res.append(r[i])
                else:
                    if (res):
                        res.pop()
                    
                
            return list(res)
        
        
        
        
        return final(S) == final(T)        
        
