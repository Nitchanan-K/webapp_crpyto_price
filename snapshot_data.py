from yahoo_fin.stock_info import *
from yahoo_fin.stock_info import get_analysts_info
import yahoo_fin.stock_info as si

def snapshot():
    with open('C:/Users/User/PycharmProjects/web_app_crypto_analyze/dataset/crypto_list.csv') as f:
        crypto_name = f.read().splitlines()
        for crypto in crypto_name:
            symbol = crypto.split()[0]
            data = get_data(symbol, start_date="07-01-2022",
                            end_date="08-26-2022", index_as_date=True,
                            interval="1d")
            data.to_csv(f'dataset/daily/{symbol}.csv')

snapshot()