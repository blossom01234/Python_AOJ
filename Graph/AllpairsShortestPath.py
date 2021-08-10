MAX = 100
INFTY = 1 << 32
n = 0
d = [[INFTY for j in range(MAX)]for i in range(MAX)]


def floyd():
    for k in range(n):
        for i in range(n):
            if d[i][k] == INFTY:
                continue
            for j in range(n):
                if d[k][j] == INFTY:
                    continue
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


if __name__ == "__main__":
    n, e = map(int, input().splirt())
    for i in range(n):
        d[i][i] = 0
    for i in range(e):
        u, v, c = map(int, input().split())
        d[u][v] = c
    floyd()
    negative = False
    for i in range(n):
        if d[i][i] < 0:
            negative = True
    if negative:
        print("NEGATIVE CYCLE")
    else:
        for i in range(n):
            for j in range(n):
                if j:
                    print(" ", end="")
                if d[i][j] == INFTY:
                    print("INF", end="")
                else:
                    print(d[i][j])
            print()
