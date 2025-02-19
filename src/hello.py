from world import world

def hello() -> str:
    return 'Hello, world!'

def main() -> None:    
    print("Hello from example!")
    print("world() returns: ", world())


if __name__ == "__main__":
    main()