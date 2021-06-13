NIL = -1
T = []


class Node():
    def __init__(self) -> None:
        self.left = NIL
        self.right = NIL
        self.parent = NIL
        self.depth = NIL
        self.height = NIL

    def getDegree(self) -> int:
        ret = 0
        if self.right != NIL:
            ret += 1
        if self.left != NIL:
            ret += 1
        return ret

    def getType(self) -> str:
        if self.parent == NIL:
            return "root"
        elif self.left == NIL and self.right == NIL:
            return "leaf"
        else:
            return "internal node"

    def getSibling(self, n) -> int:
        if n == 0:
            n = n
        if self.parent == NIL:
            return NIL
        elif T[self.parent].left != NIL and T[self.parent].left != n:
            return T[self.parent].left
        elif T[self.parent].right != NIL and T[self.parent].right != n:
            return T[self.parent].right
        else:
            return NIL


def culcDepth(u, p):
    T[u].depth = p
    if T[u].left != NIL:
        culcDepth(T[u].left, p + 1)
    if T[u].right != NIL:
        culcDepth(T[u].right, p + 1)


def calcHeight(u):
    isChild = False
    ans1 = 0
    ans2 = 0
    if T[u].left != NIL:
        ans1 = calcHeight(T[u].left) + 1
    if T[u].right != NIL:
        ans2 = calcHeight(T[u].right) + 1
    T[u].height = max(ans1, ans2)
    return T[u].height


def printTrees(u):
    print(
        f"node {u}: parent = {T[u].parent}, sibling = {T[u].getSibling(u)}, "
        f"degree = {T[u].getDegree()}, depth = {T[u].depth}, "
        f"height = {T[u].height}, {T[u].getType()}")


if __name__ == "__main__":
    n = int(input())
    T = [Node() for i in range(n)]
    for i in range(n):
        Line = list(map(int, input().split()))
        T[Line[0]].left = Line[1]
        T[Line[0]].right = Line[2]
        if Line[1] != NIL:
            T[Line[1]].parent = Line[0]
        if Line[2] != NIL:
            T[Line[2]].parent = Line[0]

    for i in range(n):
        if T[i].parent == NIL:
            r = i
    culcDepth(r, 0)
    calcHeight(r)

    for i in range(n):
        printTrees(i)
