"""This is the CLI program of the roleplay bot."""

import sys


def validate(message: str) -> str:
    if not message:
        raise ValueError("String cannot be empty")
    return message


def main():
    """Main function."""
    try:
        bot_name = validate(input("Bot's nickname: "))
        username = validate(input("Your nickname: "))
    except ValueError:
        print("Invalid input")
        sys.exit(1)

    bot_description = input("Bot's character description (Optional): ")
    user_description = input("Your character description (Optional): ")
    world = input("Scenario and lore (Optional): ")


if __name__ == "__main__":
    main()
