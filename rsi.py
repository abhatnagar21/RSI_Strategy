import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
stock = 'AAPL' 
start = '2023-01-01'
end = '2023-12-31'
data = yf.download(stock, start=start, end=end)
#print(data)
def calculate_rsi(data, window):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
window_length = 14
data['RSI'] = calculate_rsi(data, window_length)
#print(data)
#defining rsi when <30 undervalue(buy) when > 70 overvalue(sell)
data['signal'] = 0
data['signal'][data['RSI'] < 30] = 1
data['signal'][data['RSI'] > 70] = -1
data['positions'] = data['signal'].diff()
#print(data.head())
capital = 100000.0
positions = pd.DataFrame(index=data.index).fillna(0.0)
positions[stock] = data['signal']
portfolio = positions.multiply(data['Adj Close'], axis=0)
pos_diff = positions.diff()
portfolio['holdings'] = (positions.multiply(data['Adj Close'], axis=0)).sum(axis=1)
portfolio['cash'] = capital - (pos_diff.multiply(data['Adj Close'], axis=0)).sum(axis=1).cumsum()
portfolio['total'] = portfolio['cash'] + portfolio['holdings']
portfolio['returns'] = portfolio['total'].pct_change()
#plot
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Stock Price')
plt.plot(data['RSI'], label='RSI')
plt.plot(data.loc[data['positions'] == 1.0].index, data['RSI'][data['positions'] == 1.0], '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(data.loc[data['positions'] == -1.0].index, data['RSI'][data['positions'] == -1.0], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.axhline(30, color='red', linestyle='--', alpha=0.5)
plt.axhline(70, color='green', linestyle='--', alpha=0.5)
plt.title(f'{stock} RSI with Buy/Sell Signals')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.grid()
plt.show()
#value
plt.figure(figsize=(10, 6))
plt.plot(portfolio['total'], label='Portfolio Value')
plt.title('Portfolio Value Over Time')
plt.xlabel('Date')
plt.ylabel('Portfolio Value')
plt.legend()
plt.grid()
plt.show()
