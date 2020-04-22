class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        from collections import deque
        direction = number = 0
        for i in shift:
            if i[0] == 0: #means left
                direction = direction -1
                number = number - i[1] 
            else:
                direction += 1
                number += i[1]
        q = deque([str(x) for x in s])
        q.rotate(number)
        return ''.join(map(str,list(q))) 
