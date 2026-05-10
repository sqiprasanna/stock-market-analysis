import yfinance as yf
import polars as pl

import yfinance as yf
import polars as pl

def get_stock_data(ticker: str, period: str = "1y"):
    """Fetches stock data using yfinance and converts to Polars DataFrame."""
    df = yf.download(ticker, period=period)
    # Reset index to make 'Date' a column
    df = df.reset_index()
    
    # Debug print to check column names
    print(f"Columns after reset: {df.columns.tolist()}")
    
    # Ensure columns match expected casing
    return pl.from_pandas(df)

def get_market_metrics(ticker: str):
    """Fetches basic ticker info."""
    stock = yf.Ticker(ticker)
    return stock.info
