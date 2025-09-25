# PartnershipBot

A simple Discord bot to manage and send partnership messages easily.

---

## Features

* Send partnership messages with a specified manager.
* Custom modal for entering partnership content.
* Automatically mentions the author, server name, manager, and optionally `@everyone`/`@here`.
* Configurable channel and emoji.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/PartnershipBot.git
cd PartnershipBot
```

2. **Install dependencies:**

```bash
pip install -U discord.py
```

3. **Configure the bot:**

Edit the `DISCORD_TOKEN`, `PARTNERSHIP_CHANNEL_ID`, and `EMOJI` variables in the script:

```python
# === CONFIGS === 
DISCORD_TOKEN = "" # Bot Token 
PARTNERSHIP_CHANNEL_ID = 1409569987424948306 # Channed ID 
EMOJI = "⭐" # Emoji 
# ===============================
```

---

## Usage

1. Run the bot:

```bash
python partnershipbot.py
```

2. Use the `/partnership manager` command in Discord.

3. Fill out the modal with your partnership message and submit.

4. The bot will post the formatted partnership message in the configured channel.

---

## Permissions

Make sure the bot has:

* Permission to send messages in the partnership channel.
* Permission to mention `@everyone` if needed.

---

## License

```
# Copyright (c) 2025 - .rotafn (VortexTeam) - All rights reserved.
# This code is protected by the VortexTeam (.rotafn) Proprietary License.
# Use, modification, or distribution is prohibited without written permission.
# The full version of the license is available upon request.
```

---

## Contributing

If you have suggestions or improvements, contact the author directly. This bot is proprietary, so pull requests or redistribution are not allowed without permission.

---

## Acknowledgements

* Built with [discord.py](https://discordpy.readthedocs.io/)
