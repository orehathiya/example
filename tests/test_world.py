from example.world import world


def test_world() -> None:
    assert world() == "world"
