import yfinance as yf
import pandas as pd

def get_nse_stock_symbols():
    # NSE ke kuch popular stocks ka example list
    nse_stocks = ["TCS.NS", "INFY.NS", "RELIANCE.NS", "HDFCBANK.NS", "SBIN.NS", "ICICIBANK.NS", "AXISBANK.NS"]
    
    stock_data = []
    for symbol in nse_stocks:
        stock = yf.Ticker(symbol)
        info = stock.info
        stock_data.append({
            "Symbol": symbol,
            "Company": info.get("longName", "Unknown"),
            "Sector": info.get("sector", "Unknown")
        })

    df = pd.DataFrame(stock_data)
    df.to_csv("nse_stocks.csv", index=False)
    print("✅ NSE Stock List Saved!")

# Function Call
get_nse_stock_symbols()
