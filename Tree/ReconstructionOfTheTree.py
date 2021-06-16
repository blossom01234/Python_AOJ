pos = 0
inList = []
preList = []
postList = []


def rec(l: int, r: int) -> None:
    global pos
    if l >= r:
        return
    root = preList[pos]
    pos += 1

    m = inList.index(root)
    rec(l, m)
    rec(m + 1, r)
    postList.append(root)


def solve() -> None:
    post = 0
    rec(0, len(preList))
    print(*postList)


if __name__ == "__main__":
    n = int(input())

    preList = list(map(int, input().split()))
    inList = list(map(int, input().split()))
    solve()
