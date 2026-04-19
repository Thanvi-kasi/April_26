class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        import math
        
        def is_prime(x):
            if x <= 1:
                return False
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        
        n = len(nums)
        max_prime = 0
        
        for i in range(n):
            # Main diagonal
            if is_prime(nums[i][i]):
                max_prime = max(max_prime, nums[i][i])
            
            # Secondary diagonal
            if is_prime(nums[i][n - i - 1]):
                max_prime = max(max_prime, nums[i][n - i - 1])
        
        return max_prime
