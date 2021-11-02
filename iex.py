import requests

class Stock:

    def __init__(self, token, symbol):
        self.BASE_URL = 'https://cloud.iexapis.com/stable'
        self.token = token
        self.symbol = symbol
    
    def get_logo(self):
        tag = 'logo'
        url = f'{self.BASE_URL}/stock/{self.symbol}/{tag}?token={self.token}'
        r = requests.get(url)
        return r.json()

    def get_company_info(self):
        tag = 'company'
        url = f'{self.BASE_URL}/stock/{self.symbol}/{tag}?token={self.token}'
        r = requests.get(url)
        return r.json()

    def get_balance_sheet(self):
        tag = 'balance-sheet'
        url = f'{self.BASE_URL}/stock/{self.symbol}/{tag}?token={self.token}'
        r = requests.get(url)
        return r.json()

    def get_price(self):
        tag = 'price'
        url = f'{self.BASE_URL}/stock/{self.symbol}/{tag}?token={self.token}'
        r = requests.get(url)
        return r.json()

    def get_pervious(self):
        tag = 'previous'
        url = f'{self.BASE_URL}/stock/{self.symbol}/{tag}?token={self.token}'
        r = requests.get(url)
        return r.json()
    
    def get_news(self,last=10):
        tag = 'news'
        url = f'{self.BASE_URL}/stock/{self.symbol}/{tag}/last/{last}?token={self.token}'
        r = requests.get(url)
        return r.json()
