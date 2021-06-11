SENTINEL = 2000000000


class Card():
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = int(value)


def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    L.append(Card("sentinel", SENTINEL))
    R.append(Card("sentinel", SENTINEL))
    i = 0
    j = 0
    for k in range(left, right):
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left+right)//2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j].value <= x.value:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


if __name__ == "__main__":
    A = []
    B = []
    n = int(input())
    for i in range(n):
        suit, value = input().split()
        A.append(Card(suit, value))
        B.append(Card(suit, value))
    mergeSort(A, 0, n)
    quickSort(B, 0, n-1)

    ans = "Stable"
    for i in range(len(B)):
        if A[i].suit != B[i].suit:
            ans = "Not stable"
    print(ans)

    for i in B:
        print(i.suit, i.value)
