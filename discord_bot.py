import os
from bot import DiscordRSIBot

def main():
    token = os.getenv('DISCORD_TOKEN')
    channel_id = int(os.getenv('CHANNEL_ID'))
    symbol = 'SOLUSDT'
    interval = '60'
    bot = DiscordRSIBot(token, channel_id, symbol, interval)
    bot.run_bot()

if __name__ == '__main__':
    main()
