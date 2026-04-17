class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Function to count primes up to n using Sieve of Eratosthenes
        def count_primes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return sum(is_prime)
        
        # Count how many primes are in [1, n]
        prime_count = count_primes(n)
        non_prime_count = n - prime_count
        
        # Compute factorial modulo MOD
        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % MOD
            return result
        
        # Multiply permutations of primes and non-primes
        return (factorial(prime_count) * factorial(non_prime_count)) % MOD
