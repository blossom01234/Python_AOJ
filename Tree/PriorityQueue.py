from collections import deque
import sys


class PriorityQueue(object):
    def __init__(self, heap: deque) -> None:
        self.heap = heap
        self.heap.insert(0, 0)

    def parent(self, i: int):
        return i // 2

    def left(self, i: int):
        return 2 * i

    def right(self, i: int):
        return (2 * i) + 1

    def maxHeapify(self, i):
        heap = self.heap
        l = self.left(i)
        r = self.right(i)
        if l <= len(heap)-1 and heap[l] > heap[i]:
            lergest = l
        else:
            lergest = i
        if r <= len(heap)-1 and heap[r] > heap[lergest]:
            lergest = r

        if lergest != i:
            self.heap[i], self.heap[lergest] = self.heap[lergest], self.heap[i]
            self.maxHeapify(lergest)

    def buildMaxHeap(self):
        maxlength = len(self.heap)-1
        for i in range(maxlength // 2, 0, -1):
            self.maxHeapify(i)

    def extract(self):
        if len(self.heap) < 2:
            return -1
        maxv = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.maxHeapify(1)
        return maxv

    def insert(self, key: int):
        self.heap.append(-1)
        self.increaseKey(key)

    def increaseKey(self, key: int):
        i = len(self.heap) - 1
        if key < self.heap[i]:
            return
        self.heap[i] = key

        while i > 1 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)
                                    ] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


if __name__ == "__main__":
    pQueue = PriorityQueue([])
    for line in sys.stdin:
        order = line.rstrip()
        if order == "extract":
            print(pQueue.extract())
        elif order == "end":
            break
        else:
            _, index = order.split()
            index = int(index)
            pQueue.insert(index)
