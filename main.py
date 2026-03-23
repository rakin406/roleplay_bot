"""This is the CLI program of the roleplay bot."""

import sys

from .bot import Bot, BotParameters


def validate(message: str) -> str:
    # TODO: Remove extra spaces between name.
    modified = message.strip()
    if not modified:
        raise ValueError("String cannot be empty")
    return modified


def main():
    """Main function."""
    try:
        bot_name = validate(input("Bot's nickname: "))
        username = validate(input("Your nickname: "))
    except ValueError:
        print("Invalid input")
        sys.exit(1)

    bot_description = input("Bot's character description (Optional): ").strip()
    user_description = input("Your character description (Optional): ").strip()
    scene = input("Scenario and lore (Optional): ").strip()

    params = BotParameters(
        bot_name=bot_name,
        anon_name=username,
        bot_description=bot_description,
        anon_description=user_description,
        scene=scene,
    )

    chatbot = Bot(params)


if __name__ == "__main__":
    main()
