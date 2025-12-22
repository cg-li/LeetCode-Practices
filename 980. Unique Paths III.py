class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        m = len(grid)
        n = len(grid[0])


        def validnb(i,j):
            nb = []
            if i-1 >= 0 and grid[i-1][j] != -1:
                nb.append((i-1,j))
            if i+1 < m and grid[i+1][j] != -1:
                nb.append((i+1,j))
            if j-1 >= 0 and grid[i][j-1] != -1:
                nb.append((i,j-1))
            if j+1 < n and grid[i][j+1] != -1:
                nb.append((i,j+1))
            return nb

        visited = set()

        s1 = 0
        s2 = 0
        blanks = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s1 = i
                    s2 = j
                if grid[i][j] == 0:
                    blanks += 1
        
        count = [0]        

        def dfs(p,q):
            visited.add((p,q))
            for s,t in validnb(p,q):
                if (s,t) in visited:
                    continue
                if grid[s][t] == 1:
                    continue
                if grid[s][t] == 2:
                    if len(visited) == blanks + 1:
                        count[0] += 1
                else:
                    dfs(s,t)
            visited.remove((p,q))

        dfs(s1,s2)

        return count[0]
