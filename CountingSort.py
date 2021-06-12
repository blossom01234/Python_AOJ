def CountingSort(A: list, k: int, n: int) -> list:
    C = [0 for i in range(k + 1)]

    # Cに出現回数を記録する
    for j in range(1, n + 1):
        C[A[j]] += 1

    # 各要素を前から足してCの累積和をそれぞれの要素に入れる
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    # ソート元リストの後ろから順番に、Cのリストの要素番号の値を添え字としてBに値を格納
    # 後ろから行わな、安定的なソートにならない
    B = A[:]
    for j in range(n, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

    return B


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    B = CountingSort(A, 10000, n)
    print(*B[1:])
