class Heap(object):
    def __init__(self, heap: list) -> None:
        self.heap = heap
        self.heap.insert(0, 0)

    def parent(self, i: int):
        return i // 2

    def left(self, i: int):
        return 2 * i

    def right(self, i: int):
        return (2 * i) + 1

    def print(self):
        heap = self.heap
        for i in range(1, len(self.heap)):
            print(f"node {i}: key = {heap[i]}, ", end="")
            if self.parent(i) >= 1:
                print(f"parent key = {heap[self.parent(i)]}, ", end="")
            if self.left(i) <= len(self.heap)-1:
                print(f"left key = {heap[self.left(i)]}, ", end="")
            if self.right(i) <= len(self.heap)-1:
                print(f"right key = {heap[self.right(i)]}, ", end="")
            print()

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


if __name__ == "__main__":
    input()
    heap = Heap(list(map(int, input().split())))
    heap.buildMaxHeap()
    print("", *heap.heap[1:])
