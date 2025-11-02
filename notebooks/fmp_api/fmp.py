import os, sys, logging, requests
from datetime import datetime

if os.getcwd() not in sys.path: sys.path.append(os.getcwd())

logger = logging.basicConfig(
    level=logging.INFO,
    filename=f'{__name__}.log',
    filemode='w',
    format='%(asctime)s %(levelname)s %(message)s'
)

class FMP:

    def __init__(self):
        self.api_key = os.environ['api_key']
        logging.info(f"Class instance initiated the 'api_key' as {self.api_key}")
    
    def get_response(self, method: str, url: str, params: dict):
        r = requests.request(
            method=method,
            url=url,
            params=params
        )

        if r.status_code == 200:
            data = r.json()
            logging.info(f"{method} request to {url} was {r.status_code}")
            return data
        else:
            logging.error(f"{method} request to {url} was {r.status_code}")

    def etf_information(self, symbol: str = 'SPY'):
        etf_info = self.get_response(
                method='GET',
                url='https://financialmodelingprep.com/stable/etf/info',
                params={
                    'symbol': symbol,
                    'apikey': self.api_key
                }
        )

        if etf_info:
            logging.info(f"Information on '{symbol}' successfully retrieved")
            return etf_info
        else:
            logging.error(f"Information on '{symbol}' cannot be retrieved")
