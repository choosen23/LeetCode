def isHappy( n: int) -> bool:
    isSeen = set()
    while(1):
        res =  [int(d) for d in str(n)]
        sum = 0
        for i in res:
            sum = sum + i*i
        
        if sum not in isSeen:
            if sum == 1 :
                return True
            else:
                n = sum                
                isSeen.add(sum)
                
        else: 
            return False

a = int(input())
print(isHappy(a))
