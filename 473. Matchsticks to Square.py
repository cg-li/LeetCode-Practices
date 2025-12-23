class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        

        n = len(matchsticks)
        summatch = 0
        for i in range(n):
            summatch += matchsticks[i]

        if summatch % 4 != 0:
            return False
        
        side = summatch // 4
        matchsticks.sort(reverse = True)

        sides = [0, 0, 0, 0]

        def dfs(i):
            if i == n:
                return True
            for j in range(4):
                if matchsticks[i] <= side-sides[j]:
                    if j > 0 and sides[j] == sides[j-1]:
                        continue
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
                if sides[j] == 0:
                    break
            return False
        
        return dfs(0)
