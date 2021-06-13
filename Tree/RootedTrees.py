import sys
# 一時的に再帰回数を上げておくことで実行時エラーを回避する
sys.setrecursionlimit(200000)
NIL = -1


class Node():
    def __init__(self) -> None:
        self.p = NIL
        self.l = NIL
        self.r = NIL


T = []
D = []


def printTrees(u: int):
    print(f"node {u}: parent = {T[u].p}, depth = {D[u]}, ", end="")
    if T[u].p == NIL:
        print("root, ", end="")
    elif T[u].l == NIL:
        print("leaf, ", end="")
    else:
        print("internal node, ", end="")

    print("[", end="")
    c = T[u].l
    while c != NIL:
        print(c, end="")
        c = T[c].r
        if c != NIL:
            print(", ", end="")
    print("]")


def rec(u, p):
    D[u] = p
    if T[u].r != NIL:
        rec(T[u].r, p)
    if T[u].l != NIL:
        rec(T[u].l, p + 1)


if __name__ == "__main__":
    n = int(input())
    D = [0 for i in range(n)]
    T = [Node() for i in range(n)]
    prev = 0
    for i in range(n):
        Line = list(map(int, input().split()))
        for index, value in enumerate(Line):
            if index < 2:
                continue
            if index == 2:
                T[Line[0]].l = value
            else:
                T[prev].r = value
            prev = value
            T[value].p = Line[0]

    for i in range(n):
        if T[i].p == NIL:
            r = i

    rec(r, 0)

    for i in range(n):
        printTrees(i)
