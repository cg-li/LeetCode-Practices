class MedianFinder(object):

    def __init__(self):
        self.hp1 = []
        self.hp2 = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        n1 = len(self.hp1)
        n2 = len(self.hp2)
        if n1 == n2:
            if n1 == 0:
                heapq.heappush(self.hp1, -num)
            else:
                mid1 = -self.hp1[0]
                mid2 = self.hp2[0]
                if num > mid2:
                    heapq.heappush(self.hp2, num)
                    heapq.heappop(self.hp2)
                    heapq.heappush(self.hp1, -mid2)
                else:
                    heapq.heappush(self.hp1, -num)
        else:
            if n2 == 0:
                if num >= -self.hp1[0]:
                    heapq.heappush(self.hp2, num)
                else:
                    mid1 = -heapq.heappop(self.hp1)
                    heapq.heappush(self.hp1, -num)
                    heapq.heappush(self.hp2, mid1)
            else:
                mid1 = -self.hp1[0]
                mid2 = self.hp2[0]
                if num >= mid1:
                    heapq.heappush(self.hp2, num)
                else:
                    heapq.heappop(self.hp1)
                    heapq.heappush(self.hp1, -num)
                    heapq.heappush(self.hp2, mid1)

    def findMedian(self):
        """
        :rtype: float
        """
        n1 = len(self.hp1)
        n2 = len(self.hp2)
        if n1 == n2:
            if n1 == 0:
                return "null"
            else:
                mid1 = -self.hp1[0]
                mid2 = self.hp2[0]
                return float((mid1 + mid2)/2.0)
        else:
            return float(-self.hp1[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
