import requests

class BybitAPI:
    BASE_URL = 'https://api.bybit.com'

    def __init__(self, symbol: str, interval: str):
        self.symbol = symbol
        self.interval = interval

    def fetch_klines(self):
        endpoint = f'/v2/public/kline/list?symbol={self.symbol}&interval={self.interval}'
        response = requests.get(self.BASE_URL + endpoint)
        response.raise_for_status()
        return response.json()['result']