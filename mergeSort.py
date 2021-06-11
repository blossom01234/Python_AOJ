cnt = 0
SENTINEL = 1000000000


def merge(A, n: int, left: int, mid: int, right: int) -> list:
    L = A[left:mid]
    R = A[mid:right]
    L.append(SENTINEL)
    R.append(SENTINEL)
    global cnt
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


def mergeSort(A, n: int, left: int, right: int) -> list:
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)
        return A
    else:
        pass


if __name__ == "__main__":
    cnt = 0
    n = int(input())
    A = list(map(int, input().split()))
    mergeSort(A, n, 0, n)
    print(*A)
    print(cnt)
