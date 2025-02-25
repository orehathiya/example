import configparser
import os

from example.world import world


def hello() -> str:
    return "Hello, world!"


def main() -> None:
    print("Hello from example!")
    print("world() returns: ", world())


class Example:
    def __init__(self) -> None:
        print("Example class created!")

    def example_method(self) -> str:
        return "Example method called!"


if __name__ == "__main__":
    main()
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    print(os.environ["CONDA_PYTHON_EXE"])
    print(cfg.get("System", "conda_location", vars=os.environ))
