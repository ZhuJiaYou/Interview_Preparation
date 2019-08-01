import heapq


class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []

    def add_num(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        print(self.low)
        print(self.high)
        if len(self.low) == len(self.high):
            return (self.high[0] - self.low[0]) / 2
        else:
            return -self.low[0]



if __name__ == '__main__':
    mf = MedianFinder()
    mf.add_num(-1)
    mf.add_num(-2)
    mf.add_num(-3)
    mf.add_num(-4)
    mf.add_num(-5)
    print(mf.find_median())

    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())
    mf.add_num(41)
    print(mf.find_median())
    mf.add_num(35)
    mf.add_num(62)
    mf.add_num(4)
    mf.add_num(97)
    print(mf.find_median())
