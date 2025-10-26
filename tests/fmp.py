import requests, os, sys


if os.getcwd() not in sys.path: sys.path.append(os.getcwd())

API_KEY = os.environ['api_key']

r = requests.request(
    method='GET',
    url='https://financialmodelingprep.com/stable/financial-reports-xlsx',
    params={
        'symbol': 'AAPL',
        'period': 'FY',
        'year': 2022,
        'apikey': API_KEY
    }
)


if r.status_code == 200:
    data = r.content
    print('API call successful')
    print(data)