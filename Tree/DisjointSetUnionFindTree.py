class DisjointSet(object):
    def __init__(self, n: int) -> None:
        self.rank = [0 for i in range(n)]
        self.parent = [0 for i in range(n)]
        for i in range(n):
            self.make_set(i)

    def make_set(self, x: int):
        self.parent[x] = x
        self.rank[x] = 0

    def same(self, x: int, y: int) -> bool:
        return self.find_set(x) == self.find_set(y)

    def unite(self, x: int, y: int):
        # 集合を結合する際に、親で結合することで木構造を圧縮することができる
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x: int, y: int) -> None:
        # ランクの高いほうを代表とする。同じ場合はx側を代表とする
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x: int) -> int:
        # 親をたどって、代表を返す。途中の子全ての親に代表の値を設定する
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]


if __name__ == "__main__":
    n, q = map(int, input().split())
    dSet = DisjointSet(n)
    for i in range(q):
        order, x, y = map(int, input().split())
        if order == 0:
            dSet.unite(x, y)
        else:
            if dSet.same(x, y):
                print(1)
            else:
                print(0)
