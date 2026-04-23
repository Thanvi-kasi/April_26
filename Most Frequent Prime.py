from collections import defaultdict
import math

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # 8 directions
        directions = [
            (0, 1),   # east
            (1, 1),   # south-east
            (1, 0),   # south
            (1, -1),  # south-west
            (0, -1),  # west
            (-1, -1), # north-west
            (-1, 0),  # north
            (-1, 1)   # north-east
        ]
        
        # Prime check
        def is_prime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True
        
        freq = defaultdict(int)
        
        # Traverse each cell
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i, j
                    num = 0
                    
                    # Move in one direction
                    while 0 <= x < m and 0 <= y < n:
                        num = num * 10 + mat[x][y]
                        
                        if num > 10 and is_prime(num):
                            freq[num] += 1
                        
                        x += dx
                        y += dy
        
        if not freq:
            return -1
        
        # Find most frequent prime (largest if tie)
        max_freq = max(freq.values())
        result = max(num for num, count in freq.items() if count == max_freq)
        
        return result
