class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n = len(nums)
        m = len(multipliers)

        INF = 10**9

        dp = [[-INF]*(m+1) for _ in range(m+1)]
        dp[0][0] = 0

        for i in range(1, m+1):
            for l in range(i+1):
                if l-1 >= 0:
                    dp[i][l] = max(dp[i][l], dp[i-1][l-1] + nums[l-1] * multipliers[i-1])
                if i-1-l >= 0:
                    dp[i][l] = max(dp[i][l], dp[i-1][l] + nums[n-1-(i-l-1)] * multipliers[i-1])
            
        return max(dp[m])

