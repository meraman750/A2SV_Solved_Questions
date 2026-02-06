#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        from collections import Counter
        s = Counter(a)
        
        for i in b:
            if i in s:
                s[i] -=1
                if s[i] == 0:
                    del s[i]
            else:
                return False
        return True    
    
    
    
