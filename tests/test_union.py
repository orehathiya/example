import pytest

from example.union import Branch, Circle, Point, Rectangle, Tree, contains, print_shape


def test_print_shape_point(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that print_shape correctly prints a Point."""
    p: Point = Point(1.0, 2.0)
    print_shape(p)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Point 1.0 2.0"


def test_print_shape_circle(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that print_shape correctly prints a Circle."""
    c: Circle = Circle(3.0, 4.0, 5.0)
    print_shape(c)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Circle 3.0 4.0 5.0"


def test_print_shape_rectangle(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that print_shape correctly prints a Rectangle."""
    r: Rectangle = Rectangle(6.0, 7.0, 8.0, 9.0)
    print_shape(r)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Rectangle 6.0 7.0 8.0 9.0"


def test_contains() -> None:
    """Test that contains finds values in a non-empty tree and returns False for missing values."""
    tree: Tree = Branch(
        1, Branch(2, None, None), Branch(3, None, Branch(4, None, None))
    )
    assert contains(tree, 1)
    assert contains(tree, 2)
    assert contains(tree, 3)
    assert contains(tree, 4)
    assert not contains(tree, 5)


def test_contains_empty() -> None:
    """Test that contains returns False for an empty tree."""
    assert not contains(None, 1)
