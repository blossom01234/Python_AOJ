MAX = 100
INFTY = 9999
WHITE = 0
GRAY = 1
BLACK = 2
n = 0


def prim() -> int:
    d = [INFTY for i in range(MAX)]
    p = [-1 for i in range(MAX)]
    color = [WHITE for i in range(MAX)]
    d[0] = 0

    while True:
        minv = INFTY
        u = -1
        for i in range(n):
            if minv > d[i] and color[i] != BLACK:
                u = i
                minv = d[i]

        if u == -1:
            break

        color[u] = BLACK

        for v in range(n):
            if color[v] != BLACK and M[u][v] != INFTY:
                if d[v] > M[u][v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = GRAY

    sum = 0
    for i in range(n):
        if p[i] != -1:
            sum += M[i][p[i]]
    return sum


if __name__ == "__main__":
    n = int(input())
    M = [[INFTY for j in range(n)] for i in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        for j, e in enumerate(line):
            if e != -1:
                M[i][j] = e

    print(prim())
