from collections import deque

n = 0
MAX = 100000
G = [[] for i in range(MAX)]
color = [None for i in range(MAX)]


def dfs(r: int, c: int):
    S = deque()
    S.append(r)
    color[r] = c
    while len(S) > 0:
        u = S.pop()
        for i in range(len(G[u])):
            v = G[u][i]
            if color[v] == None:
                color[v] = c
                S.append(v)


def assinColor():
    id = 1
    for u in range(n):
        if color[u] == None:
            dfs(u, id)
            id += 1


if __name__ == "__main__":
    n, m = map(int, input().split())

    for i in range(m):
        s, t = map(int, input().split())
        G[s].append(t)
        G[t].append(s)

    assinColor()

    q = int(input())
    for i in range(q):
        s, t = map(int, input().split())
        if color[s] == color[t]:
            print("yes")
        else:
            print("no")
