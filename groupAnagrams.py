class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections 
        def areAnagram(str1, str2):  
            # r1 =  [str(d) for d in str(str1)]
            # r2 =  [str(d) for d in str(str2)]
            # return collections.Counter(r1) == collections.Counter(r2)
            return collections.Counter(str1) == collections.Counter(str2)
        
        
        
        from collections import deque
        
        res = []
        new = deque(strs)
        
        while(strs):
            element = new.popleft()
            strs.remove(element)
            
            q = deque()
            l = []
            l.append(element)
            
            if (strs):
                for i in range(0,len(strs)):
                    if (areAnagram(strs[i],element)):
                        l.append(strs[i])
                        q.append(strs[i])

                while(q):
                    fige = q.pop()
                    new.remove(fige)
                    strs.remove(fige)
            print(l)
            res.append(l)

        
        return res
        