n = 6
for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        print(i, j, l)
