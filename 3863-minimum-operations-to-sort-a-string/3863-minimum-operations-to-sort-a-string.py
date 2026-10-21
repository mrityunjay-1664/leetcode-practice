class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_s = "".join(sorted(s))

        # Case 0: Already sorted
        if s == sorted_s:
            return 0

    
        if n == 2:
            return -1

        min_char = sorted_s[0]
        max_char = sorted_s[-1]

       
        if s[0] == min_char or s[-1] == max_char:
            return 1

       
        if s[0] == max_char and s[-1] == min_char:
            if s.count(max_char) == 1 and s.count(min_char) == 1:
                return 3

        # Case 2: All other cases can be sorted in 2 operations
        return 2