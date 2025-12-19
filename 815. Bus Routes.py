class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        
        dictionary = defaultdict(list)
        n = len(routes)

        for i in range(n):
            for j in routes[i]:
                dictionary[j].append(i)

        if source == target:
            return 0
        if source not in dictionary or target not in dictionary:
            return -1
        
        visitedstop = set()
        visitedbus = set()

        q = deque()
        for i in dictionary[source]:
                visitedbus.add(i)
                q.append((i,1))

        while q:
            bus, num = q.popleft()
            for j in routes[bus]:
                if j == target:
                    return num
                if j in visitedstop:
                    continue
                else:
                    visitedstop.add(j)
                    for k in dictionary[j]:
                        if k not in visitedbus:
                            visitedbus.add(k)
                            q.append((k, num+1))                        


        return -1
