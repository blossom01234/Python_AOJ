class Node(object):
    __slots__ = ["value", "parent", "left", "right"]

    def __init__(self, value: int, parent: 'Node' = None) -> None:
        self.value = value
        self.parent = parent
        self.left: Node = None
        self.right: Node = None

    def inPerse(self, a: list) -> list:
        if self.left:
            self.left.inPerse(a)
        a.append(self.value)
        if self.right:
            self.right.inPerse(a)
        return a

    def prePerse(self, a: list) -> list:
        a.append(self.value)
        if self.left:
            self.left.prePerse(a)
        if self.right:
            self.right.prePerse(a)
        return a


class BinarySearchTree(object):
    __slots__ = ["root"]

    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, target: int):
        if self.root is None:
            self.root = Node(target)
            return
        parent, current = None, self.root

        while current:
            parent = current
            if target < current.value:
                current = current.left
            else:
                current = current.right

        if target < parent.value:
            parent.left = Node(target, parent)
        else:
            parent.right = Node(target, parent)

    def find(self, k: int):
        x = self.root
        while x != None and k != x.value:
            if k < x.value:
                x = x.left
            else:
                x = x.right
        return x

    def getMinimum(self, target: Node) -> Node:
        while target.left is not None:
            target = target.left
        return target

    def getSuccesser(self, target: Node):
        if target.right is not None:
            # 右の子の中で一番小さいものを返す
            return self.getMinimum(target.right)

        parent = target.parent

        # この部分はなくても動く、中間順で一つ前の位置を返す
        while parent is not None and parent.right == target:
            target = parent
            parent = parent.parent
        return parent

    def delete(self, target: Node):
        if target.left is None or target.right is None:
            # 子がない、または一つの場合tempはtarget自身となる
            temp = target
        else:
            # 子が両方ある場合tempは右の子の中で一番小さいノードになる
            temp = self.getSuccesser(target)

        # tempの子がなかった場合はNoneと差し替える
        # ある場合はある方と差し替える
        child = None
        if temp.left is not None:
            child = temp.left
        elif temp.right is not None:
            child = temp.right

        if child is not None:
            child.parent = temp.parent

        # 上で選択した子供を親の子供（自分自身）の位置に配置する
        if temp.parent == None:
            # 親を削除する場合、子をそのまま親にする
            self.root = child
        elif temp == temp.parent.left:
            temp.parent.left = child
        elif temp == temp.parent.right:
            temp.parent.right = child

        # 子が両方ある場合は削除した箇所の値を右の子の中で一番小さいノードの値で更新する
        if temp != target:
            target.value = temp.value


if __name__ == "__main__":
    tree = BinarySearchTree()
    for i in range(int(input())):
        order = input()
        if order == "print":
            inp = tree.root.inPerse([])
            print("", *inp)
            prp = tree.root.prePerse([])
            print("", *prp)
        elif order.startswith("find"):
            _, target = order.split()
            target = int(target)
            if tree.find(target) is not None:
                print("yes")
            else:
                print("no")
        elif order.startswith("insert"):
            _, target = order.split()
            target = int(target)
            tree.insert(target)
        elif order.startswith("delete"):
            _, target = order.split()
            target = int(target)
            tree.delete(tree.find(target))
