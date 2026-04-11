class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Helper to count characters
        def count(word):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            return freq
        
        # Step 1: Build max frequency requirement from words2
        maxFreq = [0] * 26
        for word in words2:
            freq = count(word)
            for i in range(26):
                if freq[i] > maxFreq[i]:
                    maxFreq[i] = freq[i]
        
        # Step 2: Check each word in words1
        result = []
        for word in words1:
            freq = count(word)
            valid = True
            
            for i in range(26):
                if freq[i] < maxFreq[i]:
                    valid = False
                    break
            
            if valid:
                result.append(word)
        
        return result
