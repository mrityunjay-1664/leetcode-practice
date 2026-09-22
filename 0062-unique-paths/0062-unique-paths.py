class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row with 1s
        row = [1] * n
        
        # Iterate through the remaining rows
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(1, n):
                # The number of paths to a cell is the sum of paths 
                # from the cell above it and the cell to its left
                newRow[j] = newRow[j - 1] + row[j]
            row = newRow
            
        return row[-1]