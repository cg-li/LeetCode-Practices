class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """


        stickercounter = [Counter(s) for s in stickers]

        initialstate = ''.join(sorted(target))

        memo = {'':0}


        maxcount = Counter()
        for s in stickercounter:
            maxcount |= s
        for char in set(target):
            if maxcount[char] == 0:
                return -1

        def dp(state):
            if state in memo:
                return memo[state]
            best = float('inf')
            for s in stickercounter:                
                if state[0] in s:
                    newstring = []
                    new = Counter(state)
                    for char, num in new.items():
                        remain = num - s.get(char, 0)
                        if remain > 0:
                            newstring.append(char*remain)
                    newstate = ''.join(sorted(''.join(newstring)))
                    best = min(best, 1+dp(newstate))
            memo[state] = best
            return best

        result = dp(initialstate)

        return result if result != float('inf') else -1
                    
