class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        
        def mod_pow(x, n):
            result = 1
            x %= MOD
            while n:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result
        
        result = 1
        for digit in b:
            result = mod_pow(result, 10) * mod_pow(a, digit) % MOD
        
        return result
