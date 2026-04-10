class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        sums.sort()
        
        def helper(sums):
            if len(sums) == 1:
                return []
            
            diff = sums[1] - sums[0]
            counter = Counter(sums)
            
            left = []
            right = []
            
            for x in sums:
                if counter[x] > 0:
                    counter[x] -= 1
                    counter[x + diff] -= 1
                    left.append(x)
                    right.append(x + diff)
            
            # Check which group contains 0
            if 0 in left:
                return helper(left) + [diff]
            else:
                return helper(right) + [-diff]
        
        return helper(sums)
