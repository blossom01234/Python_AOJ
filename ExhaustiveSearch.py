n = int(input())
A = list(map(int, input().split()))

q = int(input())
m = list(map(int, input().split()))


def dfs(idx, s, target):
    # 対象の数値を合計値が超えた時点でFalseを返しているので実行速度が速い
    # 足し算ではなく、引き算にしてターゲットの数値が0であるかで
    # 判定すると、全部の要素を走査するので時間がかかってしまう
    if s == target:
        return 1

    # ここの左の条件で再帰呼び出しを早めに切り上げることができる
    if s > target or idx == n:
        return 0
    if s + sum(A[idx:]) < target:
        return 0

    return dfs(idx+1, s, target) or dfs(idx+1, s + A[idx], target)


for target in m:
    ans = 'yes' if dfs(0, 0, target) else 'no'
    print(ans)
