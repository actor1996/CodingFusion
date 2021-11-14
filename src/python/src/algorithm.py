from typing import List
import pandas as pd
import heapq
from sortedcontainers import SortedList
from abc import ABCMeta, abstractmethod


class MedianFinder():
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def addNum(self, num: int) -> None:
        pass

    @abstractmethod
    def findMedian(self) -> float:
        pass


    def test(self):
        self.addNum(1)
        self.addNum(2)
        ans1 = self.findMedian()
        print('expected:{} actual:{}'.format(1.5, ans1))
        self.addNum(3)
        ans2 = self.findMedian()
        print('expected:{} actual:{}'.format(2.0, ans2))



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinderPriorityQueue(MedianFinder):

    def __init__(self):
        MedianFinder.__init__(self)
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinderOrderedSetsAndDoublePointers(MedianFinder):

    def __init__(self):
        MedianFinder.__init__(self)
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num: int) -> None:
        nums_ = self.nums

        n = len(nums_)
        nums_.add(num)

        if n == 0:
            self.left = self.right = 0
        else:
            # 模拟双指针，当 num 小于 self.left 或 self.right 指向的元素时，num 的加入会导致对应指针向右移动一个位置
            if num < self.left_value:
                self.left += 1
            if num < self.right_value:
                self.right += 1

            if n & 1:
                if num < self.left_value:
                    self.left -= 1
                else:
                    self.right += 1
            else:
                if self.left_value < num < self.right_value:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_value:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right

        self.left_value = nums_[self.left]
        self.right_value = nums_[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class KthSmallest:
    __metaclass__ = ABCMeta

    @abstractmethod
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass

    def test_case1(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        ans=self.kthSmallest(matrix,k)
        print('expected:{} actual:{}'.format(13, ans))


    def test_case2(self):
        matrix = [[-5]]
        k = 1
        ans=self.kthSmallest(matrix,k)
        print('expected:{} actual:{}'.format(-5, ans))

    def test(self):
        self.test_case1()
        self.test_case2()



class KthSmallestDichotomousSearch(KthSmallest):
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left



def test():
    # MedianFinderPriorityQueue().test()
    # MedianFinderOrderedSetsAndDoublePointers().test()
    KthSmallestDichotomousSearch().test()

if __name__ == '__main__':
    test()

