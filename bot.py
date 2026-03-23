"""This module contains the AI chatbot."""

from dataclasses import dataclass


@dataclass
class BotParameters:
    """Class for storing bot information."""

    bot_name: str
    anon_name: str
    bot_description: str | None
    anon_description: str | None
    world: str | None  # Scenario and lore


class Bot:
    """Class for running the chatbot."""

    def __init__(self, params: BotParameters):
        self.params = params
