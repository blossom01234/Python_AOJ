from math import sin, cos, radians


class Point():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0


def koch(n: int, a: Point, b: Point):
    if n == 0:
        return
    s = Point()
    t = Point()
    u = Point()
    th = radians(60)
    s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
    t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
    u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
    u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y

    koch(n - 1, a, s)
    print(s.x, s.y)
    koch(n - 1, s, u)
    print(u.x, u.y)
    koch(n - 1, u, t)
    print(t.x, t.y)
    koch(n - 1, t, b)


if __name__ == "__main__":
    a = Point()
    b = Point()
    n = int(input())

    a.x = 0
    a.y = 0
    b.x = 100
    b.y = 0

    print(a.x, a.y)
    koch(n, a, b)
    print(b.x, b.y)
