class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        temp = s + "#" + rev
        
        # Build LPS array
        lps = [0] * len(temp)
        
        for i in range(1, len(temp)):
            j = lps[i - 1]
            
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            
            if temp[i] == temp[j]:
                j += 1
            
            lps[i] = j
        
        # Length of longest palindromic prefix
        longest_prefix_len = lps[-1]
        
        # Add remaining characters in front
        return rev[:len(s) - longest_prefix_len] + s
