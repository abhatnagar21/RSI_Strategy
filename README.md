This project leverages Python for analyzing stock data from Yahoo Finance, focusing on generating buy/sell signals based on the Relative Strength Index (RSI) and tracking portfolio performance over time.

Project Components
Data Collection and Preparation

Stock data is fetched using Yahoo Finance API (yfinance) for a specified stock (e.g., AAPL) and time period (e.g., 2023).
RSI is calculated to determine overbought (>70) and oversold (<30) conditions.
Signal Generation

Buy signals are generated when RSI < 30.
Sell signals are generated when RSI > 70.
Portfolio Management

A portfolio is initialized with a starting capital of $100,000.
Positions are taken based on the buy/sell signals generated.
Portfolio value and returns are tracked over time.
Visualization

Visualizations include:
Stock price and RSI with buy/sell signals plotted.
Portfolio value over time.
Requirements
Python 3.x
Required Python packages: yfinance, pandas, matplotlib, seaborn
