NIL = -1


class Node():
    def __init__(self) -> None:
        self.left = NIL
        self.right = NIL
        self.parent = NIL


T = [Node()]
printList = []


def preParse(u: int):
    if u == NIL:
        return
    printList.append(u)
    preParse(T[u].left)
    preParse(T[u].right)


def inParse(u: int):
    if u == NIL:
        return
    inParse(T[u].left)
    printList.append(u)
    inParse(T[u].right)


def postParse(u: int):
    if u == NIL:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    printList.append(u)


if __name__ == "__main__":
    n = int(input())
    T = [Node() for i in range(n)]
    for i in range(n):
        value, left, right = map(int, input().split())
        T[value].left = left
        T[value].right = right
        if left != NIL:
            T[left].parent = value
        if right != NIL:
            T[right].parent = value
    root = 0
    for i in range(n):
        if T[i].parent == NIL:
            root = i

    print("Preorder")
    printList = []
    preParse(root)
    print(" ", end="")
    print(*printList)

    print("Inorder")
    printList = []
    inParse(root)
    print(" ", end="")
    print(*printList)

    print("Postorder")
    printList = []
    postParse(root)
    print(" ", end="")
    print(*printList)
