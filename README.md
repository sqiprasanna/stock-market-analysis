# Stock Market Analysis Dashboard

A real-time financial market analysis dashboard built with Python. This project provides interactive visualization, technical indicators, and real-time sentiment analysis for stocks.

## Features

- **Real-Time Data:** Fetches live stock market data using `yfinance`.
- **Interactive Visualization:** Dynamic candlestick charts built with `Plotly`.
- **Sentiment Analysis:** Real-time financial news sentiment scoring using `VADER` and the `Marketaux API`.
- **Dashboard UI:** Clean, responsive interface powered by `Streamlit`.

## Prerequisites

- Python 3.10+
- [Marketaux API Token](https://www.marketaux.com/) (Free tier available)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sqiprasanna/stock-market-analysis
   cd stock-market-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API Token:
   - Open `services/sentiment_service.py`.
   - Replace `'YOUR_MARKETAUX_API_TOKEN'` with your actual API token.

## Running the Application

Launch the dashboard locally:
```bash
streamlit run app.py
```

The application will be accessible at `http://localhost:8501`.

## Deployment

This dashboard can be deployed for free using [Streamlit Community Cloud](https://share.streamlit.io/):
1. Connect your GitHub repository to Streamlit Community Cloud.
2. Select your repository and `app.py` as the entry point.
3. Add your `API_TOKEN` in the Streamlit Cloud "Secrets" management.

## Tech Stack

- **Framework:** Streamlit
- **Data Acquisition:** `yfinance`, `OpenBB SDK`
- **Processing:** `Polars`, `Pandas`
- **Sentiment Analysis:** `VADER` (via `vaderSentiment`), `Marketaux API`
- **Charts:** `Plotly`

## License

This project is licensed under the MIT License.
