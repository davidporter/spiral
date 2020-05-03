import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import datetime
plt.style.use('fivethirtyeight')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 2)


btc = web.get_data_yahoo('BTC-USD', start=datetime.datetime(1990, 1, 1), end=datetime.datetime.now())
print(btc)

btc.to_csv('btc.csv')

with open('btc_file.txt', 'w') as f:
    print('Filename:', btc, file=f)


np.sum(btc['Close'] - btc['Adj Close'])

btc_adj = btc['Adj Close']
btc_adj.plot(lw=1.5, figsize=(24, 10))

plt.show()