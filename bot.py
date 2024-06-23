import discord
import asyncio
from bybit_api import BybitAPI
from rsi_calculator import RSICalculator

class DiscordRSIBot(discord.Client):
    def __init__(self, token: str, channel_id: int, symbol: str, interval: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.channel_id = channel_id
        self.api = BybitAPI(symbol, interval)
        self.rsi_calculator = RSICalculator()
        self.loop.create_task(self.notify_rsi())

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def notify_rsi(self):
        await self.wait_until_ready()
        channel = self.get_channel(self.channel_id)
        while not self.is_closed():
            klines = self.api.fetch_klines()
            rsi = self.rsi_calculator.calculate(klines)
            if rsi > 70:
                await channel.send(f'RSI is above 70: {rsi}')
            elif rsi < 30:
                await channel.send(f'RSI is below 30: {rsi}')
            await asyncio.sleep(3600)  # Sleep for 1 hour

    def run_bot(self):
        self.run(self.token)