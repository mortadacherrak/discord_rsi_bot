# Discord RSI Bot

This bot fetches the SOL/USDT spot K-line data from Bybit, calculates the RSI, and sends notifications to a Discord channel when RSI is above 70 or below 30.

## Setup

1. Create a Discord bot and get the token: https://discord.com/developers/docs/intro
2. Add the bot to your server.
3. Get the channel ID where you want the bot to send messages.

## Running the bot

### Using Docker

1. Build the Docker image:

```bash
docker build -t discord-rsi-bot .
```

2. Run the Docker container:

```bash
docker run -e DISCORD_TOKEN='YOUR_DISCORD_TOKEN' -e CHANNEL_ID='YOUR_CHANNEL_ID' discord-rsi-bot
```

### Without Docker

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Run the bot:

```bash
python discord_bot.py
```
