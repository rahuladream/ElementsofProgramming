import collections
class Solution:
    def maxPower(self, s):

        l = len(s) 
        count = 0
    
        # Find the maximum repeating  
        # character starting from s[i] 
        res = s[0] 
        for i in range(l): 
            
            cur_count = 1
            for j in range(i + 1, l): 
        
                if (s[i] != s[j]): 
                    break
                cur_count += 1
    
            # Update result if required 
            if cur_count > count : 
                count = cur_count 
                res = s[i] 
        return count
        
        

if __name__ == "__main__":
    a = Solution()
    print(a.maxPower("leetcode"))
