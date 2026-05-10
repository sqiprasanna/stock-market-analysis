import yfinance as yf
import polars as pl

def get_stock_data(ticker: str, period: str = "1y"):
    """Fetches stock data using yfinance and converts to Polars DataFrame."""
    df = yf.download(ticker, period=period)
    # Convert to Polars
    return pl.from_pandas(df.reset_index())

def get_market_metrics(ticker: str):
    """Fetches basic ticker info."""
    stock = yf.Ticker(ticker)
    return stock.info
