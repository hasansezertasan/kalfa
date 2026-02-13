from importlib.metadata import Distribution


def main() -> None:
    distribution = Distribution.from_name("kalfa")
    print(f"Name: {distribution.name}")
    print(f"Version: {distribution.version}")
