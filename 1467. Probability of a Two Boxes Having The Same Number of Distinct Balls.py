class Solution:
    def getProbability(self, balls: List[int]) -> float:
        
        k = len(balls)
        dp = defaultdict(int)
        dp[(0,0,0)] = 1
        

        for i in range(k):

            m = balls[i]
            newdp = defaultdict(int)

            for (A,B,delta), count in dp.items():
                newdp[(A+1,B,delta+m)] += count
                newdp[(A,B+1,delta-m)] += count
                for j in range(1,m):
                    newdp[(A+1,B+1,delta+2*j-m)] += count*comb(m,j)
            dp = newdp
        
        total = 0
        same = 0
        for (A,B,delta), count in dp.items():
            if delta == 0:
                total += count
                if A == B:
                    same += count
        
        return same/total





        
