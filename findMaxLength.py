class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
            def do(x):
                if x == 0:
                    return -1
                else:
                    return 1
                
            n = len(nums)
            arr =nums
            hash_map = {}   
            curr_sum = 0 
            max_len = 0 
            ending_index = -1 
            arr = list(map(do,arr))
            for i in range (n):  
                curr_sum += arr[i]  
                if (curr_sum == 0):  
                    max_len = i + 1 
                    ending_index = i  

                if curr_sum in hash_map: 
                    if max_len < i - hash_map[curr_sum]: 
                        max_len = i - hash_map[curr_sum] 
                        ending_index = i 
                else:  
                    hash_map[curr_sum] = i   

            return max_len 

    
    
    
    
    
    
