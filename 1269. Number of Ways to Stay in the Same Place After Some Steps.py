class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        maxpos = min(arrLen-1, steps)
        dp = [[0]*(maxpos+1) for _ in range(steps+1)]
        dp [0][0] = 1
        for i in range(1, steps+1):
            for j in range(0, maxpos+1):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                if j < maxpos:
                    dp[i][j] += dp[i-1][j+1]
                dp[i][j] %= MOD
        return dp[steps][0]
