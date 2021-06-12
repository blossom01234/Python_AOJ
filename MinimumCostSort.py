MAX = 1000
VMAX = 10000
A = []
B = []
T = [0 for i in range(VMAX+1)]
n = 0
s = 0


def solve():
    ans = 0
    V = []
    B = A[:]
    for i in range(n):        
        V.append(False)
    B.sort()
    for i in range(n):
        T[B[i]] = i
    for i in range(n):
        if V[i]:
            continue
        cur = i
        S = 0
        m = VMAX
        an = 0
        while True:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]:
                break
        ans += min(S * (an - 2) * m, m + S + (an + 1) * s)
    return ans


if __name__ == "__main__":
    n = int(input())
    s = VMAX
    A = list(map(int,input().split()))
    for i in range(n):
        s = min(s, A[i])
    ans = solve()
    print(ans)