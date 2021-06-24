MAX = 100
INFTY = 999999
WHITE = 0
GRAY = 1
BLACK = 2


M = [[INFTY for i in range(MAX)]for i in range(MAX)]
d = [INFTY for i in range(MAX)]
color = [WHITE for i in range(MAX)]


def dijkstra():
    global d
    global color
    d[0] = 0
    while True:
        mincost = INFTY
        for i in range(n):
            if color[i] != BLACK and d[i] < mincost:
                mincost = d[i]
                u = i

        if mincost == INFTY:
            break

        color[u] = BLACK

        for v in range(n):
            if color[v] != BLACK and M[u][v] != INFTY:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    color[v] = GRAY


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(2, len(line), 2):
            M[i][line[j]] = line[j + 1]

    dijkstra()

    for i in range(n):
        print(i, d[i])
