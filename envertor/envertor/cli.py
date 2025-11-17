# envertor/cli.py
import argparse
from .core import generate_example_env
from .version import __version__

def main():
    parser = argparse.ArgumentParser(
        description="Envertor: Generate example .env files from existing .env"
    )

    parser.add_argument(
        "-i", "--input",
        default=".env",
        help="Path to input .env file"
    )
    parser.add_argument(
        "-o", "--output",
        default=".env.example",
        help="Path to output example .env file"
    )

    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show envertor version"
    )

    args = parser.parse_args()

    if args.version:
        print(f"envertor v{__version__}")
        return

    generate_example_env(args.input, args.output)
    print(f"Created: {args.output}")

