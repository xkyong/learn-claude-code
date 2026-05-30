"""A minimal greeting example used for demonstrating refactoring."""


def greet(name: str) -> None:
    """Print a friendly greeting to the given name.

    Args:
        name: The name of the person (or entity) to greet.
    """
    message = f"Hello, {name}"
    print(message)


def main() -> None:
    """Entry point for running this module as a script."""
    greet("Claude")


if __name__ == "__main__":
    main()
