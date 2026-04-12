class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}

        for num in nums:
            node = trie
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        max_xor = 0
        
        for num in nums:
            node = trie
            curr_xor = 0
            
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit  
                
                if toggled in node:
                    curr_xor |= (1 << i)
                    node = node[toggled]
                else:
                    node = node[bit]
            
            max_xor = max(max_xor, curr_xor)
        
        return max_xor
