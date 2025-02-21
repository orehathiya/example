from example.hello import Example, hello


def test_hello(mocker):
    mocker.patch("test_hello.hello", return_value="hello function mocked!")
    assert hello() == "hello function mocked!"


def test_example(mocker):
    mocker.patch.object(
        Example, "example_method", return_value="example method mocked!"
    )
    ex = Example()
    assert ex.example_method() == "example method mocked!"
