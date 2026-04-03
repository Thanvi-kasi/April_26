class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        
        for i in range(len(s)):
            # Check if prefix matches starting at i
            if s[i:].startswith(prefix):
                # Check if suffix exists after prefix
                if suffix == "" or suffix in s[i + len(prefix):]:
                    return True
        
        return False
