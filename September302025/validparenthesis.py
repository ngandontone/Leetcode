def isValid(self, s: str) -> bool:
        hashmap = {'}':'{',
                    ']':'[',
                    ')':'('}
        stack = []
        for c in s:
            if c in hashmap:
                if stack and stack[-1]==hashmap[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)

        return True if not stack else False
