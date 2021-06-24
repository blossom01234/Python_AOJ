WHITE = 0
GRAY = 1
BLACK = 2


class DepthFisstSearch():
    def __init__(self, n: int, M: list) -> None:
        self.n = n
        self.tt = 0
        self.M = M
        self.color = [WHITE for i in range(n)]
        self.d = [WHITE for i in range(n)]
        self.f = [WHITE for i in range(n)]

    def dfs_visit(self, u: int) -> None:
        self.color[u] = GRAY
        self.tt += 1
        self.d[u] = self.tt
        for v in range(self.n):
            if self.M[u][v] == 0:
                continue
            if self.color[v] == WHITE:
                self.dfs_visit(v)
        self.color[u] = BLACK
        self.tt += 1
        self.f[u] = self.tt

    def dfs(self) -> None:
        for i in range(self.n):
            if self.color[i] == WHITE:
                self.dfs_visit(i)
        for i in range(self.n):
            print(i + 1, self.d[i], self.f[i])


if __name__ == "__main__":
    n = int(input())
    graph = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        j = 2
        while j < len(line):
            graph[i][line[j] - 1] = 1
            j += 1
    deph = DepthFisstSearch(n, graph)
    deph.dfs()
