from example.math import add, minus, multiply


class TestAdd:
    def test_add(self) -> None:
        assert add(2, 3) == 5


class TestMinus:
    def test_minus(self) -> None:
        assert minus(5, 3) == 2


class TestMultiply:
    def test_positive_numbers(self) -> None:
        assert multiply(2, 3) == 6
        assert multiply(4, 5) == 20

    def test_zero(self) -> None:
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0

    def test_negative_numbers(self) -> None:
        assert multiply(-2, 3) == -6
        assert multiply(2, -3) == -6
        assert multiply(-2, -3) == 6
