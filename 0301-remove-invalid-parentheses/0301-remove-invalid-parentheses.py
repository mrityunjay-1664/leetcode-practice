from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        # BFS queue and visited set to avoid duplicate states
        queue = deque([s])
        visited = {s}
        found = False
        res = []

        while queue:
            level_size = len(queue)
            level_res = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if isValid(curr):
                    found = True
                    level_res.append(curr)
                
                if found:
                    continue
                
                # Generate all possible strings by removing one parenthesis at a time
                for i in range(len(curr)):
                    if curr[i] not in ('(', ')'):
                        continue
                    
                    next_str = curr[:i] + curr[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
            
            # If we found valid strings at this depth, return them
            if found:
                return level_res

        return [""]