A = []


def partition(p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


input()
A = list(map(int, input().split()))
r = A[len(A)-1]
q = partition(0, len(A)-1)

ans = ""
for i in range(len(A)):
    if i == q:
        ans += f"[{A[i]}] "
    else:
        ans += f"{A[i]} "
print(ans[:-1])
