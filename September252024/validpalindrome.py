def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()
        
        l = 0
        r = len(clean) - 1

        while l <= r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True
