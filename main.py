# pip install yfinance
import yfinance as yf
import matplotlib.pyplot as plt
import json
from json import JSONEncoder
from matplotlib.lines import Line2D
from collections import deque
from priceActionPattern import getHigherLows, getHigherHighs, getLowerHighs, getLowerLows

start = '2021-01-01'
end = '2022-01-01'
ticker = 'BTC'
order = 5
K = 2
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

if __name__ == '__main__':
    # Load Data
    yfObj = yf.Ticker(ticker)
    data = yfObj.history(start='2021-01-01', end='2022-01-01')
    plt.figure(figsize=(15, 8))
    plt.plot(data['Close'])
    plt.title(f'Price Chart for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.show()
    close = data['Close'].values
    dates = data.index

    # Get parice action patterns
    hh = getHigherHighs(close, order, K)
    hl = getHigherLows(close, order, K)
    ll = getLowerLows(close, order, K)
    lh = getLowerHighs(close, order, K)
    print(dates)
    print(hh)
    # Save data
    dictionary = {
        "ticker": ticker,
        "startDate": start,
        "endDate": end,
        #"HigherHighs": hh,
        #"HigherLows": hl,
        #"LowerLows": ll,
        #LowerHighs": lh,
        #"dates": dates,
        #"close": close
    }
    # Serializing json
    #json_object = json.dumps(dictionary)
    json_object = json.dumps(dictionary)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    plt.figure(figsize=(15, 8))
    plt.plot(data['Close'])
    _ = [plt.plot(dates[i], close[i], c=colors[1]) for i in hh]
    _ = [plt.plot(dates[i], close[i], c=colors[2]) for i in hl]
    _ = [plt.plot(dates[i], close[i], c=colors[3]) for i in ll]
    _ = [plt.plot(dates[i], close[i], c=colors[4]) for i in lh]
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title(f'Potential Divergence Points for {ticker} Closing Price')
    legend_elements = [
        Line2D([0], [0], color=colors[0], label='Close'),
        Line2D([0], [0], color=colors[1], label='Higher Highs'),
        Line2D([0], [0], color=colors[2], label='Higher Lows'),
        Line2D([0], [0], color=colors[3], label='Lower Lows'),
        Line2D([0], [0], color=colors[4], label='Lower Highs')
    ]
    plt.legend(handles=legend_elements)
    plt.show()
