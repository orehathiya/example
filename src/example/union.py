from __future__ import annotations

from dataclasses import dataclass
from typing import assert_never


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Circle:
    x: float
    y: float
    r: float


@dataclass
class Rectangle:
    x: float
    y: float
    w: float
    h: float


Shape = Point | Circle | Rectangle


def print_shape(shape: Shape) -> None:
    match shape:
        case Point(x, y):
            print(f"Point {x} {y}")
        case Circle(x, y, r):
            print(f"Circle {x} {y} {r}")
        case Rectangle(x, y, w, h):
            print(f"Rectangle {x} {y} {w} {h}")
        case _ as unreachable:
            assert_never(unreachable)


@dataclass
class Branch:
    value: int
    left: Tree
    right: Tree


Tree = Branch | None


def contains(tree: Tree, value: int) -> bool:
    match tree:
        case None:
            return False
        case Branch(x, left, right):
            return x == value or contains(left, value) or contains(right, value)


tree: Tree = Branch(1, Branch(2, None, None), Branch(3, None, Branch(4, None, None)))

if __name__ == "__main__":
    print_shape(Point(1, 2))
    print_shape(Circle(3, 5, 7))
    print_shape(Rectangle(11, 13, 17, 19))

    assert contains(tree, 1)
    assert contains(tree, 2)
    assert contains(tree, 3)
    assert contains(tree, 4)
    assert not contains(tree, 5)
