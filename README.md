# Roleplay Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue.svg)]() [![Lint](https://github.com/rakin406/roleplay_bot/actions/workflows/lint.yml/badge.svg)](https://github.com/rakin406/roleplay_bot/actions)

**Roleplay Bot** is a Python command-line chatbot for roleplaying. The bot plays a
character with a given name and personality, while you play another character. You
provide character names, optional descriptions, and an optional scenario, and the
bot generates in-character dialogue and actions.

## Prerequisites

- **Python 3.10+**
- **Ollama CLI:** [Install Ollama](https://ollama.com) and ensure it is running on your system. Ollama lets you use local LLMs via a simple Python API.
- **llama3.2 model:** Pull the `llama3.2` model for Ollama using the command `ollama pull llama3.2`.
- **(Optional) `uv` package manager:** For convenience, you can use [Astral UV](https://astral.sh/docs/uv) to manage dependencies. Install via `pip install uv` and use `uv sync` as shown below. Alternatively, you may install dependencies with pip manually.

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/rakin406/roleplay_bot.git
   cd roleplay_bot
   ```
2. **Install Python dependencies:**  
   You need the Ollama Python library (and optionally UV). For example:  
   ```bash
   pip install ollama
   ```  
   *Alternatively*, use the `uv` manager:  
   ```bash
   pip install uv
   uv sync
   ```

## Usage

Run the main script:

```bash
python main.py
```

You will be prompted for: **Bot’s nickname**, **Your nickname**, **Bot’s character description** (optional), **Your character description** (optional), and **Scenario and lore** (optional). For example:

```
Bot's nickname: Aria
Your nickname: Fin
Bot's character description (Optional): A mischievous forest pixie
Your character description (Optional): A brave ranger
Scenario and lore (Optional): In a misty woodland glade, a chance encounter...
```

After entering this information, the interactive chat begins.

```bash
>> Hello, Aria!
*Aria giggles and flutters a hand* Greetings, kind ranger. What brings you to my glade?
```

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request on GitHub.

## Contact

Rakin Rahman - rakinrahman406@gmail.com

## License

This project is released under the **MIT License** (see the [LICENSE](LICENSE) file). 
