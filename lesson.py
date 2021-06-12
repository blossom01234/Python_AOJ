SENTINEL = 1000000000


def merge(A, n: int, left: int, mid: int, right: int) -> int:
    L = A[left:mid]
    R = A[mid:right]
    L.append(SENTINEL)
    R.append(SENTINEL)
    n1 = mid - left
    n2 = right - mid
    cnt = 0
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            # n1の数からi（入れ替わりが起らなかった回数を引くと、移動距離が求められる）
            cnt += n1 - i
    return cnt


def mergeSort(A, n: int, left: int, right: int) -> int:
    if left + 1 < right:
        mid = (left + right) // 2
        v1 = mergeSort(A, n, left, mid)
        v2 = mergeSort(A, n, mid, right)
        v3 = merge(A, n, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0


if __name__ == "__main__":
    cnt = 0
    n = int(input())
    A = list(map(int, input().split()))
    ans = mergeSort(A, n, 0, n)
    print(ans)
