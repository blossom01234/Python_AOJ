def matrixChainMultiplication(n):
    m = [[0 for x in range(n + 1)] for y in range(n + 1)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = 99000001
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k + 1]
                              [j] + p[i - 1] * p[k] * p[j])
    print(m[1][n])


p = []

n = int(input())

for i in range(n):
    listed_input = input().split()
    p.append(int(listed_input[0]))

p.append(int(listed_input[1]))

matrixChainMultiplication(n)
