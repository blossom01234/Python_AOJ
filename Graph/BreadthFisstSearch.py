from collections import deque
import math
WHITE = 0
GRAY = 1
BLACK = 2
INFINITY = 1000


class BreadthFirstSearch():
    def __init__(self, M: list, n: int) -> None:
        self.color = [WHITE for i in range(n)]
        self.M = M
        self.d = [INFINITY for i in range(n)]
        self.Q = deque()
        self.n = n

    def bfs(self, start: int):
        self.Q.append(start)
        self.d[start] = 0
        while len(self.Q) > 0:
            target = self.Q.popleft()
            for v in range(self.n):
                if self.M[target][v] == 0:
                    continue
                if self.d[v] != INFINITY:
                    continue
                if self.color[v] == WHITE:
                    self.Q.append(v)
                    self.color[v] = GRAY
                    self.d[v] = self.d[target] + 1
            self.color[target] = BLACK
        for i in range(n):
            if self.d[i] == INFINITY:
                print(i + 1, -1)
            else:
                print(i + 1, self.d[i])


if __name__ == "__main__":
    n = int(input())
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        j = 2
        while j < len(line):
            graph[i][line[j] - 1] = 1
            j += 1
    breadth = BreadthFirstSearch(graph, n)
    breadth.bfs(0)
