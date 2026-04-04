class Solution:
    def primePalindrome(self, n: int) -> int:
        import math
        
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(math.sqrt(x))
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True
        
        # Handle small cases
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11
        
        length = 1
        while True:
            # Generate odd-length palindromes
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                palindrome = int(s + s[-2::-1])
                
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
            
            length += 1
