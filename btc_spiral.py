import pandas as pd
import numpy as np
from pandas_datapackage_reader import read_datapackage
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
plt.style.use("ggplot")

btc2usd = pd.read_csv(
    "btc_formatted.prn",
    delim_whitespace=True,
    header=None)
btc2usd['year'] = btc2usd.iloc[:, 0].apply(lambda x: x.split("/")[0]).astype(int)
btc2usd['month'] = btc2usd.iloc[:, 0].apply(lambda x: x.split("/")[1]).astype(int)
btc2usd = btc2usd.rename(columns={1: "value"})
btc2usd = btc2usd.iloc[:, 1:]
btc2usd.head()   

#btc2usd = btc2usd.drop(btc2usd[btc2usd['year'] == 201].index)
btc2usd = btc2usd.set_index(['year', 'month'])
print(btc2usd)

# btc2usd -= btc2usd.loc[2015:2019].mean()
btc2usd = btc2usd.reset_index()

# hc_1850 = btc2usd[btc2usd['year'] == 2015]
fig = plt.figure(figsize=(8,8))
ax1 = plt.subplot(111, projection='polar')
#r = hc_1850['value'] + 1
theta = np.linspace(0, 2*np.pi, 12)

#ax1.axes.get_yaxis().set_ticklabels([])
ax1.axes.get_xaxis().set_ticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
ax1.tick_params(axis='x', colors='white')

# formatter = ticker.FormatStrFormatter('$%1.2f')
# ax1.yaxis.set_major_formatter(formatter)

# for tick in ax1.yaxis.get_major_ticks():
#     tick.label1.set_visible(False)
#     tick.label2.set_visible(True)
#     tick.label2.set_color('green')
ax1.tick_params(axis='y', colors='green')

fig.set_facecolor("#323331")


ax1.set_title("BTC/USD 2015 - 2019", color='white', fontdict={'fontsize': 30})

years = btc2usd['year'].unique()


for year in years:
    r = btc2usd[btc2usd['year'] == year]['value'] + 1
    ax1.plot(theta, r)
plt.show()