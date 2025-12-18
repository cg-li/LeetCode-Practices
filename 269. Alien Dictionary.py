class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        letters = []
        for s in words:
            for ch in s:
                if ch not in letters:
                    letters.append(ch)
        
        before = {ch : set() for ch in letters}
        after = {ch: set() for ch in letters}

        n = len(words)
        if n == 0:
            return ""
        if n == 1:
            return ''.join(letters)

        def compare(s1, s2):
            i = 0
            n1 = len(s1)
            n2 = len(s2)
            while i < n1 and i < n2 and s1[i] == s2[i]:
                i += 1
            if i == n1 and i == n2:
                return ""
            elif i == n1:
                return ""
            elif i == n2:
                return "-1"
            return s1[i] + s2[i]    
                 
        comparisons = []

        for i in range(n-1):
            s = compare(words[i], words[i+1])
            if s == "-1":
                return ""
            elif s != "":
                if s not in comparisons:
                    comparisons.append(s)
        
        if len(comparisons) == 0:
            return ''.join(letters)
        
        for s in comparisons:
            ch1 = s[0]
            ch2 = s[1]
            before[ch2].add(ch1)
            after[ch1].add(ch2)

        countbefore = {ch: 0 for ch in letters}
        for ch in before:
            countbefore[ch] = len(before[ch])

        result = []
        count = 0
        while len(result) < len(letters):
            oldcount = count
            for ch in countbefore:
                if countbefore[ch] == 0:
                    result.append(ch)
                    for afterch in after[ch]:
                        countbefore[afterch] -= 1
                    countbefore[ch] = -1  # visited marker
                    count += 1
            if oldcount == count:
                return ""
        return ''.join(result)
